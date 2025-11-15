@echo off
echo ======================================================================
echo BACKEND STARTUP - DIAGNOSTIC MODE
echo ======================================================================
echo.

cd backend

echo Checking Python installation...
python --version
echo.

echo Checking if uvicorn is installed...
python -c "import uvicorn; print('uvicorn: OK')" 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: uvicorn is NOT installed!
    echo.
    echo Installing now...
    pip install fastapi uvicorn --break-system-packages
    echo.
)

echo Checking if fastapi is installed...
python -c "import fastapi; print('fastapi: OK')" 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: fastapi is NOT installed!
    echo.
    echo Installing now...
    pip install fastapi uvicorn --break-system-packages
    echo.
)

echo.
echo ======================================================================
echo STARTING BACKEND SERVER
echo ======================================================================
echo.

python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

echo.
echo ======================================================================
echo Backend stopped.
echo ======================================================================
pause
