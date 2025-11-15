@echo off
echo ======================================================================
echo POST-DEPLOYMENT TEST SCRIPT
echo ======================================================================
echo.
echo This script helps you test your deployed backend and frontend.
echo.
echo You'll need:
echo   1. Backend URL (from Railway)
echo   2. Frontend URL (from Vercel)
echo.
pause

echo.
echo Enter your BACKEND URL (from Railway):
echo Example: https://equitybridge-production.railway.app
set /p BACKEND_URL="Backend URL: "

echo.
echo Enter your FRONTEND URL (from Vercel):
echo Example: https://equitybridge.vercel.app
set /p FRONTEND_URL="Frontend URL: "

echo.
echo ======================================================================
echo TESTING BACKEND
echo ======================================================================
echo.

echo [1/3] Testing health endpoint...
curl -s "%BACKEND_URL%/" > health_test.json
if %ERRORLEVEL% EQU 0 (
    echo [OK] Health endpoint responded
    type health_test.json
) else (
    echo [ERROR] Health endpoint failed
)

echo.
echo [2/3] Testing API endpoint...
curl -s -X POST "%BACKEND_URL%/api/match-grants" ^
  -H "Content-Type: application/json" ^
  -d "{\"name\":\"Test Org\",\"zip_code\":\"92501\",\"mission\":\"Health services\",\"focus_area\":\"health\",\"annual_budget\":250000,\"staff_size\":\"6-20 staff\"}" ^
  > api_test.json

if %ERRORLEVEL% EQU 0 (
    echo [OK] API endpoint responded
    echo Response saved to api_test.json
) else (
    echo [ERROR] API endpoint failed
)

echo.
echo [3/3] Opening frontend in browser...
start "" "%FRONTEND_URL%"

echo.
echo ======================================================================
echo TEST RESULTS
echo ======================================================================
echo.
echo Backend Health: Check health_test.json
echo Backend API: Check api_test.json
echo Frontend: Opened in browser
echo.
echo Next steps:
echo   1. Check frontend loads correctly
echo   2. Submit the form
echo   3. Verify grants return with match scores
echo   4. Check browser console for errors
echo.
pause

