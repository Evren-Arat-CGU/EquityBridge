@echo off
echo ======================================================================
echo UPDATE API URL IN FRONTEND CONFIG
echo ======================================================================
echo.
echo This script updates the API URL in frontend/config.js
echo.
set /p RAILWAY_URL="Enter your Railway backend URL (e.g., https://equitybridge-xxx.railway.app): "

if "%RAILWAY_URL%"=="" (
    echo ERROR: URL cannot be empty
    pause
    exit /b 1
)

echo.
echo Updating frontend/config.js with URL: %RAILWAY_URL%
echo.

cd frontend

REM Create new config.js with the Railway URL
(
echo // Frontend Configuration
echo // API URL for production backend
echo window.API_URL = '%RAILWAY_URL%';
) > config.js

cd ..

echo.
echo [OK] config.js updated!
echo.
echo Next steps:
echo 1. Commit and push: git add frontend/config.js ^&^& git commit -m "Update API URL" ^&^& git push
echo 2. Vercel will auto-redeploy
echo.
pause

