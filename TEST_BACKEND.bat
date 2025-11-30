@echo off
echo ================================================
echo   TESTING EQUITYBRIDGE BACKEND
echo ================================================
echo.

cd C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD

echo Running backend tests...
echo.
python test_backend.py

echo.
echo ================================================
echo   TEST COMPLETE
echo ================================================
echo.
echo If you see green checkmarks, backend is working!
echo If you see red X marks, there's a problem.
echo.
pause
