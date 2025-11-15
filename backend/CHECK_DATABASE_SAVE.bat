@echo off
echo ========================================
echo CHECKING DATABASE CONTENTS...
echo ========================================
echo.
echo Running check... results will be saved to database_status.txt
echo.

cd /d "%~dp0"

python check_database.py > database_status.txt 2>&1

echo.
echo ========================================
echo DONE! Opening results file...
echo ========================================
echo.

start database_status.txt

pause
