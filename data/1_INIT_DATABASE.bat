@echo off
echo ========================================
echo EQUITYBRIDGE - DATABASE INITIALIZATION
echo ========================================
echo.

cd /d "%~dp0..\backend"

echo Running database setup...
python database.py

echo.
echo ========================================
echo Database initialization complete!
echo ========================================
echo.
pause
