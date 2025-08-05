#!/usr/bin/env python
"""
Simple browser test - opens all pages for manual testing
"""
import webbrowser
import time

def open_all_pages():
    print("Django Tool Management System - Browser Testing")
    print("=" * 50)
    print("Opening all pages for testing...")
    print("Server should be running at: http://127.0.0.1:8000")
    print()
    
    # List of all pages to test
    pages = [
        ("http://127.0.0.1:8000/", "Home Page"),
        ("http://127.0.0.1:8000/tools/", "Tools List"),
        ("http://127.0.0.1:8000/tools/1/", "Tool Detail (ID 1)"),
        ("http://127.0.0.1:8000/tools/create/", "Create Tool"),
        ("http://127.0.0.1:8000/employees/", "Employees List"),
        ("http://127.0.0.1:8000/employees/1/", "Employee Detail (ID 1)"),
        ("http://127.0.0.1:8000/employees/create/", "Create Employee"),
        ("http://127.0.0.1:8000/workcenters/", "Work Centers List"),
        ("http://127.0.0.1:8000/workcenters/1/", "Work Center Detail (ID 1)"),
        ("http://127.0.0.1:8000/workcenters/create/", "Create Work Center"),
        ("http://127.0.0.1:8000/admin/", "Admin Interface"),
        ("http://127.0.0.1:8000/api/tools/", "Tools API (JSON)"),
        ("http://127.0.0.1:8000/api/employees/", "Employees API (JSON)"),
        ("http://127.0.0.1:8000/api/workcenters/", "Work Centers API (JSON)"),
        ("http://127.0.0.1:8000/api/db-status/", "Database Status API"),
    ]
    
    print("TEST CHECKLIST - For each page, verify:")
    print("[ ] Page loads without errors")
    print("[ ] All content displays correctly")
    print("[ ] Links and buttons work")
    print("[ ] Forms can be submitted")
    print("[ ] CRUD operations work")
    print()
    
    # Open each page
    for i, (url, name) in enumerate(pages, 1):
        print(f"[{i:2d}/15] Opening: {name}")
        print(f"        URL: {url}")
        
        try:
            webbrowser.open(url)
            time.sleep(2)  # Brief pause between opens
            print("        Browser opened successfully")
        except Exception as e:
            print(f"        Error: {e}")
            print(f"        Please manually go to: {url}")
        
        print()
    
    print("All pages opened!")
    print()
    print("TESTING TASKS:")
    print("1. Create a new tool with all fields")
    print("2. Edit an existing tool")
    print("3. Delete a tool")
    print("4. Create a new employee")
    print("5. Create a new work center") 
    print("6. Assign a tool to a work center")
    print("7. Test API endpoints return JSON")
    print("8. Login to admin interface")
    print("9. Check for any error messages")
    print("10. Test responsive design")
    print()
    print("Your database has 50 tools, 15 employees, 10 work centers for testing!")

if __name__ == '__main__':
    open_all_pages()