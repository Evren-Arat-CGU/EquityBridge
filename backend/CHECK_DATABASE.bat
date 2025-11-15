@echo off
echo ========================================
echo CHECKING DATABASE CONTENTS...
echo ========================================
echo.

cd /d "%~dp0"

python check_database.py

echo.
echo ========================================
pause
