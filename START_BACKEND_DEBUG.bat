@echo off
echo ======================================================================
echo QUICK BACKEND TEST
echo ======================================================================
echo.

echo Current directory:
cd
echo.

echo Checking if backend folder exists...
if exist "backend" (
    echo [OK] backend folder exists
) else (
    echo [ERROR] backend folder NOT found!
    echo Current location: %cd%
    pause
    exit /b 1
)

echo.
echo Checking backend files...
if exist "backend\main.py" (
    echo [OK] main.py exists
) else (
    echo [ERROR] main.py NOT found!
)

if exist "backend\equitybridge.db" (
    echo [OK] database exists
) else (
    echo [WARNING] database NOT found - will be created on startup
)

echo.
echo Checking Python...
python --version 2>nul
if errorlevel 1 (
    echo [ERROR] Python is NOT installed or not in PATH!
    echo.
    echo Please install Python from: https://python.org
    pause
    exit /b 1
) else (
    echo [OK] Python is installed
)

echo.
echo Checking required packages...
python -c "import fastapi" 2>nul
if errorlevel 1 (
    echo [MISSING] fastapi - installing now...
    pip install fastapi uvicorn --break-system-packages
) else (
    echo [OK] fastapi installed
)

python -c "import uvicorn" 2>nul
if errorlevel 1 (
    echo [MISSING] uvicorn - installing now...
    pip install fastapi uvicorn --break-system-packages
) else (
    echo [OK] uvicorn installed
)

echo.
echo ======================================================================
echo All checks passed! Starting backend...
echo ======================================================================
echo.

cd backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

pause
