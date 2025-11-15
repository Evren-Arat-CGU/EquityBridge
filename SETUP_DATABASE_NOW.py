"""
MASTER DATABASE SETUP - Run this ONCE to set up everything
Creates tables and loads 18+ grants
"""

import sqlite3
from datetime import datetime, timedelta
import os

# Database path
db_path = r'C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\backend\equitybridge.db'

print("="*70)
print("EQUITYBRIDGE DATABASE SETUP - COMPLETE INITIALIZATION")
print("="*70)
print()

# Step 1: Create tables
print("STEP 1: Creating database tables...")
print("-"*70)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Grants table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            funder TEXT NOT NULL,
            description TEXT,
            focus_area TEXT,
            amount_min INTEGER,
            amount_max INTEGER,
            deadline TEXT,
            geographic_eligibility TEXT,
            website_url TEXT,
            created_at TEXT
        )
    ''')
    
    # Nonprofits table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nonprofits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ein TEXT,
            zip_code TEXT,
            county TEXT,
            revenue INTEGER,
            focus_area TEXT,
            created_at TEXT
        )
    ''')
    
    conn.commit()
    print("[OK] Tables created successfully")
    
except Exception as e:
    print(f"[ERROR] Failed to create tables: {e}")
    exit(1)

# Step 2: Add grants
print("\nSTEP 2: Adding grants to database...")
print("-"*70)

