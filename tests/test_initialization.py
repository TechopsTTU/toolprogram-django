"""
Initialization tests - verify system startup and configuration
"""
import os
import django
from django.test import TestCase, override_settings
from django.conf import settings
from django.core.management import call_command
from django.db import connection
from django.apps import apps


class InitializationTestCase(TestCase):
    """Test basic Django initialization and configuration"""
    
    def test_django_settings_loaded(self):
        """Test that Django settings are properly loaded"""
        self.assertTrue(hasattr(settings, 'DEBUG'))
        self.assertTrue(hasattr(settings, 'DATABASES'))
        self.assertTrue(hasattr(settings, 'INSTALLED_APPS'))
    
    def test_installed_apps_configuration(self):
        """Test that all required apps are installed and configured"""
        installed_apps = settings.INSTALLED_APPS
        required_apps = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'rest_framework',
            'tools',
            'employees',
            'workcenters',
        ]
        
        for app in required_apps:
            with self.subTest(app=app):
                self.assertIn(app, installed_apps)
    
    def test_database_connection(self):
        """Test database connection is working"""
        try:
            connection.ensure_connection()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Database connection failed: {e}")
    
    def test_apps_ready(self):
        """Test that all apps are properly loaded"""
        app_configs = apps.get_app_configs()
        app_names = [app.name for app in app_configs]
        
        required_apps = ['tools', 'employees', 'workcenters']
        for app in required_apps:
            with self.subTest(app=app):
                self.assertIn(app, app_names)
    
    def test_models_loaded(self):
        """Test that models are properly loaded"""
        from tools.models import Tool
        from employees.models import Employee
        from workcenters.models import WorkCenter
        
        # Test model classes are accessible
        self.assertTrue(hasattr(Tool, '_meta'))
        self.assertTrue(hasattr(Employee, '_meta'))
        self.assertTrue(hasattr(WorkCenter, '_meta'))
    
    def test_rest_framework_configuration(self):
        """Test REST framework is properly configured"""
        self.assertTrue(hasattr(settings, 'REST_FRAMEWORK'))
        rest_config = settings.REST_FRAMEWORK
        
        self.assertIn('DEFAULT_PERMISSION_CLASSES', rest_config)
        self.assertIn('DEFAULT_AUTHENTICATION_CLASSES', rest_config)
        self.assertIn('DEFAULT_PAGINATION_CLASS', rest_config)
    
    def test_static_files_configuration(self):
        """Test static files are configured"""
        self.assertTrue(hasattr(settings, 'STATIC_URL'))
        self.assertTrue(hasattr(settings, 'STATICFILES_DIRS'))
        self.assertTrue(hasattr(settings, 'STATIC_ROOT'))
    
    def test_templates_configuration(self):
        """Test templates are configured"""
        self.assertTrue(hasattr(settings, 'TEMPLATES'))
        templates = settings.TEMPLATES
        self.assertTrue(len(templates) > 0)
        
        template_config = templates[0]
        self.assertEqual(template_config['BACKEND'], 'django.template.backends.django.DjangoTemplates')
        self.assertTrue('DIRS' in template_config)


class MigrationTestCase(TestCase):
    """Test database migrations"""
    
    def test_migrations_applied(self):
        """Test that migrations can be applied without errors"""
        try:
            call_command('migrate', verbosity=0, interactive=False)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Migration failed: {e}")
    
    def test_check_for_missing_migrations(self):
        """Test that there are no missing migrations"""
        try:
            call_command('makemigrations', check=True, dry_run=True, verbosity=0)
            self.assertTrue(True)
        except SystemExit:
            self.fail("Missing migrations detected")