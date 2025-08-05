@echo off
echo Starting Django Tool Management System
echo ========================================
echo Using LOCAL SQLite database
echo Server will run at: http://127.0.0.1:8000
echo Database contains 50 tools, 10 work centers, 15 employees
echo.
echo Press Ctrl+C to stop the server
echo ========================================

set DATABASE_ENV=local
python manage.py runserver 127.0.0.1:8000