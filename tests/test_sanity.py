"""
Sanity tests - verify basic functionality works as expected
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter


class ModelSanityTestCase(TestCase):
    """Test basic model functionality"""
    
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
    
    def test_tool_creation(self):
        """Test tool can be created and retrieved"""
        self.assertEqual(self.tool.name, "Test Tool")
        self.assertEqual(self.tool.serial_number, "T001")
        
        # Test string representation
        self.assertIn("Test Tool", str(self.tool))
    
    def test_employee_creation(self):
        """Test employee can be created and retrieved"""
        self.assertEqual(self.employee.first_name, "John")
        self.assertEqual(self.employee.last_name, "Doe")
        self.assertEqual(self.employee.employee_number, "E001")
        
        # Test string representation
        self.assertIn("John", str(self.employee))
        self.assertIn("Doe", str(self.employee))
    
    def test_workcenter_creation(self):
        """Test workcenter can be created and retrieved"""
        self.assertEqual(self.workcenter.name, "Test WorkCenter")
        self.assertEqual(self.workcenter.location, "Test Location")
        
        # Test string representation
        self.assertIn("Test WorkCenter", str(self.workcenter))
    
    def test_model_relationships(self):
        """Test basic model functionality"""
        # Test models have required fields
        self.assertTrue(hasattr(self.tool, 'name'))
        self.assertTrue(hasattr(self.workcenter, 'name'))
        self.assertTrue(hasattr(self.employee, 'first_name'))
        
        # Test models can be saved and retrieved
        self.assertIsNotNone(self.tool.id)
        self.assertIsNotNone(self.workcenter.id)
        self.assertIsNotNone(self.employee.id)


class URLSanityTestCase(TestCase):
    """Test URL routing works correctly"""
    
    def setUp(self):
        """Set up test client"""
        self.client = Client()
        
        # Create test data
        self.workcenter = WorkCenter.objects.create(
            name="Test WorkCenter",
            description="Test Description"
        )
        
        self.employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            employee_id="E001",
            employee_number="E001", 
            email="john.doe@example.com"
        )
        
        self.tool = Tool.objects.create(
            name="Test Tool",
            description="Test Description",
            serial_number="T001",
            location=self.workcenter
        )
    
    def test_root_url_landing_page(self):
        """Test root URL shows landing page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tool Management System')
    
    def test_tools_list_url(self):
        """Test tools list URL is accessible"""
        response = self.client.get('/tools/')
        self.assertEqual(response.status_code, 200)
    
    def test_tools_detail_url(self):
        """Test tool detail URL is accessible"""
        response = self.client.get(f'/tools/{self.tool.id}/')
        self.assertEqual(response.status_code, 200)
    
    def test_employees_list_url(self):
        """Test employees list URL is accessible"""
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, 200)
    
    def test_employees_detail_url(self):
        """Test employee detail URL is accessible"""
        response = self.client.get(f'/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, 200)
    
    def test_workcenters_list_url(self):
        """Test workcenters list URL is accessible"""
        response = self.client.get('/workcenters/')
        self.assertEqual(response.status_code, 200)
    
    def test_workcenters_detail_url(self):
        """Test workcenter detail URL is accessible"""
        response = self.client.get(f'/workcenters/{self.workcenter.id}/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin_url(self):
        """Test admin URL is accessible"""
        response = self.client.get('/admin/')
        # Should redirect to login
        self.assertEqual(response.status_code, 302)


class APISanityTestCase(TestCase):
    """Test API endpoints work correctly"""
    
    def setUp(self):
        """Set up test data and authenticated user"""
        self.client = Client()
        
        # Create user and login
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # Create test data
        self.workcenter = WorkCenter.objects.create(
            name="Test WorkCenter",
            description="Test Description"
        )
        
        self.employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            employee_id="E001",
            employee_number="E001", 
            email="john.doe@example.com"
        )
        
        self.tool = Tool.objects.create(
            name="Test Tool",
            description="Test Description",
            serial_number="T001",
            location=self.workcenter
        )
    
    def test_tools_api_list(self):
        """Test tools API list endpoint"""
        response = self.client.get('/api/tools/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_tools_api_detail(self):
        """Test tools API detail endpoint"""
        response = self.client.get(f'/api/tools/{self.tool.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_employees_api_list(self):
        """Test employees API list endpoint"""
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_employees_api_detail(self):
        """Test employees API detail endpoint"""
        response = self.client.get(f'/api/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_workcenters_api_list(self):
        """Test workcenters API list endpoint"""
        response = self.client.get('/api/workcenters/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_workcenters_api_detail(self):
        """Test workcenters API detail endpoint"""
        response = self.client.get(f'/api/workcenters/{self.workcenter.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')