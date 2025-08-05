#!/usr/bin/env python
"""
Test the new page structure
"""
import webbrowser
import time
import os

def test_pages():
    print("Testing New Page Structure")
    print("=" * 40)
    print("Landing Page: http://127.0.0.1:8000/")
    print("Tools Page: http://127.0.0.1:8000/tools/")
    print()
    
    # Set environment
    os.environ['DATABASE_ENV'] = 'local'
    
    print("Make sure Django server is running first!")
    print("Run: python run_server.py")
    print()
    
    ready = input("Is the server running? (y/n): ")
    if ready.lower() != 'y':
        print("Start the server first!")
        return
    
    print("Opening landing page...")
    webbrowser.open("http://127.0.0.1:8000/")
    time.sleep(2)
    
    print("Opening tools page...")
    webbrowser.open("http://127.0.0.1:8000/tools/")
    
    print()
    print("What you should see:")
    print("Landing Page (/):")
    print("  - Beautiful dashboard with navigation cards")
    print("  - Statistics showing 50 tools, 15 employees, 10 work centers")
    print("  - 6 navigation cards with gradients")
    print("  - System status section")
    print()
    print("Tools Page (/tools/):")
    print("  - Clean tool list with all 50 tools")
    print("  - Tool cards with details and status badges")
    print("  - Add New Tool button")
    print("  - View/Edit/Delete buttons for each tool")
    print()

if __name__ == '__main__':
    test_pages()