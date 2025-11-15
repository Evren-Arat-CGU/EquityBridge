"""
EquityBridge Demo Verification System
Tests all components and provides clear status
"""

import sqlite3
import os
import sys
from pathlib import Path

def test_database():
    """Test database exists and has grants"""
    print("\n" + "="*70)
    print("STEP 1: DATABASE VERIFICATION")
    print("="*70)
    
    db_path = Path(__file__).parent / "backend" / "equitybridge.db"
    
    if not db_path.exists():
        print("[FAIL] Database not found at:", db_path)
        return False
    
    print(f"[OK] Database exists: {db_path}")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check grants table
        cursor.execute("SELECT COUNT(*) FROM grants")
        grant_count = cursor.fetchone()[0]
        
        print(f"[OK] Grants in database: {grant_count}")
        
        if grant_count == 0:
            print("[WARN] No grants found - database needs to be populated")
            conn.close()
            return False
        
        # Show sample grants
        cursor.execute("SELECT title, funder, focus_area FROM grants LIMIT 3")
        samples = cursor.fetchall()
        
        print("\nSample grants:")
        for i, (title, funder, focus) in enumerate(samples, 1):
            print(f"  {i}. {title[:50]}... ({funder}, {focus})")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"[FAIL] Database error: {e}")
        return False

def test_backend_files():
    """Test backend files exist"""
    print("\n" + "="*70)
    print("STEP 2: BACKEND FILES CHECK")
    print("="*70)
    
    backend_path = Path(__file__).parent / "backend"
    
    required_files = {
        "main.py": "FastAPI application",
        "database.py": "Database initialization",
        "equitybridge.db": "SQLite database"
    }
    
    all_good = True
    for filename, description in required_files.items():
        filepath = backend_path / filename
        if filepath.exists():
            print(f"[OK] {filename:20} - {description}")
        else:
            print(f"[FAIL] {filename:20} - MISSING")
            all_good = False
    
    return all_good

def test_frontend_files():
    """Test frontend files exist"""
    print("\n" + "="*70)
    print("STEP 3: FRONTEND FILES CHECK")
    print("="*70)
    
    frontend_path = Path(__file__).parent / "frontend"
    
    required_files = {
        "index.html": "Main HTML page",
        "app.js": "JavaScript logic",
        "styles.css": "Styling"
    }
    
    all_good = True
    for filename, description in required_files.items():
        filepath = frontend_path / filename
        if filepath.exists():
            print(f"[OK] {filename:20} - {description}")
        else:
            print(f"[FAIL] {filename:20} - MISSING")
            all_good = False
    
    return all_good

def print_instructions():
    """Print clear instructions for running demo"""
    print("\n" + "="*70)
    print("HOW TO RUN THE DEMO")
    print("="*70)
    
    print("\n1. START BACKEND:")
    print("   Open Command Prompt and run:")
    print("   cd backend")
    print("   uvicorn main:app --reload")
    print("   ")
    print("   You should see: 'Uvicorn running on http://127.0.0.1:8000'")
    
    print("\n2. OPEN FRONTEND:")
    print("   Navigate to: frontend/index.html")
    print("   Double-click to open in browser")
    
    print("\n3. TEST THE DEMO:")
    print("   Fill in the form:")
    print("   - Organization: 'Riverside Community Health'")
    print("   - Zip Code: '92501'")
    print("   - Focus: 'Community Health'")
    print("   - Budget: '250000'")
    print("   - Staff: '6-20 staff'")
    print("   - Mission: 'Providing health services to underserved communities'")
    print("   ")
    print("   Click 'Find Matching Grants'")
    print("   You should see ~5 matching grants with scores!")
    
    print("\n4. WHAT YOUR TEAM WILL SEE:")
    print("   ✓ Working form that accepts organization info")
    print("   ✓ Live grant matching with relevance scores")
    print("   ✓ Clear explanations of why each grant matches")
    print("   ✓ Accessible, professional interface")

def main():
    """Run all tests"""
    print("\n" + "="*70)
    print("EQUITYBRIDGE DEMO VERIFICATION")
    print("="*70)
    
    results = {
        "Database": test_database(),
        "Backend Files": test_backend_files(),
        "Frontend Files": test_frontend_files()
    }
    
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    all_passed = True
    for test_name, passed in results.items():
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status} {test_name}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n✅ ALL SYSTEMS GO! Demo is ready to run!")
        print_instructions()
    else:
        print("\n❌ ISSUES FOUND - Fix the failed checks above")
        print("\nQuick fix: Run SETUP_DATABASE.bat to populate database")
    
    print("\n" + "="*70)
    input("\nPress ENTER to close...")

if __name__ == "__main__":
    main()
