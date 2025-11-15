"""
Scrape Grant Data from Public Sources
- Grants.gov API
- Foundation websites (if time allows)
"""

import requests
import sqlite3
from datetime import datetime
import xml.etree.ElementTree as ET

# Grants.gov API v2
# Docs: https://www.grants.gov/web/grants/xml-extract.html
GRANTS_GOV_API = "https://www.grants.gov/grantsws/rest/opportunities/search/"

def search_grants_gov(keywords=None, agency=None):
    """
    Search grants from Grants.gov API
    
    Args:
        keywords: Search terms (e.g., "health equity", "environmental justice")
        agency: Federal agency (e.g., "HHS", "EPA")
    """
    
    print("Searching Grants.gov...")
    
    # Build query parameters
    params = {}
    
    if keywords:
        params['keyword'] = keywords
    
    if agency:
        params['fundingInstrumentType'] = agency
    
    # TODO: Implement API call
    # Note: Grants.gov API can be slow and has rate limits
    
    grants = []
    
    try:
        # Example API call structure:
        # GET https://www.grants.gov/grantsws/rest/opportunities/search/
        # ?keyword=health+equity&oppStatus=posted
        
        # TODO: Parse XML response
        # TODO: Extract relevant fields
        # TODO: Filter for health/environment focus
        
        pass
        
    except Exception as e:
        print(f"Error fetching from Grants.gov: {e}")
    
    return grants

def scrape_foundation_grants():
    """
    Scrape grants from foundation websites
    
    Target foundations:
    - California Wellness Foundation
    - California Community Foundation  
    - California Endowment
    """
    
    print("Scraping foundation grants...")
    
    grants = []
    
    # TODO: Implement web scraping
    # Note: Respect robots.txt
    # Note: Add delays between requests
    
    # Sample foundation grant
    sample_grants = [
        {
            'title': 'California Wellness Foundation - Health Equity Grants',
            'funder': 'California Wellness Foundation',
            'description': 'Support organizations advancing health equity in California',
            'focus_area': 'health',
            'amount_min': 25000,
            'amount_max': 150000,
            'deadline': '2026-02-01',
            'geographic_eligibility': 'CA',
            'website_url': 'https://www.calwellness.org',
            'created_at': datetime.now().isoformat()
        }
    ]
    
    return sample_grants

def save_grants_to_database(grants):
    """Save grant data to database"""
    
    conn = sqlite3.connect('../backend/equitybridge.db')
    cursor = conn.cursor()
    
    for grant in grants:
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
    
    conn.commit()
    conn.close()
    
    print(f"✅ Saved {len(grants)} grants to database")

def main():
    """Main execution"""
    
    print("Starting grant data collection...")
    
    # Collect from multiple sources
    all_grants = []
    
    # 1. Grants.gov (federal)
    # federal_grants = search_grants_gov(keywords="health equity")
    # all_grants.extend(federal_grants)
    
    # 2. Foundation grants
    foundation_grants = scrape_foundation_grants()
    all_grants.extend(foundation_grants)
    
    # Save to database
    if all_grants:
        save_grants_to_database(all_grants)
        print(f"✅ Total grants collected: {len(all_grants)}")
    else:
        print("⚠️  No grants collected - using sample data from database.py")

if __name__ == "__main__":
    main()
