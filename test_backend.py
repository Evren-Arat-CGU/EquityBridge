import requests
import json

print("=" * 60)
print("  EQUITYBRIDGE BACKEND TEST")
print("=" * 60)
print()

API_URL = "https://ideal-flow-production-2795.up.railway.app"

# Test 1: Health Check
print("[TEST 1] Health Check...")
try:
    response = requests.get(f"{API_URL}/")
    print(f"✅ Status: {response.status_code}")
    print(f"✅ Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"❌ Error: {e}")

print()
print("-" * 60)
print()

# Test 2: Grant Matching
print("[TEST 2] Grant Matching...")
test_data = {
    "name": "Test Community Clinic",
    "zip_code": "90001",
    "mission": "Providing healthcare to underserved communities",
    "focus_area": "health",
    "annual_budget": 250000,
    "staff_size": "6-20"
}

print(f"Sending test data:")
print(json.dumps(test_data, indent=2))
print()

try:
    response = requests.post(
        f"{API_URL}/api/match-grants",
        json=test_data,
        headers={"Content-Type": "application/json"}
    )
    print(f"✅ Status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Organization: {result['organization']}")
        print(f"✅ Matches Found: {result['matches_found']}")
        print()
        print("Top Grants:")
        for i, grant in enumerate(result['grants'][:3], 1):
            print(f"\n  {i}. {grant['title']}")
            print(f"     Funder: {grant['funder']}")
            print(f"     Amount: {grant['amount']}")
            print(f"     Match: {grant['match_score']}%")
            print(f"     Reason: {grant['match_reason']}")
    else:
        print(f"❌ Error Response: {response.text}")
        
except Exception as e:
    print(f"❌ Error: {e}")

print()
print("=" * 60)
print("  TESTS COMPLETE")
print("=" * 60)
