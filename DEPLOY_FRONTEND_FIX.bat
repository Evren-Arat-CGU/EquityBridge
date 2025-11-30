@echo off
echo ================================================
echo   DEPLOY FRONTEND FIX TO VERCEL
echo ================================================
echo.

cd C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\frontend

echo [Step 1] Checking current status...
git status
echo.

echo [Step 2] Adding fixed index.html...
git add index.html
echo.

echo [Step 3] Committing changes...
git commit -m "Fix: Remove profile wrapper in API call, parse response correctly"
echo.

echo [Step 4] Pushing to GitHub (triggers Vercel deploy)...
git push
echo.

echo ================================================
echo   DEPLOYMENT INITIATED!
echo ================================================
echo.
echo Vercel will automatically rebuild from the git push.
echo This takes about 30-60 seconds.
echo.
echo When done, test at: https://equity-bridge.vercel.app/
echo.
pause
