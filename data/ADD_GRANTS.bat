@echo off
echo ADDING GRANTS TO DATABASE...
echo.
cd /d "%~dp0"
python add_grants_now.py
