@echo off
echo ======================================================================
echo UPDATE FRONTEND API URL FOR PRODUCTION
echo ======================================================================
echo.
echo Enter your Railway backend URL:
echo Example: https://equitybridge-production.railway.app
echo.
set /p RAILWAY_URL="Railway URL: "

echo.
echo Updating frontend/config.js...
echo.

powershell -Command "(Get-Content 'frontend\config.js') -replace 'http://localhost:8000', '%RAILWAY_URL%' | Set-Content 'frontend\config.js'"

echo [OK] Updated frontend/config.js with Railway URL
echo.
echo Next steps:
echo 1. Commit and push: git add frontend/config.js && git commit -m 'Update API URL' && git push
echo 2. Vercel will auto-redeploy
echo.
pause

