"""
Working Nonprofit 990 Data Scraper
Uses ProPublica Nonprofit Explorer API to get real California nonprofit data
"""

import requests
import sqlite3
import time
from datetime import datetime

# ProPublica Nonprofit Explorer API
API_BASE = "https://projects.propublica.org/nonprofits/api/v2"

def search_california_nonprofits(search_term, max_results=20):
    """
    Search for nonprofits in California by keyword
    
    Args:
        search_term: Keyword to search (e.g., "health", "environment")
        max_results: Maximum number of results to return
    """
    
    print(f"\n🔍 Searching for '{search_term}' nonprofits in California...")
    
    nonprofits = []
    
    try:
        # ProPublica API search endpoint
        # Format: /search.json?q=keyword&state[id]=CA
        url = f"{API_BASE}/search.json"
        params = {
            'q': search_term,
            'state[id]': 'CA'
        }
        
        response = requests.get(url, params=params, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            organizations = data.get('organizations', [])[:max_results]
            
            print(f"   Found {len(organizations)} organizations")
            
            for org in organizations:
                # Get basic info
                nonprofit = {
                    'name': org.get('name'),
                    'ein': org.get('ein'),
                    'zip_code': org.get('zipcode'),
                    'city': org.get('city'),
                    'state': org.get('state'),
                    'revenue': None,  # Will try to get from detail
                    'focus_area': search_term,  # Tag with search term
                    'created_at': datetime.now().isoformat()
                }
                
                nonprofits.append(nonprofit)
                
            print(f"   ✅ Collected {len(nonprofits)} nonprofit records")
            
        else:
            print(f"   ⚠️  API returned status {response.status_code}")
            
    except requests.exceptions.Timeout:
        print(f"   ⚠️  Request timed out - API may be slow")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    return nonprofits

def get_nonprofit_details(ein):
    """
    Get detailed financial info for a specific nonprofit
    
    Args:
        ein: Employer Identification Number
    """
    
    try:
        url = f"{API_BASE}/organizations/{ein}.json"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            org = data.get('organization', {})
            
            # Get most recent filing for revenue
            filings = data.get('filings_with_data', [])
            revenue = None
            
            if filings:
                latest = filings[0]
                revenue = latest.get('totrevenue')
            
            return {
                'revenue': revenue,
                'city': org.get('city'),
                'state': org.get('state'),
                'zip_code': org.get('zipcode')
            }
        else:
            return None
            
    except Exception as e:
        return None

def enrich_nonprofit_data(nonprofits, max_details=10):
    """
    Enrich nonprofit data with detailed financial info
    Limited to avoid rate limiting
    
    Args:
        nonprofits: List of nonprofit dicts
        max_details: Maximum number to enrich (to avoid rate limits)
    """
    
    print(f"\n💰 Enriching {min(len(nonprofits), max_details)} records with financial data...")
    
    for i, nonprofit in enumerate(nonprofits[:max_details]):
        ein = nonprofit.get('ein')
        if ein:
            print(f"   Fetching details for {nonprofit['name'][:40]}...")
            details = get_nonprofit_details(ein)
            
            if details and details.get('revenue'):
                nonprofit['revenue'] = details['revenue']
                # Update location info if missing
                if not nonprofit.get('city') and details.get('city'):
                    nonprofit['city'] = details['city']
                if not nonprofit.get('zip_code') and details.get('zip_code'):
                    nonprofit['zip_code'] = details['zip_code']
            
            time.sleep(0.5)  # Rate limiting - be respectful
    
    print(f"   ✅ Enrichment complete")
    
    return nonprofits

def map_city_to_county(city):
    """
    Map California cities to counties
    Simple mapping for common cities
    """
    
    county_map = {
        'riverside': 'Riverside',
        'corona': 'Riverside',
        'moreno valley': 'Riverside',
        'los angeles': 'Los Angeles',
        'san diego': 'San Diego',
        'san francisco': 'San Francisco',
        'oakland': 'Alameda',
        'berkeley': 'Alameda',
        'sacramento': 'Sacramento',
        'fresno': 'Fresno',
        'san jose': 'Santa Clara'
    }
    
    if city:
        city_lower = city.lower()
        return county_map.get(city_lower, None)
    
    return None

def save_nonprofits_to_database(nonprofits):
    """Save nonprofit data to SQLite database"""
    
    if not nonprofits:
        print("\n⚠️  No nonprofits to save")
        return 0
    
    print(f"\n💾 Saving {len(nonprofits)} nonprofits to database...")
    
    try:
        conn = sqlite3.connect('../backend/equitybridge.db')
        cursor = conn.cursor()
        
        saved_count = 0
        
        for org in nonprofits:
            try:
                # Map city to county
                county = map_city_to_county(org.get('city'))
                
                cursor.execute('''
                    INSERT INTO nonprofits 
                    (name, ein, zip_code, county, revenue, focus_area, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    org.get('name'),
                    org.get('ein'),
                    org.get('zip_code'),
                    county,
                    org.get('revenue'),
                    org.get('focus_area'),
                    org['created_at']
                ))
                saved_count += 1
            except sqlite3.IntegrityError:
                # Skip duplicates
                continue
        
        conn.commit()
        conn.close()
        
        print(f"   ✅ Successfully saved {saved_count} nonprofits to database")
        return saved_count
        
    except Exception as e:
        print(f"   ❌ Error saving to database: {e}")
        return 0

def main():
    """Main execution"""
    
    print("=" * 60)
    print("🏥 EQUITYBRIDGE NONPROFIT DATA COLLECTOR")
    print("=" * 60)
    
    all_nonprofits = []
    
    # Search terms for health and environmental organizations
    search_terms = [
        ('health', 15),
        ('community health', 10),
        ('environmental', 10),
        ('conservation', 10)
    ]
    
    # Collect nonprofits for each search term
    for term, max_results in search_terms:
        nonprofits = search_california_nonprofits(term, max_results)
        all_nonprofits.extend(nonprofits)
        time.sleep(1)  # Rate limiting between searches
    
    # Remove duplicates based on EIN
    seen_eins = set()
    unique_nonprofits = []
    
    for org in all_nonprofits:
        ein = org.get('ein')
        if ein and ein not in seen_eins:
            seen_eins.add(ein)
            unique_nonprofits.append(org)
    
    print(f"\n📊 Collected {len(unique_nonprofits)} unique nonprofits")
    
    # Enrich first 10 with detailed financial data
    if unique_nonprofits:
        enriched = enrich_nonprofit_data(unique_nonprofits, max_details=10)
        
        # Save to database
        saved_count = save_nonprofits_to_database(enriched)
        
        print("\n" + "=" * 60)
        print(f"✅ COMPLETE: {saved_count} nonprofits saved to database")
        print("=" * 60)
        print("\n💡 Nonprofit data ready for matching algorithm!")
    else:
        print("\n❌ No nonprofits collected")

if __name__ == "__main__":
    main()
