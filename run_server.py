#!/usr/bin/env python
"""
Start Django server with proper environment setup
"""
import os
import sys
import subprocess

def start_server():
    print("=" * 50)
    print("Django Tool Management System")
    print("=" * 50)
    print("Setting up local SQLite environment...")
    
    # Force environment variables
    os.environ['DATABASE_ENV'] = 'local'
    os.environ['DJANGO_SETTINGS_MODULE'] = 'toolprogram.settings'
    
    print("Environment: LOCAL SQLite")
    print("URL: http://127.0.0.1:8000")
    print("Landing Page: http://127.0.0.1:8000/tools/")
    print("Data: 50 tools, 15 employees, 10 work centers")
    print()
    print("Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        # Start Django development server
        subprocess.run([
            sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'
        ], env=os.environ, check=True)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure you're in the project directory")
        print("2. Activate virtual environment: .venv\\Scripts\\activate")
        print("3. Check if port 8000 is already in use")

if __name__ == '__main__':
    start_server()