"""
Smoke tests - quick tests to verify major functionality isn't broken
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter
import json


class CRUDSmokeTestCase(TestCase):
    """Test basic CRUD operations work"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        
        # Create user for authentication
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create initial data
        self.workcenter = WorkCenter.objects.create(
            name="Test WorkCenter",
            location="Test Location",
            supervisor="Test Supervisor",
            description="Test Description"
        )
    
    def test_tool_crud_smoke(self):
        """Smoke test for tool CRUD operations"""
        # CREATE
        tool_data = {
            'name': 'Smoke Test Tool',
            'description': 'Tool for smoke testing',
            'serial_number': 'ST001',
            'location': self.workcenter.id
        }
        
        response = self.client.post('/tools/create/', tool_data)
        self.assertIn(response.status_code, [200, 201, 302])
        
        # Verify tool was created
        tool = Tool.objects.filter(serial_number='ST001').first()
        self.assertIsNotNone(tool)
        
        # READ
        response = self.client.get(f'/tools/{tool.id}/')
        self.assertEqual(response.status_code, 200)
        
        # UPDATE
        update_data = {
            'name': 'Updated Smoke Test Tool',
            'description': 'Updated description',
            'serial_number': 'ST001',
            'location': self.workcenter.id
        }
        
        response = self.client.post(f'/tools/{tool.id}/edit/', update_data)
        self.assertIn(response.status_code, [200, 302])
        
        # DELETE
        response = self.client.post(f'/tools/{tool.id}/delete/')
        self.assertIn(response.status_code, [200, 302])
    
    def test_employee_crud_smoke(self):
        """Smoke test for employee CRUD operations"""
        # CREATE
        employee_data = {
            'name': 'Jane Smith',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'employee_id': 'ST002',
            'employee_number': 'EMP002',
            'department': 'Test Department',
            'email': 'jane.smith@example.com'
        }
        
        response = self.client.post('/employees/create/', employee_data)
        self.assertIn(response.status_code, [200, 201, 302])
        
        # Verify employee was created
        employee = Employee.objects.filter(employee_id='ST002').first()
        self.assertIsNotNone(employee)
        
        # READ
        response = self.client.get(f'/employees/{employee.id}/')
        self.assertEqual(response.status_code, 200)
        
        # UPDATE
        update_data = {
            'name': 'Janet Smith',
            'first_name': 'Janet',
            'last_name': 'Smith',
            'employee_id': 'ST002',
            'employee_number': 'EMP002',
            'department': 'Test Department',
            'email': 'janet.smith@example.com'
        }
        
        response = self.client.post(f'/employees/{employee.id}/edit/', update_data)
        self.assertIn(response.status_code, [200, 302])
        
        # DELETE
        response = self.client.post(f'/employees/{employee.id}/delete/')
        self.assertIn(response.status_code, [200, 302])
    
    def test_workcenter_crud_smoke(self):
        """Smoke test for workcenter CRUD operations"""
        # CREATE
        wc_data = {
            'name': 'Smoke Test WC',
            'location': 'Test Location',
            'supervisor': 'Test Supervisor',
            'description': 'WorkCenter for smoke testing'
        }
        
        response = self.client.post('/workcenters/create/', wc_data)
        self.assertIn(response.status_code, [200, 201, 302])
        
        # Verify workcenter was created
        wc = WorkCenter.objects.filter(name='Smoke Test WC').first()
        self.assertIsNotNone(wc)
        
        # READ
        response = self.client.get(f'/workcenters/{wc.id}/')
        self.assertEqual(response.status_code, 200)
        
        # UPDATE
        update_data = {
            'name': 'Updated Smoke Test WC',
            'location': 'Updated Location',
            'supervisor': 'Updated Supervisor',
            'description': 'Updated description'
        }
        
        response = self.client.post(f'/workcenters/{wc.id}/edit/', update_data)
        self.assertIn(response.status_code, [200, 302])
        
        # DELETE
        response = self.client.post(f'/workcenters/{wc.id}/delete/')
        self.assertIn(response.status_code, [200, 302])


