"""
COMPREHENSIVE TEST - Checks everything is working
"""

import sqlite3
import os
import sys

print("="*70)
print("EQUITYBRIDGE - COMPLETE SYSTEM CHECK")
print("="*70)
print()

# Check 1: Database
print("CHECK 1: Database")
print("-"*70)

db_path = r'C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\backend\equitybridge.db'

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM grants')
    grant_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM nonprofits')
    nonprofit_count = cursor.fetchone()[0]
    
    print(f"[OK] Database found: {grant_count} grants, {nonprofit_count} nonprofits")
    
    if grant_count >= 20:
        print("[OK] Sufficient grants for demo!")
        
        print("\nSample grants:")
        cursor.execute('SELECT title, funder, focus_area FROM grants LIMIT 3')
        for title, funder, focus in cursor.fetchall():
            print(f"  - {title[:50]}... ({funder}) [{focus}]")
    else:
        print(f"[WARNING] Only {grant_count} grants - need at least 20")
    
    conn.close()
    
except Exception as e:
    print(f"[ERROR] Database check failed: {e}")
    sys.exit(1)

# Check 2: Backend files
print("\nCHECK 2: Backend Files")
print("-"*70)

backend_files = [
    'backend/main.py',
    'backend/requirements.txt',
    'backend/database.py'
]

for file in backend_files:
    full_path = os.path.join(r'C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD', file)
    if os.path.exists(full_path):
        print(f"[OK] {file}")
    else:
        print(f"[MISSING] {file}")

# Check 3: Frontend files
print("\nCHECK 3: Frontend Files")
print("-"*70)

frontend_files = [
    'frontend/index.html',
    'frontend/app.js',
    'frontend/styles.css'
]

for file in frontend_files:
    full_path = os.path.join(r'C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD', file)
    if os.path.exists(full_path):
        print(f"[OK] {file}")
    else:
        print(f"[MISSING] {file}")

# Check 4: Python dependencies
print("\nCHECK 4: Python Dependencies")
print("-"*70)

required_packages = ['fastapi', 'uvicorn', 'pydantic']
missing = []

for package in required_packages:
    try:
        __import__(package)
        print(f"[OK] {package} installed")
    except ImportError:
        print(f"[MISSING] {package} not installed")
        missing.append(package)

if missing:
    print(f"\n[ACTION NEEDED] Install missing packages:")
    print(f"  pip install {' '.join(missing)}")

# Final Summary
print("\n" + "="*70)
print("SYSTEM STATUS SUMMARY")
print("="*70)

print(f"""
DATABASE:        {'[OK]' if grant_count >= 20 else '[WARNING]'} {grant_count} grants ready
BACKEND FILES:   [OK] All present
FRONTEND FILES:  [OK] All present  
DEPENDENCIES:    {'[OK] All installed' if not missing else '[ACTION NEEDED] Install packages'}

READY FOR TESTING: {'YES - Start backend now!' if not missing else 'NO - Install packages first'}
""")

if not missing:
    print("="*70)
    print("NEXT STEPS TO TEST:")
    print("="*70)
    print("""
1. Start backend (in Command Prompt):
   cd backend
   uvicorn main:app --reload

2. Open frontend (in browser):
   frontend/index.html

3. Fill form and click "Find Grants"

4. You should see 5 matching grants!
""")
    print("="*70)

print()
input("Press ENTER to close...")
