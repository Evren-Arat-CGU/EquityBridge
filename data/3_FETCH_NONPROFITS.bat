@echo off
echo ========================================
echo EQUITYBRIDGE - NONPROFIT DATA COLLECTION
echo ========================================
echo.
echo This will fetch nonprofit data from:
echo - ProPublica Nonprofit Explorer API
echo - Focus: California health and environmental orgs
echo.
echo Estimated time: 1-2 minutes
echo.
pause

cd /d "%~dp0"

echo.
echo Fetching nonprofit data...
python fetch_nonprofits_working.py

echo.
echo ========================================
echo Nonprofit data collection complete!
echo ========================================
echo.
pause
