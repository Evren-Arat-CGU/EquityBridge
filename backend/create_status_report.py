"""Quick check of database contents - saves results to file"""
import sqlite3
import os

db_path = 'equitybridge.db'
output_file = 'DATABASE_STATUS_REPORT.txt'

# Open output file
with open(output_file, 'w') as f:
    
    def write(text):
        print(text)
        f.write(text + '\n')
    
    write("="*60)
    write("EQUITYBRIDGE DATABASE STATUS REPORT")
    write("="*60)
    write("")
    
    if not os.path.exists(db_path):
        write("❌ Database file NOT found!")
        write(f"   Looking for: {os.path.abspath(db_path)}")
    else:
        write("✅ Database file exists!")
        write(f"   Location: {os.path.abspath(db_path)}")
        write(f"   Size: {os.path.getsize(db_path)} bytes")
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check grants
            cursor.execute('SELECT COUNT(*) FROM grants')
            grant_count = cursor.fetchone()[0]
            
            # Check nonprofits
            cursor.execute('SELECT COUNT(*) FROM nonprofits')
            nonprofit_count = cursor.fetchone()[0]
            
            write("")
            write("📊 DATABASE CONTENTS:")
            write(f"   Grants: {grant_count}")
            write(f"   Nonprofits: {nonprofit_count}")
            
            if grant_count > 0:
                write("")
                write("📋 Sample grants:")
                cursor.execute('SELECT title, funder FROM grants LIMIT 5')
                for title, funder in cursor.fetchall():
                    write(f"   - {title[:60]}... ({funder})")
            
            if nonprofit_count > 0:
                write("")
                write("🏥 Sample nonprofits:")
                cursor.execute('SELECT name, city FROM nonprofits LIMIT 5')
                for name, city in cursor.fetchall():
                    city_str = city if city else "Unknown"
                    write(f"   - {name[:60]}... ({city_str})")
            
            conn.close()
            
            # Status
            write("")
            write("="*60)
            if grant_count >= 10 and nonprofit_count >= 5:
                write("✅ DATA COLLECTION SUCCESSFUL!")
                write("   Ready to start backend and test matching!")
                write("")
                write("NEXT STEPS:")
                write("   1. Start backend: python main.py")
                write("   2. Open frontend/index.html")
                write("   3. Test grant matching!")
            elif grant_count > 0 or nonprofit_count > 0:
                write("⚠️  PARTIAL DATA COLLECTION")
                write("   Some data exists but need more")
                write("")
                write("NEXT STEPS:")
                write("   1. Run: RUN_ALL.bat in /data folder")
                write("   2. This will fetch 40+ more grants and nonprofits")
            else:
                write("❌ NO DATA IN DATABASE")
                write("   Need to run data collection scripts")
                write("")
                write("NEXT STEPS:")
                write("   1. Go to /data folder")
                write("   2. Run: RUN_ALL.bat")
            write("="*60)
            
        except Exception as e:
            write("")
            write(f"❌ Error reading database: {e}")

print(f"\n✅ Report saved to: {os.path.abspath(output_file)}")
print("Opening report file...")

# Open the report file
import subprocess
subprocess.Popen(['notepad.exe', output_file])