grants = [
    ("CDC Healthy Communities Program", "Centers for Disease Control",
     "Support community health initiatives addressing health disparities",
     "health", 50000, 300000, "2026-01-15", "federal", "https://www.cdc.gov/grants"),
    
    ("EPA Environmental Justice Grant", "Environmental Protection Agency",
     "Fund projects addressing environmental health in underserved communities",
     "environment", 100000, 500000, "2025-12-20", "federal", "https://www.epa.gov/environmentaljustice/grants"),
    
    ("California Wellness Foundation - Health Equity", "California Wellness Foundation",
     "Support health equity initiatives in California communities",
     "health", 25000, 150000, "2026-02-01", "CA", "https://www.calwellness.org"),
    
    ("California Endowment - Building Healthy Communities", "The California Endowment",
     "Multi-year investments in community health initiatives focused on systems change",
     "health", 50000, 300000, (datetime.now() + timedelta(days=45)).strftime('%Y-%m-%d'),
     "CA", "https://www.calendow.org"),
    
    ("Silicon Valley Community Foundation - Environmental Justice", "Silicon Valley Community Foundation",
     "Support environmental justice work in disadvantaged communities",
     "environment", 30000, 100000, (datetime.now() + timedelta(days=75)).strftime('%Y-%m-%d'),
     "CA", "https://www.siliconvalleycf.org"),
    
    ("California Community Foundation - Healthy Communities", "California Community Foundation",
     "Grants to improve health outcomes in Los Angeles County communities",
     "health", 20000, 75000, (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d'),
     "CA", "https://www.calfund.org"),
    
    ("Riverside Community Foundation - Local Health Grants", "Riverside Community Foundation",
     "Small grants for health programs serving Riverside and San Bernardino counties",
     "health", 10000, 50000, (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
     "county:riverside", "https://www.riversidecommunityfoundation.org"),
    
    ("Resources Legacy Fund - Environmental Conservation", "Resources Legacy Fund",
     "Support environmental conservation and climate resilience projects",
     "environment", 40000, 200000, (datetime.now() + timedelta(days=120)).strftime('%Y-%m-%d'),
     "CA", "https://www.resourceslegacyfund.org"),
    
    ("California Health Care Foundation - Health Access", "California Health Care Foundation",
     "Improve access to quality health care for underserved Californians",
     "health", 35000, 150000, (datetime.now() + timedelta(days=105)).strftime('%Y-%m-%d'),
     "CA", "https://www.chcf.org"),
    
    ("San Diego Foundation - Environmental Stewardship", "San Diego Foundation",
     "Support environmental education and conservation in San Diego County",
     "environment", 15000, 60000, (datetime.now() + timedelta(days=50)).strftime('%Y-%m-%d'),
     "county:san_diego", "https://www.sdfoundation.org"),
    
    ("CDC Health Disparities Grant", "Centers for Disease Control",
     "Funding for programs addressing health disparities in underserved populations",
     "health", 75000, 400000, (datetime.now() + timedelta(days=120)).strftime('%Y-%m-%d'),
     "federal", "https://www.cdc.gov/grants"),
    
    ("EPA Environmental Justice Small Grants", "Environmental Protection Agency",
     "Support community-driven projects addressing environmental justice concerns",
     "environment", 30000, 75000, (datetime.now() + timedelta(days=100)).strftime('%Y-%m-%d'),
     "federal", "https://www.epa.gov/environmentaljustice"),
    
    ("HHS Community Health Centers Grant", "Health and Human Services",
     "Funding for community health centers serving vulnerable populations",
     "health", 100000, 650000, (datetime.now() + timedelta(days=150)).strftime('%Y-%m-%d'),
     "federal", "https://www.hhs.gov/grants"),
    
    ("California Air Resources Board - Community Air Protection", "California Air Resources Board",
     "Fund projects reducing air pollution in disadvantaged communities",
     "environment", 25000, 150000, (datetime.now() + timedelta(days=80)).strftime('%Y-%m-%d'),
     "CA", "https://ww2.arb.ca.gov/our-work/programs/community-air-protection-program"),
    
    ("Sierra Health Foundation - Health Equity Grants", "Sierra Health Foundation",
     "Support initiatives advancing health equity in Northern California",
     "health", 20000, 100000, (datetime.now() + timedelta(days=65)).strftime('%Y-%m-%d'),
     "CA", "https://www.sierrahealth.org"),
    
    ("Orange County Community Foundation - Health Programs", "Orange County Community Foundation",
     "Grants for health programs serving Orange County residents",
     "health", 15000, 60000, (datetime.now() + timedelta(days=55)).strftime('%Y-%m-%d'),
     "county:orange", "https://www.occf.org"),
    
    ("The California Wellness Foundation - Advancing Health Equity", "California Wellness Foundation",
     "Multi-year grants for organizations advancing health equity statewide",
     "health", 50000, 250000, (datetime.now() + timedelta(days=95)).strftime('%Y-%m-%d'),
     "CA", "https://www.calwellness.org"),
    
    ("Wildlife Conservation Board - Habitat Restoration", "Wildlife Conservation Board",
     "Fund habitat restoration and environmental protection projects",
     "environment", 35000, 175000, (datetime.now() + timedelta(days=110)).strftime('%Y-%m-%d'),
     "CA", "https://wcb.ca.gov"),
]

added = 0
for grant in grants:
    try:
        cursor.execute('''
            INSERT INTO grants 
            (title, funder, description, focus_area, amount_min, amount_max,
             deadline, geographic_eligibility, website_url, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (*grant, datetime.now().isoformat()))
        added += 1
        print(f"[OK] Added: {grant[0][:60]}")
    except Exception as e:
        print(f"[SKIP] {grant[0][:60]}: {e}")

conn.commit()

# Verify
cursor.execute('SELECT COUNT(*) FROM grants')
total_grants = cursor.fetchone()[0]

cursor.execute('SELECT COUNT(*) FROM nonprofits')
total_nonprofits = cursor.fetchone()[0]

conn.close()

print()
print("="*70)
print("DATABASE SETUP COMPLETE!")
print("="*70)
print(f"\nTotal grants: {total_grants}")
print(f"Total nonprofits: {total_nonprofits}")
print()
print("Database location:")
print(f"  {db_path}")
print()
print("="*70)
print()
print("NEXT STEPS:")
print("  1. Start backend: cd backend && python main.py")
print("  2. Open frontend/index.html in browser")
print("  3. Test grant matching!")
print()
print("="*70)
print()
input("Press ENTER to close...")
