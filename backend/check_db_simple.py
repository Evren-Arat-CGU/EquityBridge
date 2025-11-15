"""Quick check of database contents - Windows compatible"""
import sqlite3
import os

db_path = 'equitybridge.db'

print("="*60)
print("EQUITYBRIDGE DATABASE STATUS REPORT")
print("="*60)
print("")

if not os.path.exists(db_path):
    print("[ERROR] Database file NOT found!")
    print(f"   Looking for: {os.path.abspath(db_path)}")
else:
    print("[OK] Database file exists!")
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
        
        print("")
        print("DATABASE CONTENTS:")
        print(f"   Grants: {grant_count}")
        print(f"   Nonprofits: {nonprofit_count}")
        
        if grant_count > 0:
            print("")
            print("Sample grants:")
            cursor.execute('SELECT title, funder FROM grants LIMIT 5')
            for title, funder in cursor.fetchall():
                print(f"   - {title[:60]}... ({funder})")
        
        if nonprofit_count > 0:
            print("")
            print("Sample nonprofits:")
            cursor.execute('SELECT name, city FROM nonprofits LIMIT 5')
            for name, city in cursor.fetchall():
                city_str = city if city else "Unknown"
                print(f"   - {name[:60]}... ({city_str})")
        
        conn.close()
        
        # Status
        print("")
        print("="*60)
        if grant_count >= 10 and nonprofit_count >= 5:
            print("[SUCCESS] DATA COLLECTION COMPLETE!")
            print("   Ready to start backend and test matching!")
            print("")
            print("NEXT STEPS:")
            print("   1. Start backend: python main.py")
            print("   2. Open frontend/index.html")
            print("   3. Test grant matching!")
        elif grant_count > 0 or nonprofit_count > 0:
            print("[PARTIAL] Some data exists but need more")
            print("")
            print("NEXT STEPS:")
            print("   1. Go to /data folder")
            print("   2. Run: RUN_ALL.bat")
            print("   3. This will fetch 40+ more grants and nonprofits")
        else:
            print("[ERROR] NO DATA IN DATABASE")
            print("")
            print("NEXT STEPS:")
            print("   1. Go to /data folder")
            print("   2. Run: RUN_ALL.bat")
        print("="*60)
        
    except Exception as e:
        print("")
        print(f"[ERROR] Error reading database: {e}")

print("")
input("Press ENTER to close...")
