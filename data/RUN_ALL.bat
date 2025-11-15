@echo off
echo ========================================
echo EQUITYBRIDGE - COMPLETE DATA SETUP
echo ========================================
echo.
echo This will run ALL data collection:
echo   1. Initialize database
echo   2. Fetch grants (federal + foundations)
echo   3. Fetch nonprofits (California orgs)
echo.
echo Estimated total time: 3-5 minutes
echo.
echo ========================================
pause

cd /d "%~dp0"

echo.
echo.
echo ========================================
echo STEP 1: Initialize Database
echo ========================================
python RUN_ALL_DATA_COLLECTION.py

echo.
echo.
echo ========================================
echo ALL DATA COLLECTION COMPLETE!
echo ========================================
echo.
echo Next steps:
echo   1. Start backend: cd backend ^&^& python main.py
echo   2. Open frontend/index.html in browser
echo   3. Test grant matching!
echo.
pause
