"""
Test endpoint to verify Mind Studio integration
Run this to test if Mind Studio can call the API
"""

import requests
import json

API_URL = "http://localhost:8000/api/match-grants"

# Sample request that Mind Studio will send
test_request = {
    "name": "Riverside Community Health Clinic",
    "zip_code": "92501",
    "county": "Riverside",
    "mission": "Providing primary care and maternal health services to low-income families",
    "focus_area": "health",
    "annual_budget": 250000,
    "staff_size": "6-20"
}

print("="*70)
print("TESTING MIND STUDIO API INTEGRATION")
print("="*70)
print("\nSending request to:", API_URL)
print("\nRequest body:")
print(json.dumps(test_request, indent=2))
print("\n" + "="*70)

try:
    response = requests.post(API_URL, json=test_request)
    
    print(f"\nStatus Code: {response.status_code}")
    
    if response.status_code == 200:
        print("\n✅ SUCCESS! API is working")
        print("\nResponse:")
        result = response.json()
        print(json.dumps(result, indent=2))
        
        print("\n" + "="*70)
        print("WHAT MIND STUDIO WILL RECEIVE:")
        print("="*70)
        
        if result.get('grants'):
            print(f"\nFound {result['matches_found']} grants for {result['organization']}")
            print("\nTop match:")
            top_grant = result['grants'][0]
            print(f"  Title: {top_grant['title']}")
            print(f"  Funder: {top_grant['funder']}")
            print(f"  Amount: {top_grant['amount']}")
            print(f"  Match Score: {top_grant['match_score']}%")
            print(f"  Why: {top_grant['match_reason']}")
    else:
        print(f"\n❌ ERROR: {response.status_code}")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("\n❌ ERROR: Cannot connect to backend")
    print("\nMake sure backend is running:")
    print("  cd backend")
    print("  uvicorn main:app --reload")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")

print("\n" + "="*70)
input("\nPress ENTER to close...")
