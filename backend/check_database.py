"""Quick check of database contents"""
import sqlite3
import os

db_path = 'equitybridge.db'

if not os.path.exists(db_path):
    print("❌ Database file NOT found!")
    print(f"   Looking for: {os.path.abspath(db_path)}")
else:
    print("✅ Database file exists!")
    print(f"   Location: {os.path.abspath(db_path)}")
    print(f"   Size: {os.path.getsize(db_path)} bytes")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check grants
        cursor.execute('SELECT COUNT(*) FROM grants')
        grant_count = cursor.fetchone()[0]
        
        # Check nonprofits
        cursor.execute('SELECT COUNT(*) FROM nonprofits')
        nonprofit_count = cursor.fetchone()[0]
        
        print("\n📊 DATABASE CONTENTS:")
        print(f"   Grants: {grant_count}")
        print(f"   Nonprofits: {nonprofit_count}")
        
        if grant_count > 0:
            print("\n📋 Sample grants:")
            cursor.execute('SELECT title, funder FROM grants LIMIT 5')
            for title, funder in cursor.fetchall():
                print(f"   - {title[:60]}... ({funder})")
        
        if nonprofit_count > 0:
            print("\n🏥 Sample nonprofits:")
            cursor.execute('SELECT name, city FROM nonprofits LIMIT 5')
            for name, city in cursor.fetchall():
                print(f"   - {name[:60]}... ({city})")
        
        conn.close()
        
        # Status
        print("\n" + "="*60)
        if grant_count >= 10 and nonprofit_count >= 5:
            print("✅ DATA COLLECTION SUCCESSFUL!")
            print("   Ready to start backend and test matching!")
        elif grant_count > 0 or nonprofit_count > 0:
            print("⚠️  PARTIAL DATA COLLECTION")
            print("   Some data exists but might need more")
        else:
            print("❌ NO DATA IN DATABASE")
            print("   Need to run data collection scripts")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error reading database: {e}")
