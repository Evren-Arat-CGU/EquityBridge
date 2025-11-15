"""
Working Grant Scraper - Grants.gov API + Sample Foundations
Fetches real grant data and saves to database
"""

import requests
import sqlite3
import json
from datetime import datetime, timedelta
import time

# Grants.gov API (simplified approach)
# Note: Full API requires registration, we'll use search endpoint
GRANTS_GOV_SEARCH = "https://apply07.grants.gov/grantsws/rest/opportunities/search/"

def fetch_grants_gov_grants():
    """
    Fetch grants from Grants.gov API
    Focus on health and environmental grants
    """
    
    print("\n🔍 Fetching federal grants from Grants.gov...")
    
    grants = []
    
    # Search terms for health equity and environmental justice
    search_terms = [
        "health equity",
        "environmental justice", 
        "community health",
        "environmental health"
    ]
    
    for term in search_terms:
        try:
            print(f"   Searching for: {term}")
            
            # Build API request
            params = {
                'keyword': term,
                'oppStatus': 'posted',
                'rows': 10  # Get 10 per search term
            }
            
            response = requests.get(GRANTS_GOV_SEARCH, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                opportunities = data.get('oppHits', [])
                
                for opp in opportunities:
                    # Extract grant info
                    grant = {
                        'title': opp.get('title', 'Untitled Grant'),
                        'funder': opp.get('agencyName', 'Federal Agency'),
                        'description': opp.get('description', '')[:500],  # Truncate
                        'focus_area': 'health' if 'health' in term.lower() else 'environment',
                        'amount_min': opp.get('awardFloor', 50000),
                        'amount_max': opp.get('awardCeiling', 500000),
                        'deadline': opp.get('closeDate', (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')),
                        'geographic_eligibility': 'federal',
                        'website_url': f"https://www.grants.gov/view-opportunity.html?oppId={opp.get('id', '')}",
                        'created_at': datetime.now().isoformat()
                    }
                    
                    grants.append(grant)
                    
                print(f"   ✅ Found {len(opportunities)} grants for '{term}'")
                
            else:
                print(f"   ⚠️  API returned status {response.status_code}")
                
            time.sleep(1)  # Rate limiting - be respectful
            
        except requests.exceptions.Timeout:
            print(f"   ⚠️  Request timed out for '{term}' - skipping")
            continue
        except Exception as e:
            print(f"   ⚠️  Error searching '{term}': {e}")
            continue
    
    return grants

def generate_california_foundation_grants():
    """
    Generate realistic California foundation grants
    Based on actual foundations but with sample data
    """
    
    print("\n📚 Generating California foundation grants...")
    
    # Real California foundations with realistic grant programs
    foundation_grants = [
        {
            'title': 'California Wellness Foundation - Health Equity Initiative',
            'funder': 'California Wellness Foundation',
            'description': 'Support organizations advancing health equity in underserved California communities through community-based programs.',
            'focus_area': 'health',
            'amount_min': 25000,
            'amount_max': 150000,
            'deadline': (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d'),
            'geographic_eligibility': 'CA',
            'website_url': 'https://www.calwellness.org',
            'created_at': datetime.now().isoformat()
        },
        {
            'title': 'California Endowment - Building Healthy Communities',
            'funder': 'The California Endowment',
            'description': 'Multi-year investments in community health initiatives focused on systems change and health equity.',
            'focus_area': 'health',
            'amount_min': 50000,
            'amount_max': 300000,
            'deadline': (datetime.now() + timedelta(days=45)).strftime('%Y-%m-%d'),
            'geographic_eligibility': 'CA',
            'website_url': 'https://www.calendow.org',
            'created_at': datetime.now().isoformat()
        },
        {
            'title': 'Silicon Valley Community Foundation - Environmental Justice',
            'funder': 'Silicon Valley Community Foundation',
            'description': 'Support environmental justice work in disadvantaged communities throughout California.',
            'focus_area': 'environment',
            'amount_min': 30000,
            'amount_max': 100000,
            'deadline': (datetime.now() + timedelta(days=75)).strftime('%Y-%m-%d'),
            'geographic_eligibility': 'CA',
            'website_url': 'https://www.siliconvalleycf.org',
            'created_at': datetime.now().isoformat()
        },
        {
            'title': 'California Community Foundation - Healthy Communities',
            'funder': 'California Community Foundation',
            'description': 'Grants to improve health outcomes in Los Angeles County communities.',
            'focus_area': 'health',
            'amount_min': 20000,
            'amount_max': 75000,
            'deadline': (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d'),
            'geographic_eligibility': 'CA',
            'website_url': 'https://www.calfund.org',
            'created_at': datetime.now().isoformat()
        },
        {
            'title': 'Resources Legacy Fund - Environmental Conservation',
            'funder': 'Resources Legacy Fund',
            'description': 'Support environmental conservation and climate resilience projects in California.',
            'focus_area': 'environment',
            'amount_min': 40000,
            'amount_max': 200000,
            'deadline': (datetime.now() + timedelta(days=120)).strftime('%Y-%m-%d'),
            'geographic_eligibility': 'CA',
            'website_url': 'https://www.resourceslegacyfund.org',
            'created_at': datetime.now().isoformat()
        },
        {
            'title': 'California Health Care Foundation - Health Access',
            'funder': 'California Health Care Foundation',
            'description': 'Improve access to quality health care for underserved Californians.',
            'focus_area': 'health',
            'amount_min': 35000,
            'amount_max': 150000,
            'deadline': (datetime.now() + timedelta(days=105)).strftime('%Y-%m-%d'),
            'geographic_eligibility': 'CA',
            'website_url': 'https://www.chcf.org',
            'created_at': datetime.now().isoformat()
        },
        {
            'title': 'Riverside Community Foundation - Local Health Grants',
            'funder': 'Riverside Community Foundation',
            'description': 'Small grants for health programs serving Riverside and San Bernardino counties.',
            'focus_area': 'health',
            'amount_min': 10000,
            'amount_max': 50000,
            'deadline': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
            'geographic_eligibility': 'county:riverside',
            'website_url': 'https://www.riversidecommunityfoundation.org',
            'created_at': datetime.now().isoformat()
        },
        {
            'title': 'San Diego Foundation - Environmental Stewardship',
            'funder': 'San Diego Foundation',
            'description': 'Support environmental education and conservation in San Diego County.',
            'focus_area': 'environment',
            'amount_min': 15000,
            'amount_max': 60000,
            'deadline': (datetime.now() + timedelta(days=50)).strftime('%Y-%m-%d'),
            'geographic_eligibility': 'county:san_diego',
            'website_url': 'https://www.sdfoundation.org',
            'created_at': datetime.now().isoformat()
        }
    ]
    
    print(f"   ✅ Generated {len(foundation_grants)} foundation grants")
    
    return foundation_grants

def save_grants_to_database(grants):
    """Save grant data to SQLite database"""
    
    if not grants:
        print("\n⚠️  No grants to save")
        return 0
    
    print(f"\n💾 Saving {len(grants)} grants to database...")
    
    try:
        conn = sqlite3.connect('../backend/equitybridge.db')
        cursor = conn.cursor()
        
        saved_count = 0
        
        for grant in grants:
            try:
                cursor.execute('''
                    INSERT INTO grants 
                    (title, funder, description, focus_area, amount_min, amount_max,
                     deadline, geographic_eligibility, website_url, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    grant['title'],
                    grant['funder'],
                    grant.get('description'),
                    grant.get('focus_area'),
                    grant.get('amount_min'),
                    grant.get('amount_max'),
                    grant.get('deadline'),
                    grant.get('geographic_eligibility'),
                    grant.get('website_url'),
                    grant['created_at']
                ))
                saved_count += 1
            except sqlite3.IntegrityError:
                # Skip duplicates
                continue
        
        conn.commit()
        conn.close()
        
        print(f"   ✅ Successfully saved {saved_count} grants to database")
        return saved_count
        
    except Exception as e:
        print(f"   ❌ Error saving to database: {e}")
        return 0

def main():
    """Main execution"""
    
    print("=" * 60)
    print("🚀 EQUITYBRIDGE GRANT DATA COLLECTOR")
    print("=" * 60)
    
    all_grants = []
    
    # 1. Fetch from Grants.gov API (federal grants)
    try:
        federal_grants = fetch_grants_gov_grants()
        all_grants.extend(federal_grants)
    except Exception as e:
        print(f"\n⚠️  Error fetching federal grants: {e}")
        print("   Continuing with foundation grants...")
    
    # 2. Generate California foundation grants
    foundation_grants = generate_california_foundation_grants()
    all_grants.extend(foundation_grants)
    
    # 3. Save to database
    if all_grants:
        saved_count = save_grants_to_database(all_grants)
        
        print("\n" + "=" * 60)
        print(f"✅ COMPLETE: {saved_count} grants saved to database")
        print("=" * 60)
        print("\n💡 Next steps:")
        print("   1. Start backend: cd backend && python main.py")
        print("   2. Open frontend: frontend/index.html")
        print("   3. Test grant matching!")
    else:
        print("\n❌ No grants collected - check database.py for sample data")

if __name__ == "__main__":
    main()
