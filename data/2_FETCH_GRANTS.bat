@echo off
echo ========================================
echo EQUITYBRIDGE - GRANT DATA COLLECTION
echo ========================================
echo.
echo This will fetch grant data from:
echo - Grants.gov API (federal grants)
echo - California foundations
echo.
echo Estimated time: 1-2 minutes
echo.
pause

cd /d "%~dp0"

echo.
echo Fetching grant data...
python fetch_grants_working.py

echo.
echo ========================================
echo Grant data collection complete!
echo ========================================
echo.
pause
