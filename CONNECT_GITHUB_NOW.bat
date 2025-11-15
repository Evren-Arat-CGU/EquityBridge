@echo off
echo ======================================================================
echo CONNECT PROJECT TO GITHUB
echo ======================================================================
echo.

echo Step 1: Checking git status...
git status >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Not a git repository!
    echo Run: git init
    pause
    exit /b 1
)

echo [OK] Git repository initialized
echo.

echo Step 2: Adding files...
git add .
echo [OK] Files staged
echo.

echo Step 3: Creating initial commit...
git commit -m "Initial commit: EquityBridge hackathon project

- Backend API with grant matching algorithm
- Frontend with accessible UI and tab switching
- Database with 21 grants
- Deployment configs (Railway/Vercel)
- Documentation and coordination docs
- Mind Studio integration ready"
echo [OK] Initial commit created
echo.

echo ======================================================================
echo NEXT STEPS:
echo ======================================================================
echo.
echo 1. Create repository on GitHub:
echo    - Go to: https://github.com/new
echo    - Name: equitybridge (or your choice)
echo    - DO NOT initialize with README
echo    - Click "Create repository"
echo.
echo 2. Connect to GitHub (replace YOUR_USERNAME):
echo    git remote add origin https://github.com/YOUR_USERNAME/equitybridge.git
echo.
echo 3. Push to GitHub:
echo    git branch -M main
echo    git push -u origin main
echo.
echo For detailed instructions, see: SETUP_GITHUB.md
echo.
pause

