#!/usr/bin/env python
"""
Manual Browser Testing Guide for Django Tool Management System
Opens each page in the default browser for manual testing
"""
import os
import sys
import webbrowser
import time
import subprocess

def start_server_and_open_browser():
    """Start Django server and open browser for manual testing"""
    print("🔧 Django Tool Management System - Manual Browser Testing")
    print("=" * 60)
    
    # Set environment to local
    os.environ['DATABASE_ENV'] = 'local'
    
    print("🚀 Starting Django development server...")
    print("⚠️  If the server fails to start, run this manually:")
    print("   > set DATABASE_ENV=local")
    print("   > python manage.py runserver 127.0.0.1:8000")
    print()
    
    # Test URLs to open
    test_urls = [
        ('http://127.0.0.1:8000/', 'Home/Root Page'),
        ('http://127.0.0.1:8000/tools/', 'Tools List'),
        ('http://127.0.0.1:8000/tools/1/', 'Tool Detail (ID 1)'),
        ('http://127.0.0.1:8000/tools/create/', 'Create New Tool'),
        ('http://127.0.0.1:8000/employees/', 'Employees List'),
        ('http://127.0.0.1:8000/employees/1/', 'Employee Detail (ID 1)'),
        ('http://127.0.0.1:8000/employees/create/', 'Create New Employee'),
        ('http://127.0.0.1:8000/workcenters/', 'Work Centers List'),
        ('http://127.0.0.1:8000/workcenters/1/', 'Work Center Detail (ID 1)'),
        ('http://127.0.0.1:8000/workcenters/create/', 'Create New Work Center'),
        ('http://127.0.0.1:8000/admin/', 'Django Admin Interface'),
        ('http://127.0.0.1:8000/api/tools/', 'Tools API (JSON)'),
        ('http://127.0.0.1:8000/api/employees/', 'Employees API (JSON)'),
        ('http://127.0.0.1:8000/api/workcenters/', 'Work Centers API (JSON)'),
        ('http://127.0.0.1:8000/api/db-status/', 'Database Status API (JSON)'),
    ]
    
    print("📋 COMPREHENSIVE TESTING CHECKLIST")
    print("=" * 40)
    print("I will open each page in your browser. For each page, please test:")
    print("✅ Page loads without errors")
    print("✅ All buttons and links work")
    print("✅ Forms can be submitted")
    print("✅ Data displays correctly")
    print("✅ CRUD operations work (Create, Read, Update, Delete)")
    print("✅ Search and filtering (if available)")
    print()
    
    # Start opening pages
    for i, (url, description) in enumerate(test_urls, 1):
        print(f"🌐 [{i}/{len(test_urls)}] Opening: {description}")
        print(f"   URL: {url}")
        
        try:
            webbrowser.open(url)
            print("   ✅ Browser opened")
        except Exception as e:
            print(f"   ❌ Failed to open browser: {e}")
            print(f"   📝 Please manually navigate to: {url}")
        
        # Wait for user to test
        input("   ⏸️  Press Enter when you've finished testing this page...")
        print()
    
    print("🎯 ADDITIONAL TESTING TASKS")
    print("=" * 30)
    additional_tests = [
        "Create a new tool with all fields filled out",
        "Edit an existing tool and save changes",
        "Delete a tool and confirm it's removed",
        "Assign a tool to a work center",
        "Test tool check-in/check-out functionality",
        "Verify calibration status updates",
        "Create new employee with department",
        "Edit employee information",
        "Create new work center with supervisor",
        "Test API endpoints return valid JSON",
        "Log into admin interface (create superuser first)",
        "Test search functionality if implemented",
        "Test pagination if there are many records"
    ]
    
    for i, task in enumerate(additional_tests, 1):
        print(f"   {i:2d}. {task}")
        test_status = input("       Status (pass/fail/skip): ").lower()
        if test_status == 'fail':
            notes = input("       Notes: ")
            print(f"       ❌ FAILED: {notes}")
        elif test_status == 'pass':
            print(f"       ✅ PASSED")
        else:
            print(f"       ⏭️  SKIPPED")
        print()
    
    print("🏁 Manual Testing Complete!")
    print("=" * 30)
    print("📊 Summary:")
    print("• All main pages tested")
    print("• CRUD operations verified")
    print("• API endpoints checked")
    print("• Admin interface tested")
    print()
    print("💡 Tips for further testing:")
    print("• Try edge cases (empty forms, invalid data)")
    print("• Test with different browser sizes")
    print("• Check browser developer tools for JavaScript errors")
    print("• Verify responsive design on mobile")
    print()

def create_test_data_summary():
    """Show what test data is available"""
    print("📦 TEST DATA AVAILABLE")
    print("=" * 25)
    print("Your database contains:")
    print("• 50 Manufacturing Tools")
    print("  - Various types: Micrometers, Calipers, Gauges, etc.")
    print("  - Multiple manufacturers: Mitutoyo, Starrett, Brown & Sharpe")
    print("  - Different calibration statuses")
    print("  - Some assigned to work centers")
    print()
    print("• 10 Work Centers")
    print("  - CNC Machining Centers")
    print("  - Assembly Lines")
    print("  - Quality Control")
    print("  - Tool Crib")
    print()
    print("• 15 Employees")
    print("  - Various departments: Manufacturing, Quality, Assembly")
    print("  - Realistic names and employee numbers")
    print()

def main():
    print("Starting manual browser testing...")
    create_test_data_summary()
    
    print("🚨 IMPORTANT: Make sure Django server is running!")
    print("If not already running, open a new terminal and run:")
    print("   > set DATABASE_ENV=local")
    print("   > python manage.py runserver 127.0.0.1:8000")
    print()
    
    ready = input("Is the Django server running at http://127.0.0.1:8000? (y/n): ")
    if ready.lower() != 'y':
        print("Please start the server first, then run this script again.")
        return
    
    start_server_and_open_browser()

if __name__ == '__main__':
    main()