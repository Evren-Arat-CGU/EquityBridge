# EquityBridge Frontend Deployment
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  DEPLOYING FRONTEND FIX TO VERCEL" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

Set-Location "C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD"

Write-Host "[Step 1] Checking git status..." -ForegroundColor Yellow
git status
Write-Host ""

Write-Host "[Step 2] Adding fixed index.html..." -ForegroundColor Yellow
git add frontend/index.html
Write-Host ""

Write-Host "[Step 3] Checking what will be committed..." -ForegroundColor Yellow
git diff --cached --stat
Write-Host ""

Write-Host "[Step 4] Committing changes..." -ForegroundColor Yellow
git commit -m "Fix: Remove profile wrapper in API call and parse response correctly"
Write-Host ""

Write-Host "[Step 5] Pushing to GitHub (triggers Vercel auto-deploy)..." -ForegroundColor Yellow
git push
Write-Host ""

Write-Host "============================================" -ForegroundColor Green
Write-Host "  DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Vercel will rebuild in 30-60 seconds." -ForegroundColor White
Write-Host "Then test at: https://equity-bridge.vercel.app/" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
