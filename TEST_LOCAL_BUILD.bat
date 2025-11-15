@echo off
echo ======================================================================
echo TESTING LOCAL BUILD FOR DEPLOYMENT
echo ======================================================================
echo.

echo Testing Backend Build...
cd backend
python -c "import fastapi; import uvicorn; import pydantic; print('[OK] Backend dependencies')"
if errorlevel 1 (
    echo [ERROR] Backend dependencies missing!
    echo Run: pip install -r requirements.txt
    cd ..
    pause
    exit /b 1
)

python -c "import main; print('[OK] Backend imports successfully')"
if errorlevel 1 (
    echo [ERROR] Backend has import errors!
    cd ..
    pause
    exit /b 1
)

cd ..

echo.
echo Testing Frontend Files...
if not exist "frontend\index.html" (
    echo [ERROR] frontend\index.html missing!
    pause
    exit /b 1
)
echo [OK] Frontend HTML exists

if not exist "frontend\app.js" (
    echo [ERROR] frontend\app.js missing!
    pause
    exit /b 1
)
echo [OK] Frontend JavaScript exists

if not exist "frontend\styles.css" (
    echo [ERROR] frontend\styles.css missing!
    pause
    exit /b 1
)
echo [OK] Frontend CSS exists

echo.
echo Testing Database...
if not exist "backend\equitybridge.db" (
    echo [WARNING] Database not found. Run: python backend\database.py
) else (
    echo [OK] Database exists
)

echo.
echo ======================================================================
echo BUILD TEST COMPLETE - READY FOR DEPLOYMENT
echo ======================================================================
echo.
pause

