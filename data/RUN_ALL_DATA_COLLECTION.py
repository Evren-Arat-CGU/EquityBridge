"""
MASTER DATA COLLECTION SCRIPT
Runs all data collection in the right order:
1. Initialize database
2. Fetch grants
3. Fetch nonprofits
"""

import subprocess
import sys
import os

def run_script(script_path, description):
    """Run a Python script and handle errors"""
    
    print("\n" + "=" * 60)
    print(f"🚀 {description}")
    print("=" * 60 + "\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=120  # 2 minute timeout per script
        )
        
        print(result.stdout)
        
        if result.returncode != 0:
            print(f"⚠️  Warning: Script had errors")
            print(result.stderr)
            return False
        
        return True
        
    except subprocess.TimeoutExpired:
        print(f"❌ Script timed out after 2 minutes")
        return False
    except Exception as e:
        print(f"❌ Error running script: {e}")
        return False

def main():
    """Run all data collection scripts"""
    
    print("=" * 60)
    print("🎯 EQUITYBRIDGE - MASTER DATA COLLECTION")
    print("=" * 60)
    print("\nThis will:")
    print("  1. Initialize the database")
    print("  2. Fetch grant data (federal + foundations)")
    print("  3. Fetch nonprofit data (California)")
    print("\nEstimated time: 2-3 minutes")
    print("\n" + "=" * 60)
    
    input("\n👉 Press ENTER to start data collection...")
    
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(os.path.dirname(script_dir), 'backend')
    
    # Script paths
    database_script = os.path.join(backend_dir, 'database.py')
    grants_script = os.path.join(script_dir, 'fetch_grants_working.py')
    nonprofits_script = os.path.join(script_dir, 'fetch_nonprofits_working.py')
    
    results = []
    
    # Step 1: Initialize database
    success = run_script(database_script, "STEP 1: Initialize Database")
    results.append(("Database initialization", success))
    
    if not success:
        print("\n⚠️  Database initialization failed, but continuing...")
    
    # Step 2: Fetch grants
    success = run_script(grants_script, "STEP 2: Fetch Grant Data")
    results.append(("Grant data collection", success))
    
    # Step 3: Fetch nonprofits
    success = run_script(nonprofits_script, "STEP 3: Fetch Nonprofit Data")
    results.append(("Nonprofit data collection", success))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 DATA COLLECTION SUMMARY")
    print("=" * 60)
    
    for task, success in results:
        status = "✅ SUCCESS" if success else "⚠️  PARTIAL"
        print(f"{status}: {task}")
    
    print("\n" + "=" * 60)
    print("🎉 DATA COLLECTION COMPLETE!")
    print("=" * 60)
    print("\n💡 Next steps:")
    print("   1. Start backend: cd backend && python main.py")
    print("   2. Open frontend: frontend/index.html")
    print("   3. Test grant matching!")
    print("\n")

if __name__ == "__main__":
    main()
