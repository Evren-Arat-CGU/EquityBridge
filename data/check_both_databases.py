import sqlite3

# Check BOTH database locations
db1 = r'C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\backend\equitybridge.db'
db2 = r'C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\data\equitybridge.db'

print("="*60)
print("CHECKING BOTH DATABASE LOCATIONS")
print("="*60)

for i, db_path in enumerate([db1, db2], 1):
    print(f"\nDatabase {i}: {db_path}")
    print("-"*60)
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM grants')
        grants = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM nonprofits')
        nonprofits = cursor.fetchone()[0]
        
        print(f"Grants: {grants}")
        print(f"Nonprofits: {nonprofits}")
        
        if grants > 0:
            print("\nSample grants:")
            cursor.execute('SELECT title, funder FROM grants LIMIT 3')
            for title, funder in cursor.fetchall():
                print(f"  - {title[:50]}... ({funder})")
        
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

print("\n" + "="*60)
input("Press ENTER to close...")
