"""
Test the backend API endpoint
"""

import requests
import json

print("="*70)
print("TESTING BACKEND API")
print("="*70)
print()

# Test data
test_org = {
    "name": "Riverside Community Health Center",
    "location": "92501",
    "focus_area": "health",
    "budget": 250000
}

print("Testing /api/match-grants endpoint...")
print(f"Test organization: {test_org['name']}")
print(f"Focus: {test_org['focus_area']}")
print(f"Budget: ${test_org['budget']:,}")
print()

try:
    response = requests.post(
        "http://localhost:8000/api/match-grants",
        json=test_org,
        timeout=5
    )
    
    if response.status_code == 200:
        data = response.json()
        
        print("[SUCCESS] API responded!")
        print(f"\nMatches found: {data.get('matches_found', 0)}")
        print()
        
        grants = data.get('grants', [])
        for i, grant in enumerate(grants[:5], 1):
            print(f"{i}. {grant['title']}")
            print(f"   Funder: {grant['funder']}")
            print(f"   Amount: {grant['amount']}")
            print(f"   Match Score: {grant['match_score']}/100")
            print(f"   Reason: {grant['match_reason']}")
            print()
        
        print("="*70)
        print("[SUCCESS] BACKEND IS WORKING!")
        print("="*70)
        
    else:
        print(f"[ERROR] API returned status code: {response.status_code}")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("[ERROR] Cannot connect to backend!")
    print("\nIs the backend running?")
    print("Start it with: uvicorn main:app --reload")
    
except Exception as e:
    print(f"[ERROR] {e}")

print()
input("Press ENTER to close...")