class APISmokeTestCase(TestCase):
    """Smoke tests for API functionality"""
    
    def setUp(self):
        """Set up test data and authentication"""
        self.client = Client()
        
        # Create user and login
        self.user = User.objects.create_user(
            username='apiuser',
            password='apipass123'
        )
        self.client.login(username='apiuser', password='apipass123')
        
        # Create test data
        self.workcenter = WorkCenter.objects.create(
            name="API Test WorkCenter",
            location="API Location",
            supervisor="API Supervisor",
            description="WorkCenter for API testing"
        )
    
    def test_api_tools_smoke(self):
        """Smoke test for tools API"""
        # Test GET list
        response = self.client.get('/api/tools/')
        self.assertEqual(response.status_code, 200)
        
        # Test POST create
        tool_data = {
            'name': 'API Test Tool',
            'description': 'Tool created via API',
            'serial_number': 'API001',
            'location': self.workcenter.id
        }
        
        response = self.client.post(
            '/api/tools/',
            json.dumps(tool_data),
            content_type='application/json'
        )
        self.assertIn(response.status_code, [200, 201])
        
        # Get the created tool ID
        if response.status_code == 201:
            tool_id = response.json().get('id')
            
            # Test GET detail
            response = self.client.get(f'/api/tools/{tool_id}/')
            self.assertEqual(response.status_code, 200)
            
            # Test PUT update
            update_data = {
                'name': 'Updated API Test Tool',
                'description': 'Updated via API',
                'serial_number': 'API001',
                'location': self.workcenter.id
            }
            
            response = self.client.put(
                f'/api/tools/{tool_id}/',
                json.dumps(update_data),
                content_type='application/json'
            )
            self.assertIn(response.status_code, [200, 204])
            
            # Test DELETE
            response = self.client.delete(f'/api/tools/{tool_id}/')
            self.assertIn(response.status_code, [200, 204])
    
    def test_api_employees_smoke(self):
        """Smoke test for employees API"""
        # Test GET list
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, 200)
        
        # Test POST create
        employee_data = {
            'name': 'API User',
            'first_name': 'API',
            'last_name': 'User',
            'employee_id': 'API001',
            'employee_number': 'API001',
            'department': 'API Testing',
            'email': 'api.user@example.com'
        }
        
        response = self.client.post(
            '/api/employees/',
            json.dumps(employee_data),
            content_type='application/json'
        )
        self.assertIn(response.status_code, [200, 201])
    
    def test_api_workcenters_smoke(self):
        """Smoke test for workcenters API"""
        # Test GET list
        response = self.client.get('/api/workcenters/')
        self.assertEqual(response.status_code, 200)
        
        # Test POST create
        wc_data = {
            'name': 'API Test WC',
            'location': 'API Location',
            'supervisor': 'API Supervisor',
            'description': 'WorkCenter created via API'
        }
        
        response = self.client.post(
            '/api/workcenters/',
            json.dumps(wc_data),
            content_type='application/json'
        )
        self.assertIn(response.status_code, [200, 201])


class NavigationSmokeTestCase(TestCase):
    """Smoke tests for navigation and page rendering"""
    
    def setUp(self):
        """Set up test client and data"""
        self.client = Client()
        
        # Create test data
        self.workcenter = WorkCenter.objects.create(
            name="Nav Test WorkCenter",
            description="WorkCenter for navigation testing"
        )
        
        self.employee = Employee.objects.create(
            first_name="Nav",
            last_name="Test",
            employee_id="NAV001",
            email="nav.test@example.com"
        )
        
        self.tool = Tool.objects.create(
            name="Nav Test Tool",
            description="Tool for navigation testing",
            serial_number="NAV001",
            location=self.workcenter
        )
    
    def test_main_pages_render(self):
        """Test that main pages render without errors"""
        pages = [
            '/tools/',
            '/employees/',
            '/workcenters/',
            f'/tools/{self.tool.id}/',
            f'/employees/{self.employee.id}/',
            f'/workcenters/{self.workcenter.id}/',
        ]
        
        for page in pages:
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertEqual(response.status_code, 200)
    
    def test_form_pages_render(self):
        """Test that form pages render without errors"""
        form_pages = [
            '/tools/create/',
            '/employees/create/',
            '/workcenters/create/',
            f'/tools/{self.tool.id}/edit/',
            f'/employees/{self.employee.id}/edit/',
            f'/workcenters/{self.workcenter.id}/edit/',
        ]
        
        for page in form_pages:
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertEqual(response.status_code, 200)