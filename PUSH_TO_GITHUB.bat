@echo off
echo ======================================================================
echo PUSHING TO GITHUB
echo ======================================================================
echo.
echo Repository: https://github.com/Evren-Arat-CGU/equitybridge
echo.
echo Make sure you've created the repository on GitHub first!
echo Go to: https://github.com/new
echo Name: equitybridge
echo.
pause

echo.
echo Pushing to GitHub...
git push -u origin main

if errorlevel 1 (
    echo.
    echo [ERROR] Push failed!
    echo.
    echo Possible reasons:
    echo 1. Repository doesn't exist on GitHub yet
    echo    - Create it at: https://github.com/new
    echo    - Name: equitybridge
    echo    - DO NOT initialize with README
    echo.
    echo 2. Authentication needed
    echo    - Use Personal Access Token as password
    echo    - Get token: https://github.com/settings/tokens
    echo.
) else (
    echo.
    echo [SUCCESS] Pushed to GitHub!
    echo Repository: https://github.com/Evren-Arat-CGU/equitybridge
)

pause

