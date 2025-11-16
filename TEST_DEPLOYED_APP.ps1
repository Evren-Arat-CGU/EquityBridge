# Test Deployed EquityBridge Application
# Run this to verify everything is working

Write-Host "=== Testing EquityBridge Deployment ===" -ForegroundColor Cyan
Write-Host ""

# Test 1: Backend Health Check
Write-Host "1. Testing Backend Health..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "https://ideal-flow-production-2795.up.railway.app/" -Method Get
    Write-Host "   ✅ Backend is healthy: $($response.status)" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Backend health check failed: $_" -ForegroundColor Red
}

Write-Host ""

# Test 2: API Match Grants Endpoint
Write-Host "2. Testing /api/match-grants endpoint..." -ForegroundColor Yellow
$testData = @{
    organization_name = "Test Health Organization"
    zip_code = "90001"
    focus_area = "health"
    budget = 50000
    staff_size = 10
    county = "Los Angeles"
    mission = "Providing health services to underserved communities"
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "https://ideal-flow-production-2795.up.railway.app/api/match-grants" -Method Post -Body $testData -ContentType "application/json"
    Write-Host "   ✅ API returned $($response.matches.Count) grant matches" -ForegroundColor Green
    if ($response.matches.Count -gt 0) {
        Write-Host "   Top match: $($response.matches[0].title) (Score: $($response.matches[0].match_score)%)" -ForegroundColor Green
    }
} catch {
    Write-Host "   ❌ API test failed: $_" -ForegroundColor Red
}

Write-Host ""

# Test 3: Frontend URL
Write-Host "3. Frontend URL:" -ForegroundColor Yellow
Write-Host "   https://equity-bridge.vercel.app/" -ForegroundColor Cyan
Write-Host "   ⚠️  Please test manually in browser" -ForegroundColor Yellow

Write-Host ""
Write-Host "=== Test Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Visit https://equity-bridge.vercel.app/" -ForegroundColor White
Write-Host "2. Test the 'Chat with AI' tab (Mind Studio)" -ForegroundColor White
Write-Host "3. Test the 'Use Form Instead' tab" -ForegroundColor White
Write-Host "4. Verify map displays with results" -ForegroundColor White

