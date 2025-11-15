"""
Scrape California Nonprofit 990 Data
Uses ProPublica Nonprofit Explorer API

Free API: No authentication required for basic usage
Docs: https://projects.propublica.org/nonprofits/api
"""

import requests
import sqlite3
import time
from datetime import datetime

# ProPublica Nonprofit Explorer API
API_BASE = "https://projects.propublica.org/nonprofits/api/v2"

def search_nonprofits_by_location(state="CA", focus_keywords=None):
    """
    Search for nonprofits in a specific state
    
    Args:
        state: Two-letter state code
        focus_keywords: List of keywords to filter (e.g., ["health", "environment"])
    """
    
    print(f"Searching nonprofits in {state}...")
    
    # TODO: Implement search logic
    # ProPublica API allows search by state
    # Filter results by focus keywords in name/mission
    
    nonprofits = []
    
    # Example API call structure:
    # GET /search.json?q=health&state[id]=CA
    
    return nonprofits

def get_nonprofit_details(ein):
    """
    Get detailed info for a specific nonprofit by EIN
    
    Args:
        ein: Employer Identification Number
    """
    
    url = f"{API_BASE}/organizations/{ein}.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        org = data.get('organization', {})
        
        return {
            'name': org.get('name'),
            'ein': ein,
            'zip_code': org.get('zip_code'),
            'city': org.get('city'),
            'state': org.get('state'),
            'revenue': org.get('revenue_amount'),
            'created_at': datetime.now().isoformat()
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {ein}: {e}")
        return None

def save_to_database(nonprofits):
    """Save nonprofit data to database"""
    
    conn = sqlite3.connect('../backend/equitybridge.db')
    cursor = conn.cursor()
    
    for org in nonprofits:
        cursor.execute('''
            INSERT INTO nonprofits 
            (name, ein, zip_code, county, revenue, focus_area, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            org['name'],
            org['ein'],
            org.get('zip_code'),
            org.get('county'),
            org.get('revenue'),
            org.get('focus_area'),
            org['created_at']
        ))
    
    conn.commit()
    conn.close()
    
    print(f"✅ Saved {len(nonprofits)} nonprofits to database")

def main():
    """Main execution"""
    
    # TODO: Implement full scraping logic
    # 1. Search for health-focused nonprofits in CA
    # 2. Search for environment-focused nonprofits in CA
    # 3. Get details for each
    # 4. Save to database
    
    print("Starting nonprofit data collection...")
    print("⚠️  TODO: Implement API calls")
    print("⚠️  TODO: Add rate limiting (be respectful of API)")
    print("⚠️  TODO: Filter for Inland Empire / target regions")
    
    # For now, use sample data
    sample_nonprofits = [
        {
            'name': 'Sample Community Health Clinic',
            'ein': '123456789',
            'zip_code': '92501',
            'county': 'Riverside',
            'revenue': 250000,
            'focus_area': 'health',
            'created_at': datetime.now().isoformat()
        }
    ]
    
    save_to_database(sample_nonprofits)

if __name__ == "__main__":
    main()
