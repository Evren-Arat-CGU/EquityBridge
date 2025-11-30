@echo off
echo ================================================
echo   DEPLOY FULL VERSION WITH MAP TO VERCEL
echo ================================================
echo.

cd C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD

echo [Step 1] Adding updated index.html with map...
git add frontend/index.html

echo.
echo [Step 2] Committing...
git commit -m "Deploy full version: Form first + AI Chat + ArcGIS map"

echo.
echo [Step 3] Pushing to trigger Vercel deploy...
git push

echo.
echo ================================================
echo   DEPLOYMENT COMPLETE!
echo ================================================
echo.
echo Wait 60 seconds for Vercel to rebuild.
echo Then test at: https://equity-bridge.vercel.app/
echo.
echo You should now see:
echo   - Form tab (opens first)
echo   - AI Chat tab
echo   - LA County map with grants
echo   - Green dots for your matches
echo.
pause
