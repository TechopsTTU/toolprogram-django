#!/usr/bin/env python
"""
Start Django server with local SQLite database
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

# Force local environment
os.environ['DATABASE_ENV'] = 'local'
os.environ['DJANGO_SETTINGS_MODULE'] = 'toolprogram.settings'

def main():
    print("🔧 Starting Django Tool Management System")
    print("=" * 40)
    print("🗄️  Using LOCAL SQLite database")
    print("🌐 Server will run at: http://127.0.0.1:8000")
    print("📊 Database contains 50 tools, 10 work centers, 15 employees")
    print()
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 40)
    
    try:
        # Setup Django
        django.setup()
        
        # Start the server
        execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000'])
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you're in the correct directory")
        print("2. Activate the virtual environment: .venv\\Scripts\\activate")
        print("3. Check that DATABASE_ENV=local in your .env file")

if __name__ == '__main__':
    main()