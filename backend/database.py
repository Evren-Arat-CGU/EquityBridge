"""
Database Setup for EquityBridge
Creates SQLite database and schema for grants
"""

import sqlite3
from datetime import datetime

def create_database():
    """Create database and tables"""
    
    conn = sqlite3.connect('equitybridge.db')
    cursor = conn.cursor()
    
    # Grants table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            funder TEXT NOT NULL,
            description TEXT,
            focus_area TEXT,  -- 'health', 'environment', 'both'
            amount_min INTEGER,
            amount_max INTEGER,
            deadline TEXT,
            geographic_eligibility TEXT,  -- 'federal', 'CA', 'county:riverside', etc.
            website_url TEXT,
            created_at TEXT
        )
    ''')
    
    # Nonprofits table (from 990 data)
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
    print("[OK] Database created successfully")
    
    # Insert sample data for testing
    insert_sample_data(cursor)
    conn.commit()
    print("[OK] Sample data inserted")
    
    conn.close()

def insert_sample_data(cursor):
    """Insert sample grants for testing"""
    
    sample_grants = [
        (
            "CDC Healthy Communities Program",
            "Centers for Disease Control",
            "Support community health initiatives addressing health disparities",
            "health",
            50000,
            300000,
            "2026-01-15",
            "federal",
            "https://www.cdc.gov/grants",
            datetime.now().isoformat()
        ),
        (
            "EPA Environmental Justice Grant",
            "Environmental Protection Agency",
            "Fund projects addressing environmental health in underserved communities",
            "environment",
            100000,
            500000,
            "2025-12-20",
            "federal",
            "https://www.epa.gov/environmentaljustice/grants",
            datetime.now().isoformat()
        ),
        (
            "California Wellness Foundation - Health Equity",
            "California Wellness Foundation",
            "Support health equity initiatives in California communities",
            "health",
            25000,
            150000,
            "2026-02-01",
            "CA",
            "https://www.calwellness.org",
            datetime.now().isoformat()
        )
    ]
    
    cursor.executemany('''
        INSERT INTO grants 
        (title, funder, description, focus_area, amount_min, amount_max, 
         deadline, geographic_eligibility, website_url, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_grants)

if __name__ == "__main__":
    create_database()
