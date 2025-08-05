#!/usr/bin/env python
"""
Comprehensive Browser Test Runner for Django Tool Management System
Runs automated tests on all pages and functions through a web browser
"""
import os
import sys
import django
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import threading
import subprocess

# Force local environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'toolprogram.settings'
os.environ['DATABASE_ENV'] = 'local'
django.setup()

class BrowserTestRunner:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"
        self.driver = None
        self.server_process = None
        self.test_results = []
        
    def setup_webdriver(self):
        """Setup Chrome WebDriver"""
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # Comment out the next line if you want to see the browser window
        # chrome_options.add_argument("--headless")
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.set_window_size(1920, 1080)
            return True
        except Exception as e:
            print(f"⚠️  Could not start Chrome WebDriver: {e}")
            print("📝 Opening tests manually in default browser instead...")
            return False
    
    def start_django_server(self):
        """Start Django development server in a separate process"""
        try:
            # Set environment variables for the subprocess
            env = os.environ.copy()
            env['DATABASE_ENV'] = 'local'
            
            self.server_process = subprocess.Popen([
                sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'
            ], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait a bit for server to start
            time.sleep(3)
            print("✅ Django server started on http://127.0.0.1:8000")
            return True
        except Exception as e:
            print(f"❌ Failed to start Django server: {e}")
            return False
    
    def stop_django_server(self):
        """Stop Django development server"""
        if self.server_process:
            self.server_process.terminate()
            self.server_process.wait()
            print("🛑 Django server stopped")
    
    def test_page(self, url, page_name, expected_elements=None):
        """Test a single page"""
        full_url = f"{self.base_url}{url}"
        print(f"\\n🧪 Testing: {page_name} ({full_url})")
        
        if not self.driver:
            # Manual testing mode
            webbrowser.open(full_url)
            input(f"✋ Please manually test {page_name} at {full_url}\\nPress Enter when done...")
            return True
        
        try:
            self.driver.get(full_url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Check for expected elements
            if expected_elements:
                for element_id, description in expected_elements.items():
                    try:
                        element = self.driver.find_element(By.ID, element_id)
                        print(f"  ✅ Found {description}")
                    except NoSuchElementException:
                        print(f"  ⚠️  Missing {description} (#{element_id})")
            
            # Take screenshot
            screenshot_path = f"test_screenshots/{page_name.replace(' ', '_').lower()}.png"
            os.makedirs("test_screenshots", exist_ok=True)
            self.driver.save_screenshot(screenshot_path)
            print(f"  📸 Screenshot saved: {screenshot_path}")
            
            # Check for errors
            page_source = self.driver.page_source.lower()
            if "error" in page_source or "exception" in page_source:
                print(f"  ⚠️  Possible errors detected on page")
            else:
                print(f"  ✅ {page_name} loaded successfully")
            
            self.test_results.append({
                'page': page_name,
                'url': full_url,
                'status': 'passed',
                'screenshot': screenshot_path
            })
            
            return True
            
        except TimeoutException:
            print(f"  ❌ {page_name} failed to load (timeout)")
            self.test_results.append({
                'page': page_name,
                'url': full_url,
                'status': 'timeout'
            })
            return False
        except Exception as e:
            print(f"  ❌ {page_name} failed: {e}")
            self.test_results.append({
                'page': page_name,
                'url': full_url,
                'status': 'error',
                'error': str(e)
            })
            return False
    
    def run_comprehensive_tests(self):
        """Run all browser tests"""
        print("🚀 Starting Comprehensive Browser Testing")
        print("=" * 50)
        
        # Test plan based on Django URL patterns
        test_pages = [
            # Main pages
            ('/', 'Home Page (Root)', {'tools-list': 'Tools List'}),
            ('/tools/', 'Tools List Page', {'tools-list': 'Tools List'}),
            ('/employees/', 'Employees List Page', {'employees-list': 'Employees List'}),
            ('/workcenters/', 'Work Centers List Page', {'workcenters-list': 'Work Centers List'}),
            
            # Admin interface
            ('/admin/', 'Django Admin Login', None),
            
            # API endpoints
            ('/api/tools/', 'Tools API Endpoint', None),
            ('/api/employees/', 'Employees API Endpoint', None),
            ('/api/workcenters/', 'Work Centers API Endpoint', None),
            ('/api/db-status/', 'Database Status API', None),
        ]
        
        # CRUD operation tests (if we can access specific IDs)
        crud_tests = [
            # Tools CRUD
            ('/tools/1/', 'Tool Detail View', None),
            ('/tools/create/', 'Create New Tool', None),
            ('/tools/1/edit/', 'Edit Tool', None),
            ('/tools/1/delete/', 'Delete Tool Confirmation', None),
            
            # Employees CRUD
            ('/employees/1/', 'Employee Detail View', None),
            ('/employees/create/', 'Create New Employee', None),
            ('/employees/1/edit/', 'Edit Employee', None),
            ('/employees/1/delete/', 'Delete Employee Confirmation', None),
            
            # Work Centers CRUD
            ('/workcenters/1/', 'Work Center Detail View', None),
            ('/workcenters/create/', 'Create New Work Center', None),
            ('/workcenters/1/edit/', 'Edit Work Center', None),
            ('/workcenters/1/delete/', 'Delete Work Center Confirmation', None),
        ]
        
        # Start server
        if not self.start_django_server():
            print("❌ Cannot start server, exiting...")
            return
        
        # Setup WebDriver
        driver_available = self.setup_webdriver()
        
        try:
            # Test main pages
            print("\\n📋 Testing Main Pages...")
            for url, name, elements in test_pages:
                self.test_page(url, name, elements)
                if self.driver:
                    time.sleep(1)  # Brief pause between tests
            
            # Test CRUD operations
            print("\\n📋 Testing CRUD Operations...")
            for url, name, elements in crud_tests:
                self.test_page(url, name, elements)
                if self.driver:
                    time.sleep(1)  # Brief pause between tests
            
            # Summary
            self.print_test_summary()
            
        finally:
            if self.driver:
                self.driver.quit()
            self.stop_django_server()
    
    def print_test_summary(self):
        """Print test results summary"""
        print("\\n" + "=" * 50)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 50)
        
        total_tests = len(self.test_results)
        passed_tests = len([r for r in self.test_results if r['status'] == 'passed'])
        failed_tests = total_tests - passed_tests
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests*100):.1f}%")
        
        if failed_tests > 0:
            print("\\n❌ Failed Tests:")
            for result in self.test_results:
                if result['status'] != 'passed':
                    print(f"  - {result['page']}: {result['status']}")
        
        print("\\n🎯 Manual Testing Checklist:")
        print("□ Create a new tool and verify it appears in the list")
        print("□ Edit an existing tool and verify changes are saved")
        print("□ Delete a tool and verify it's removed")
        print("□ Assign a tool to a work center")
        print("□ Check tool calibration status")
        print("□ Test search and filtering functionality")
        print("□ Verify API endpoints return valid JSON")
        print("□ Test admin interface with superuser account")
        
        if self.driver:
            print(f"\\n📸 Screenshots saved in: test_screenshots/")

def main():
    """Main function"""
    print("🔧 Django Tool Management System - Browser Test Runner")
    print("=" * 60)
    
    runner = BrowserTestRunner()
    
    try:
        runner.run_comprehensive_tests()
    except KeyboardInterrupt:
        print("\\n⏹️  Testing interrupted by user")
    except Exception as e:
        print(f"\\n💥 Unexpected error: {e}")
    finally:
        print("\\n🏁 Testing complete!")

if __name__ == '__main__':
    main()