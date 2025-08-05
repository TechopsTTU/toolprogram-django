#!/usr/bin/env python
"""
Production Test Runner

This script runs tests in production environment configuration.
It handles database connectivity issues gracefully and provides
comprehensive test reporting.
"""
import os
import sys
import subprocess
from pathlib import Path

def set_production_env():
    """Set environment variables for production testing"""
    os.environ['DATABASE_ENV'] = 'production'
    os.environ['DEBUG'] = 'False'
    
def test_database_connection():
    """Test if production database is accessible"""
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toolprogram.settings')
        import django
        django.setup()
        
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("SUCCESS: Production database connection successful")
        return True
    except Exception as e:
        print(f"FAILED: Production database connection failed: {e}")
        print("WARNING: Will run tests with SQLite fallback")
        return False

def run_tests(test_type="all"):
    """Run specified tests"""
    base_command = [sys.executable, 'manage.py', 'test', '--verbosity=2']
    
    test_commands = {
        'sanity': base_command + ['tests.test_sanity'],
        'smoke': base_command + ['tests.test_smoke'], 
        'models': base_command + ['tests.test_models_simple'],
        'functionality': base_command + ['tests.test_working_functionality'],
        'all': base_command
    }
    
    command = test_commands.get(test_type, test_commands['all'])
    
    print(f"\nRunning {test_type} tests...")
    print(f"Command: {' '.join(command)}")
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=300)
        
        print(f"\nTest Results for {test_type}:")
        print("=" * 50)
        print(result.stdout)
        
        if result.stderr:
            print("Warnings/Errors:")
            print(result.stderr)
            
        if result.returncode == 0:
            print(f"SUCCESS: {test_type.title()} tests PASSED")
        else:
            print(f"FAILED: {test_type.title()} tests FAILED")
            
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {test_type.title()} tests timed out after 5 minutes")
        return False
    except Exception as e:
        print(f"ERROR: Error running {test_type} tests: {e}")
        return False

def main():
    """Main test runner"""
    print("Production Environment Test Runner")
    print("=" * 50)
    
    # Set production environment
    set_production_env()
    print("Production environment configured")
    
    # Test database connection
    db_available = test_database_connection()
    
    if not db_available:
        print("WARNING: Falling back to local SQLite for testing")
        os.environ['DATABASE_ENV'] = 'local'
    
    # Run test suite in order of importance
    test_results = {}
    
    # 1. Sanity tests (most critical)
    test_results['sanity'] = run_tests('sanity')
    
    # 2. Smoke tests (quick validation)
    test_results['smoke'] = run_tests('smoke')
    
    # 3. Model tests (core functionality)
    test_results['models'] = run_tests('models')
    
    # 4. Full functionality tests
    test_results['functionality'] = run_tests('functionality')
    
    # Summary report
    print("\nFINAL TEST REPORT")
    print("=" * 50)
    
    total_tests = len(test_results)
    passed_tests = sum(1 for result in test_results.values() if result)
    
    for test_type, passed in test_results.items():
        status = "PASSED" if passed else "FAILED" 
        print(f"{test_type.ljust(15)}: {status}")
    
    print("-" * 50)
    print(f"OVERALL: {passed_tests}/{total_tests} test suites passed")
    
    if passed_tests == total_tests:
        print("SUCCESS: ALL TESTS PASSED - Production environment ready!")
        return 0
    else:
        print("WARNING: Some tests failed - Review issues before production deployment")
        return 1

if __name__ == '__main__':
    sys.exit(main())