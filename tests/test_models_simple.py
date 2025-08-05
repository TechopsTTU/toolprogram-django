"""
Simple comprehensive tests that work with actual model structure
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter


class SimpleModelTestCase(TestCase):
    """Test basic model functionality with actual fields"""
    
    def setUp(self):
        """Set up test data"""
        self.workcenter = WorkCenter.objects.create(
            name="Test WorkCenter",
            location="Test Location",
            supervisor="Test Supervisor"
        )
        
        self.employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            employee_number="E001"
        )
        
        self.tool = Tool.objects.create(
            name="Test Tool",
            serial_number="T001"
        )
    
    def test_models_creation(self):
        """Test all models can be created"""
        self.assertIsNotNone(self.tool.id)
        self.assertIsNotNone(self.employee.id)
        self.assertIsNotNone(self.workcenter.id)
        
        # Test field values
        self.assertEqual(self.tool.name, "Test Tool")
        self.assertEqual(self.employee.first_name, "John")
        self.assertEqual(self.workcenter.name, "Test WorkCenter")
    
    def test_string_representations(self):
        """Test model string representations"""
        self.assertIn("Test Tool", str(self.tool))
        self.assertIn("John", str(self.employee))
        self.assertIn("Test WorkCenter", str(self.workcenter))


class SimpleViewTestCase(TestCase):
    """Test basic view functionality"""
    
    def setUp(self):
        """Set up test client and data"""
        self.client = Client()
        
        self.workcenter = WorkCenter.objects.create(
            name="View Test WC",
            location="Test Location",
            supervisor="Test Supervisor"
        )
        
        self.employee = Employee.objects.create(
            first_name="Jane",
            last_name="Smith",
            employee_number="E002"
        )
        
        self.tool = Tool.objects.create(
            name="View Test Tool",
            serial_number="T002"
        )
    
    def test_list_views_accessible(self):
        """Test that list views are accessible"""
        views = ['/tools/', '/employees/', '/workcenters/']
        
        for view in views:
            with self.subTest(view=view):
                response = self.client.get(view)
                self.assertEqual(response.status_code, 200)
    
    def test_detail_views_accessible(self):
        """Test that detail views are accessible"""
        views = [
            f'/tools/{self.tool.id}/',
            f'/employees/{self.employee.id}/',
            f'/workcenters/{self.workcenter.id}/'
        ]
        
        for view in views:
            with self.subTest(view=view):
                response = self.client.get(view)
                self.assertEqual(response.status_code, 200)
    
    def test_root_redirect(self):
        """Test root URL shows landing page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class SimpleAPITestCase(TestCase):
    """Test basic API functionality"""
    
    def setUp(self):
        """Set up test client and authentication"""
        self.client = Client()
        
        # Create user and login
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        self.workcenter = WorkCenter.objects.create(
            name="API Test WC",
            location="API Location",
            supervisor="API Supervisor"
        )
        
        self.employee = Employee.objects.create(
            first_name="API",
            last_name="User",
            employee_number="API001"
        )
        
        self.tool = Tool.objects.create(
            name="API Test Tool",
            serial_number="API001"
        )
    
    def test_api_list_endpoints(self):
        """Test API list endpoints are accessible"""
        endpoints = ['/api/tools/', '/api/employees/', '/api/workcenters/']
        
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_api_detail_endpoints(self):
        """Test API detail endpoints are accessible"""
        endpoints = [
            f'/api/tools/{self.tool.id}/',
            f'/api/employees/{self.employee.id}/',
            f'/api/workcenters/{self.workcenter.id}/'
        ]
        
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response['Content-Type'], 'application/json')


class SimpleCRUDTestCase(TestCase):
    """Test basic CRUD operations"""
    
    def setUp(self):
        """Set up test client"""
        self.client = Client()
        
        self.workcenter = WorkCenter.objects.create(
            name="CRUD Test WC",
            location="CRUD Location", 
            supervisor="CRUD Supervisor"
        )
    
    def test_tool_crud_basic(self):
        """Test basic tool CRUD operations"""
        # CREATE - Check if create form loads
        response = self.client.get('/tools/create/')
        self.assertEqual(response.status_code, 200)
        
        # Create tool directly in database for testing
        tool = Tool.objects.create(
            name="CRUD Test Tool",
            serial_number="CRUD001"
        )
        
        # READ - Check detail view
        response = self.client.get(f'/tools/{tool.id}/')
        self.assertEqual(response.status_code, 200)
        
        # UPDATE - Check edit form loads
        response = self.client.get(f'/tools/{tool.id}/edit/')
        self.assertEqual(response.status_code, 200)
        
        # DELETE - Check delete confirmation loads
        response = self.client.get(f'/tools/{tool.id}/delete/')
        self.assertEqual(response.status_code, 200)
    
    def test_employee_crud_basic(self):
        """Test basic employee CRUD operations"""
        # CREATE
        response = self.client.get('/employees/create/')
        self.assertEqual(response.status_code, 200)
        
        # Create employee for testing
        employee = Employee.objects.create(
            first_name="CRUD",
            last_name="Test",
            employee_number="CRUD001"
        )
        
        # READ
        response = self.client.get(f'/employees/{employee.id}/')
        self.assertEqual(response.status_code, 200)
        
        # UPDATE
        response = self.client.get(f'/employees/{employee.id}/edit/')
        self.assertEqual(response.status_code, 200)
        
        # DELETE
        response = self.client.get(f'/employees/{employee.id}/delete/')
        self.assertEqual(response.status_code, 200)
    
    def test_workcenter_crud_basic(self):
        """Test basic workcenter CRUD operations"""
        # CREATE
        response = self.client.get('/workcenters/create/')
        self.assertEqual(response.status_code, 200)
        
        # READ
        response = self.client.get(f'/workcenters/{self.workcenter.id}/')
        self.assertEqual(response.status_code, 200)
        
        # UPDATE
        response = self.client.get(f'/workcenters/{self.workcenter.id}/edit/')
        self.assertEqual(response.status_code, 200)
        
        # DELETE
        response = self.client.get(f'/workcenters/{self.workcenter.id}/delete/')
        self.assertEqual(response.status_code, 200)