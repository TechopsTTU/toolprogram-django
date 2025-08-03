"""
End-to-end tests - test complete user workflows
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter
import json


class ToolManagementWorkflowTestCase(TestCase):
    """Test complete tool management workflow"""
    
    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        
        # Create user
        self.user = User.objects.create_user(
            username='toolmanager',
            password='toolpass123',
            email='manager@example.com'
        )
        
        # Create initial workcenter
        self.workcenter = WorkCenter.objects.create(
            name="Manufacturing Floor",
            description="Main manufacturing area"
        )
        
        self.secondary_wc = WorkCenter.objects.create(
            name="Quality Control",
            description="Quality control area"
        )
    
    def test_complete_tool_lifecycle(self):
        """Test complete tool lifecycle from creation to deletion"""
        
        # Step 1: Create a new tool
        tool_data = {
            'name': 'Precision Drill',
            'description': 'High-precision drilling tool',
            'serial_number': 'PD-2024-001',
            'location': self.workcenter.id
        }
        
        response = self.client.post('/tools/create/', tool_data)
        self.assertIn(response.status_code, [200, 201, 302])
        
        # Verify tool was created
        tool = Tool.objects.filter(serial_number='PD-2024-001').first()
        self.assertIsNotNone(tool)
        self.assertEqual(tool.name, 'Precision Drill')
        self.assertEqual(tool.location, self.workcenter)
        
        # Step 2: View tool details
        response = self.client.get(f'/tools/{tool.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Precision Drill')
        self.assertContains(response, 'PD-2024-001')
        
        # Step 3: Update tool information
        update_data = {
            'name': 'Precision Drill Pro',
            'description': 'High-precision drilling tool - upgraded model',
            'serial_number': 'PD-2024-001',
            'location': self.secondary_wc.id  # Move to different location
        }
        
        response = self.client.post(f'/tools/{tool.id}/edit/', update_data)
        self.assertIn(response.status_code, [200, 302])
        
        # Verify update
        tool.refresh_from_db()
        self.assertEqual(tool.name, 'Precision Drill Pro')
        self.assertEqual(tool.location, self.secondary_wc)
        
        # Step 4: View updated tool
        response = self.client.get(f'/tools/{tool.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Precision Drill Pro')
        self.assertContains(response, 'Quality Control')
        
        # Step 5: View tool in list
        response = self.client.get('/tools/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Precision Drill Pro')
        
        # Step 6: Delete tool
        response = self.client.post(f'/tools/{tool.id}/delete/')
        self.assertIn(response.status_code, [200, 302])
        
        # Verify deletion
        tool_exists = Tool.objects.filter(id=tool.id).exists()
        self.assertFalse(tool_exists)


class EmployeeManagementWorkflowTestCase(TestCase):
    """Test complete employee management workflow"""
    
    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        
        # Create user
        self.user = User.objects.create_user(
            username='hrmanager',
            password='hrpass123'
        )
    
    def test_employee_onboarding_workflow(self):
        """Test complete employee onboarding workflow"""
        
        # Step 1: Create new employee
        employee_data = {
            'first_name': 'Alice',
            'last_name': 'Johnson',
            'employee_id': 'AJ2024001',
            'email': 'alice.johnson@company.com'
        }
        
        response = self.client.post('/employees/create/', employee_data)
        self.assertIn(response.status_code, [200, 201, 302])
        
        # Verify employee creation
        employee = Employee.objects.filter(employee_id='AJ2024001').first()
        self.assertIsNotNone(employee)
        self.assertEqual(employee.first_name, 'Alice')
        self.assertEqual(employee.last_name, 'Johnson')
        
        # Step 2: View employee profile
        response = self.client.get(f'/employees/{employee.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice Johnson')
        self.assertContains(response, 'AJ2024001')
        
        # Step 3: Update employee information
        update_data = {
            'first_name': 'Alice',
            'last_name': 'Johnson-Smith',
            'employee_id': 'AJ2024001',
            'email': 'alice.johnson-smith@company.com'
        }
        
        response = self.client.post(f'/employees/{employee.id}/edit/', update_data)
        self.assertIn(response.status_code, [200, 302])
        
        # Verify update
        employee.refresh_from_db()
        self.assertEqual(employee.last_name, 'Johnson-Smith')
        self.assertEqual(employee.email, 'alice.johnson-smith@company.com')
        
        # Step 4: View in employee list
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Johnson-Smith')


class WorkCenterOperationsWorkflowTestCase(TestCase):
    """Test complete workcenter operations workflow"""
    
    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        
        # Create user
        self.user = User.objects.create_user(
            username='opsmanager',
            password='opspass123'
        )
    
    def test_workcenter_setup_workflow(self):
        """Test complete workcenter setup workflow"""
        
        # Step 1: Create new workcenter
        wc_data = {
            'name': 'Assembly Line A',
            'description': 'Primary assembly line for product A'
        }
        
        response = self.client.post('/workcenters/create/', wc_data)
        self.assertIn(response.status_code, [200, 201, 302])
        
        # Verify workcenter creation
        wc = WorkCenter.objects.filter(name='Assembly Line A').first()
        self.assertIsNotNone(wc)
        
        # Step 2: Add tools to workcenter
        tool_data = {
            'name': 'Assembly Tool 1',
            'description': 'Primary assembly tool',
            'serial_number': 'AT1-001',
            'location': wc.id
        }
        
        response = self.client.post('/tools/create/', tool_data)
        self.assertIn(response.status_code, [200, 201, 302])
        
        tool = Tool.objects.filter(serial_number='AT1-001').first()
        self.assertIsNotNone(tool)
        self.assertEqual(tool.location, wc)
        
        # Step 3: View workcenter with tools
        response = self.client.get(f'/workcenters/{wc.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Assembly Line A')
        
        # Step 4: Update workcenter
        update_data = {
            'name': 'Assembly Line A - Updated',
            'description': 'Primary assembly line for product A - now with upgrades'
        }
        
        response = self.client.post(f'/workcenters/{wc.id}/edit/', update_data)
        self.assertIn(response.status_code, [200, 302])
        
        # Verify update
        wc.refresh_from_db()
        self.assertEqual(wc.name, 'Assembly Line A - Updated')


class APIWorkflowTestCase(TestCase):
    """Test complete API workflows"""
    
    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        
        # Create user and authenticate
        self.user = User.objects.create_user(
            username='apiuser',
            password='apipass123'
        )
        self.client.login(username='apiuser', password='apipass123')
        
        # Create initial data
        self.workcenter = WorkCenter.objects.create(
            name="API Test Center",
            description="WorkCenter for API testing"
        )
    
    def test_api_data_integration_workflow(self):
        """Test complete data integration workflow via API"""
        
        # Step 1: Create employee via API
        employee_data = {
            'first_name': 'API',
            'last_name': 'Tester',
            'employee_id': 'API001',
            'email': 'api.tester@company.com'
        }
        
        response = self.client.post(
            '/api/employees/',
            json.dumps(employee_data),
            content_type='application/json'
        )
        self.assertIn(response.status_code, [200, 201])
        
        if response.status_code == 201:
            employee_id = response.json().get('id')
            
            # Step 2: Create tool via API
            tool_data = {
                'name': 'API Test Tool',
                'description': 'Tool created via API workflow',
                'serial_number': 'API-TOOL-001',
                'location': self.workcenter.id
            }
            
            response = self.client.post(
                '/api/tools/',
                json.dumps(tool_data),
                content_type='application/json'
            )
            self.assertIn(response.status_code, [200, 201])
            
            if response.status_code == 201:
                tool_id = response.json().get('id')
                
                # Step 3: Retrieve all data via API
                response = self.client.get('/api/tools/')
                self.assertEqual(response.status_code, 200)
                tools_data = response.json()
                
                response = self.client.get('/api/employees/')
                self.assertEqual(response.status_code, 200)
                employees_data = response.json()
                
                response = self.client.get('/api/workcenters/')
                self.assertEqual(response.status_code, 200)
                workcenters_data = response.json()
                
                # Verify data integrity
                self.assertIsInstance(tools_data, dict)
                self.assertIsInstance(employees_data, dict)
                self.assertIsInstance(workcenters_data, dict)


class IntegrationWorkflowTestCase(TestCase):
    """Test integration between different components"""
    
    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        
        # Create comprehensive test data
        self.user = User.objects.create_user(
            username='integrationuser',
            password='integrpass123'
        )
        
        # Create multiple workcenters
        self.wc1 = WorkCenter.objects.create(
            name="Production Line 1",
            description="First production line"
        )
        
        self.wc2 = WorkCenter.objects.create(
            name="Production Line 2",
            description="Second production line"
        )
        
        # Create employees
        self.employee1 = Employee.objects.create(
            first_name="John",
            last_name="Operator",
            employee_id="OP001",
            email="john.operator@company.com"
        )
        
        self.employee2 = Employee.objects.create(
            first_name="Jane",
            last_name="Supervisor",
            employee_id="SUP001",
            email="jane.supervisor@company.com"
        )
    
    def test_multi_component_workflow(self):
        """Test workflow involving multiple components"""
        
        # Step 1: Create tools for different workcenters
        tool1_data = {
            'name': 'Line 1 Tool',
            'description': 'Tool for production line 1',
            'serial_number': 'L1-TOOL-001',
            'location': self.wc1.id
        }
        
        tool2_data = {
            'name': 'Line 2 Tool',
            'description': 'Tool for production line 2',
            'serial_number': 'L2-TOOL-001',
            'location': self.wc2.id
        }
        
        # Create tools
        response1 = self.client.post('/tools/create/', tool1_data)
        response2 = self.client.post('/tools/create/', tool2_data)
        
        self.assertIn(response1.status_code, [200, 201, 302])
        self.assertIn(response2.status_code, [200, 201, 302])
        
        # Verify tools were created in correct locations
        tool1 = Tool.objects.filter(serial_number='L1-TOOL-001').first()
        tool2 = Tool.objects.filter(serial_number='L2-TOOL-001').first()
        
        self.assertEqual(tool1.location, self.wc1)
        self.assertEqual(tool2.location, self.wc2)
        
        # Step 2: Move tool between workcenters
        move_data = {
            'name': 'Line 1 Tool',
            'description': 'Tool moved to production line 2',
            'serial_number': 'L1-TOOL-001',
            'location': self.wc2.id  # Move to line 2
        }
        
        response = self.client.post(f'/tools/{tool1.id}/edit/', move_data)
        self.assertIn(response.status_code, [200, 302])
        
        # Verify move
        tool1.refresh_from_db()
        self.assertEqual(tool1.location, self.wc2)
        
        # Step 3: Verify both tools are now at same location
        wc2_tools = Tool.objects.filter(location=self.wc2)
        self.assertEqual(wc2_tools.count(), 2)
        
        # Step 4: View workcenter with both tools
        response = self.client.get(f'/workcenters/{self.wc2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Line 1 Tool')
        self.assertContains(response, 'Line 2 Tool')