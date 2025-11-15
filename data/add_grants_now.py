"""
ADD MORE GRANTS DIRECTLY TO DATABASE
No API calls needed - just adds realistic sample grants
"""

import sqlite3
from datetime import datetime, timedelta

db_path = r'C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\backend\equitybridge.db'

print("="*60)
print("ADDING GRANTS TO DATABASE")
print("="*60)
print()

# More realistic grants
additional_grants = [
    ("California Endowment - Building Healthy Communities", "The California Endowment", 
     "Multi-year investments in community health initiatives focused on systems change and health equity.", 
     "health", 50000, 300000, (datetime.now() + timedelta(days=45)).strftime('%Y-%m-%d'), 
     "CA", "https://www.calendow.org"),
    
    ("Silicon Valley Community Foundation - Environmental Justice", "Silicon Valley Community Foundation",
     "Support environmental justice work in disadvantaged communities throughout California.",
     "environment", 30000, 100000, (datetime.now() + timedelta(days=75)).strftime('%Y-%m-%d'),
     "CA", "https://www.siliconvalleycf.org"),
    
    ("California Community Foundation - Healthy Communities", "California Community Foundation",
     "Grants to improve health outcomes in Los Angeles County communities.",
     "health", 20000, 75000, (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d'),
     "CA", "https://www.calfund.org"),
    
    ("Riverside Community Foundation - Local Health Grants", "Riverside Community Foundation",
     "Small grants for health programs serving Riverside and San Bernardino counties.",
     "health", 10000, 50000, (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
     "county:riverside", "https://www.riversidecommunityfoundation.org"),
    
    ("Resources Legacy Fund - Environmental Conservation", "Resources Legacy Fund",
     "Support environmental conservation and climate resilience projects in California.",
     "environment", 40000, 200000, (datetime.now() + timedelta(days=120)).strftime('%Y-%m-%d'),
     "CA", "https://www.resourceslegacyfund.org"),
    
    ("California Health Care Foundation - Health Access", "California Health Care Foundation",
     "Improve access to quality health care for underserved Californians.",
     "health", 35000, 150000, (datetime.now() + timedelta(days=105)).strftime('%Y-%m-%d'),
     "CA", "https://www.chcf.org"),
    
    ("San Diego Foundation - Environmental Stewardship", "San Diego Foundation",
     "Support environmental education and conservation in San Diego County.",
     "environment", 15000, 60000, (datetime.now() + timedelta(days=50)).strftime('%Y-%m-%d'),
     "county:san_diego", "https://www.sdfoundation.org"),
    
    ("CDC Health Disparities Grant", "Centers for Disease Control",
     "Funding for programs addressing health disparities in underserved populations.",
     "health", 75000, 400000, (datetime.now() + timedelta(days=120)).strftime('%Y-%m-%d'),
     "federal", "https://www.cdc.gov/grants"),
    
    ("EPA Environmental Justice Small Grants", "Environmental Protection Agency",
     "Support community-driven projects addressing environmental justice concerns.",
     "environment", 30000, 75000, (datetime.now() + timedelta(days=100)).strftime('%Y-%m-%d'),
     "federal", "https://www.epa.gov/environmentaljustice"),
    
    ("HHS Community Health Centers Grant", "Health and Human Services",
     "Funding for community health centers serving vulnerable populations.",
     "health", 100000, 650000, (datetime.now() + timedelta(days=150)).strftime('%Y-%m-%d'),
     "federal", "https://www.hhs.gov/grants"),
    
    ("California Air Resources Board - Community Air Protection", "California Air Resources Board",
     "Fund projects reducing air pollution in disadvantaged communities.",
     "environment", 25000, 150000, (datetime.now() + timedelta(days=80)).strftime('%Y-%m-%d'),
     "CA", "https://ww2.arb.ca.gov/our-work/programs/community-air-protection-program"),
    
    ("Sierra Health Foundation - Health Equity Grants", "Sierra Health Foundation",
     "Support initiatives advancing health equity in Northern California.",
     "health", 20000, 100000, (datetime.now() + timedelta(days=65)).strftime('%Y-%m-%d'),
     "CA", "https://www.sierrahealth.org"),
    
    ("Orange County Community Foundation - Health Programs", "Orange County Community Foundation",
     "Grants for health programs serving Orange County residents.",
     "health", 15000, 60000, (datetime.now() + timedelta(days=55)).strftime('%Y-%m-%d'),
     "county:orange", "https://www.occf.org"),
    
    ("The California Wellness Foundation - Advancing Health Equity", "California Wellness Foundation",
     "Multi-year grants for organizations advancing health equity statewide.",
     "health", 50000, 250000, (datetime.now() + timedelta(days=95)).strftime('%Y-%m-%d'),
     "CA", "https://www.calwellness.org"),
    
    ("Wildlife Conservation Board - Habitat Restoration", "Wildlife Conservation Board",
     "Fund habitat restoration and environmental protection projects.",
     "environment", 35000, 175000, (datetime.now() + timedelta(days=110)).strftime('%Y-%m-%d'),
     "CA", "https://wcb.ca.gov"),
]

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    added = 0
    for grant in additional_grants:
        try:
            cursor.execute('''
                INSERT INTO grants 
                (title, funder, description, focus_area, amount_min, amount_max,
                 deadline, geographic_eligibility, website_url, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (*grant, datetime.now().isoformat()))
            added += 1
            print(f"[OK] Added: {grant[0][:50]}...")
        except sqlite3.IntegrityError:
            pass  # Skip duplicates
    
    conn.commit()
    
    # Check total
    cursor.execute('SELECT COUNT(*) FROM grants')
    total = cursor.fetchone()[0]
    
    conn.close()
    
    print()
    print("="*60)
    print(f"[SUCCESS] Added {added} new grants")
    print(f"[SUCCESS] Total grants in database: {total}")
    print("="*60)
    print()
    print("Database is ready!")
    print()
    
except Exception as e:
    print(f"[ERROR] {e}")

input("Press ENTER to close...")
