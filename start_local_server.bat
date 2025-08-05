@echo off
echo ========================================
echo Starting Django Tool Management System  
echo ========================================
echo Using LOCAL SQLite database
echo Server will run at: http://127.0.0.1:8000
echo Database has 50 tools, 15 employees, 10 work centers
echo.
echo The new beautiful landing page will be at:
echo http://127.0.0.1:8000/tools/
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Force local environment
set DATABASE_ENV=local
set DJANGO_SETTINGS_MODULE=toolprogram.settings

REM Start the server
python manage.py runserver 127.0.0.1:8000

pause