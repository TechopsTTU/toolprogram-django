from django.test import TestCase, Client
from django.urls import reverse
from django.db import connections
from django.db.utils import OperationalError
import json
from unittest.mock import patch

class DatabaseConnectionTest(TestCase):
    """
    Tests for database connection functionality
    """

    def setUp(self):
        self.client = Client()

    def test_database_connection_success(self):
        # Test successful database connection response
        response = self.client.get(reverse('tools:db_status'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'connected')

    @patch('django.db.backends.base.base.BaseDatabaseWrapper.cursor')
    def test_database_connection_failure(self, mock_cursor):
        # Simulate database connection failure
        mock_cursor.side_effect = OperationalError('Database connection failed')

        response = self.client.get(reverse('tools:db_status'))
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'error')
        self.assertIn('Database connection failed', data['message'])

    def test_database_connection_info(self):
        # Test that the correct database connection info is returned
        response = self.client.get(reverse('tools:db_status'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        # Check that response contains expected database info
        self.assertIn('database', data)
        self.assertIn('name', data)

        # Verify correct database info is returned
        db_settings = connections['default'].settings_dict
        self.assertEqual(data['database'], db_settings['ENGINE'])
        self.assertEqual(data['name'], db_settings['NAME'])
