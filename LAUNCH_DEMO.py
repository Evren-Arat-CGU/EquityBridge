"""
One-Click Demo Launcher
Starts backend and opens frontend automatically
"""

import subprocess
import time
import webbrowser
from pathlib import Path
import sys

def check_uvicorn():
    """Check if uvicorn is installed"""
    try:
        subprocess.run(["uvicorn", "--version"], capture_output=True, check=True)
        return True
    except:
        return False

def start_backend():
    """Start the backend server"""
    print("\n" + "="*70)
    print("STARTING BACKEND SERVER")
    print("="*70)
    
    if not check_uvicorn():
        print("[ERROR] uvicorn not installed!")
        print("Install it with: pip install uvicorn")
        return None
    
    backend_path = Path(__file__).parent / "backend"
    
    # Start uvicorn in a subprocess
    process = subprocess.Popen(
        ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
        cwd=str(backend_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    print("[OK] Backend starting... (waiting 3 seconds)")
    time.sleep(3)
    
    # Check if it's still running
    if process.poll() is None:
        print("[OK] Backend running at http://localhost:8000")
        return process
    else:
        print("[ERROR] Backend failed to start")
        return None

def open_frontend():
    """Open frontend in browser"""
    print("\n" + "="*70)
    print("OPENING FRONTEND")
    print("="*70)
    
    frontend_path = Path(__file__).parent / "frontend" / "index.html"
    
    if not frontend_path.exists():
        print(f"[ERROR] Frontend not found: {frontend_path}")
        return False
    
    print(f"[OK] Opening {frontend_path} in browser...")
    webbrowser.open(str(frontend_path.absolute()))
    time.sleep(1)
    print("[OK] Frontend opened!")
    return True

def main():
    print("\n" + "="*70)
    print("EQUITYBRIDGE - ONE-CLICK DEMO LAUNCHER")
    print("="*70)
    
    # Start backend
    backend_process = start_backend()
    
    if backend_process is None:
        print("\n[FAIL] Could not start backend")
        input("\nPress ENTER to exit...")
        sys.exit(1)
    
    # Open frontend
    if not open_frontend():
        print("\n[FAIL] Could not open frontend")
        backend_process.terminate()
        input("\nPress ENTER to exit...")
        sys.exit(1)
    
    print("\n" + "="*70)
    print("✅ DEMO IS RUNNING!")
    print("="*70)
    print("\nFrontend: Opened in your browser")
    print("Backend: Running at http://localhost:8000")
    print("\nTest the demo:")
    print("1. Fill in the organization form")
    print("2. Click 'Find Matching Grants'")
    print("3. See grant matches with scores!")
    print("\n" + "="*70)
    print("Press Ctrl+C to stop the backend and close this window")
    print("="*70)
    
    try:
        # Keep running until user stops it
        backend_process.wait()
    except KeyboardInterrupt:
        print("\n\nStopping backend...")
        backend_process.terminate()
        backend_process.wait()
        print("Backend stopped.")

if __name__ == "__main__":
    main()
