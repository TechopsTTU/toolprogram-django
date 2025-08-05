#!/usr/bin/env python
"""
Test the new beautiful landing page
"""
import webbrowser
import time

def test_landing_page():
    print("Testing the New Beautiful Landing Page!")
    print("=" * 50)
    print("Opening the enhanced dashboard at http://127.0.0.1:8000/tools/")
    print()
    print("What you should see:")
    print("✅ Modern gradient header with navigation")
    print("✅ Hero section with manufacturing theme")
    print("✅ Statistics dashboard (50 tools, etc.)")
    print("✅ Beautiful navigation cards with gradients")
    print("✅ Tools Management card (blue gradient)")
    print("✅ Employee Management card (green gradient)")
    print("✅ Work Centers card (pink/yellow gradient)")
    print("✅ API & Data card (light gradient)")
    print("✅ Administration card (orange gradient)")
    print("✅ Reports & Analytics card (pink gradient)")
    print("✅ Recent tools list with status badges")
    print("✅ Responsive design that works on mobile")
    print()
    
    # Open the landing page
    url = "http://127.0.0.1:8000/tools/"
    try:
        webbrowser.open(url)
        print(f"🚀 Opening: {url}")
        print()
        print("TESTING CHECKLIST:")
        print("[ ] Page loads quickly without errors")
        print("[ ] Statistics show correct numbers")
        print("[ ] All navigation cards are clickable")
        print("[ ] Buttons work (Add New Tool, etc.)")
        print("[ ] Recent tools list shows populated data")
        print("[ ] Status badges show calibration status")
        print("[ ] Responsive design works (resize window)")
        print("[ ] All links navigate to correct pages")
        print("[ ] Gradients and animations work smoothly")
        print("[ ] Mobile view stacks cards properly")
        print()
        
        input("Press Enter when you've finished testing the landing page...")
        
        print("🎉 Landing page testing complete!")
        print("Your Django Tool Management System now has a beautiful,")
        print("professional dashboard that serves as the main navigation hub!")
        
    except Exception as e:
        print(f"❌ Error opening browser: {e}")
        print(f"Please manually navigate to: {url}")

if __name__ == '__main__':
    test_landing_page()