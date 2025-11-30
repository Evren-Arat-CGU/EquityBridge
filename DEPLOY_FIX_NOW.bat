@echo off
echo ================================================
echo   DEPLOY FIXED FRONTEND TO VERCEL
echo ================================================
echo.

cd C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\frontend

echo Checking git status...
git status

echo.
echo Adding changes...
git add index.html

echo.
echo Committing fix...
git commit -m "Fix: Remove profile wrapper and parse response correctly"

echo.
echo Deploying to Vercel...
echo (Vercel auto-deploys from git, so just push)
git push

echo.
echo ================================================
echo   DONE! 
echo   Wait 30-60 seconds for Vercel to rebuild
echo   Then visit: https://equity-bridge.vercel.app/
echo ================================================
echo.
pause
