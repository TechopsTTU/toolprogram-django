"""
Test runner configuration and utilities
"""
import unittest
from django.test.runner import DiscoverRunner
from django.conf import settings


class CustomTestRunner(DiscoverRunner):
    """Custom test runner with additional configuration"""
    
    def setup_test_environment(self, **kwargs):
        """Set up test environment"""
        super().setup_test_environment(**kwargs)
        
        # Additional test setup can go here
        settings.DEBUG = False
        settings.PASSWORD_HASHERS = [
            'django.contrib.auth.hashers.MD5PasswordHasher',  # Faster for tests
        ]
    
    def teardown_test_environment(self, **kwargs):
        """Tear down test environment"""
        super().teardown_test_environment(**kwargs)


def run_initialization_tests():
    """Run only initialization tests"""
    from django.test.utils import get_runner
    from django.conf import settings
    
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests(['tests.test_initialization'])
    return failures


def run_sanity_tests():
    """Run only sanity tests"""
    from django.test.utils import get_runner
    from django.conf import settings
    
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests(['tests.test_sanity'])
    return failures


def run_smoke_tests():
    """Run only smoke tests"""
    from django.test.utils import get_runner
    from django.conf import settings
    
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests(['tests.test_smoke'])
    return failures


def run_end_to_end_tests():
    """Run only end-to-end tests"""
    from django.test.utils import get_runner
    from django.conf import settings
    
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests(['tests.test_end_to_end'])
    return failures


def run_all_tests():
    """Run all tests in order"""
    from django.test.utils import get_runner
    from django.conf import settings
    
    test_runner = get_runner(settings)()
    test_modules = [
        'tests.test_initialization',
        'tests.test_sanity', 
        'tests.test_smoke',
        'tests.test_end_to_end'
    ]
    
    failures = test_runner.run_tests(test_modules)
    return failures