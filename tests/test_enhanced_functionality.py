"""
Enhanced functionality tests for improved models and features
Tests new model properties, methods, and validation
"""
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta

from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter


class ToolModelEnhancementTestCase(TestCase):
    """Test enhanced Tool model functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.workcenter = WorkCenter.objects.create(
            name="TEST-WC-01",
            location="Test Building - Floor 1", 
            supervisor="Test Supervisor",
            description="Test work center for unit testing"
        )
        
        self.tool = Tool.objects.create(
            name="Test Precision Micrometer",
            serial_number="TEST-MIC-001",
            description="High-precision micrometer for testing",
            calibrated=True,
            location=self.workcenter
        )

    def test_tool_properties(self):
        """Test new Tool model properties"""
        # Test calibration_status property
        self.assertEqual(self.tool.calibration_status, "Calibrated")
        
        uncalibrated_tool = Tool.objects.create(
            name="Uncalibrated Tool",
            serial_number="TEST-UNCAL-001",
            calibrated=False
        )
        self.assertEqual(uncalibrated_tool.calibration_status, "Requires Calibration")
        
        # Test location_name property
        self.assertEqual(self.tool.location_name, "TEST-WC-01")
        
        unassigned_tool = Tool.objects.create(
            name="Unassigned Tool",
            serial_number="TEST-UNASSIGNED-001"
        )
        self.assertEqual(unassigned_tool.location_name, "Unassigned")

    def test_tool_is_available_property(self):
        """Test is_available property"""
        # Tool with no check-in time should be available
        self.assertTrue(self.tool.is_available)
        
        # Tool checked in recently should still be available (in this simple logic)
        self.tool.last_checked_in = timezone.now() - timedelta(hours=1)
        self.tool.save()
        self.assertTrue(self.tool.is_available)

    def test_tool_check_in_method(self):
        """Test check_in method"""
        initial_checkin = self.tool.last_checked_in
        self.tool.check_in()
        
        # Refresh from database
        self.tool.refresh_from_db()
        self.assertIsNotNone(self.tool.last_checked_in)
        self.assertNotEqual(initial_checkin, self.tool.last_checked_in)

    def test_tool_assign_to_location_method(self):
        """Test assign_to_location method"""
        new_workcenter = WorkCenter.objects.create(
            name="NEW-WC-01",
            location="New Test Building",
            supervisor="New Supervisor"
        )
        
        self.tool.assign_to_location(new_workcenter)
        self.tool.refresh_from_db()
        
        self.assertEqual(self.tool.location, new_workcenter)
        self.assertEqual(self.tool.location_name, "NEW-WC-01")

    def test_serial_number_uniqueness(self):
        """Test that serial numbers must be unique"""
        with self.assertRaises(Exception):  # Django will raise an IntegrityError
            Tool.objects.create(
                name="Duplicate Serial Tool",
                serial_number="TEST-MIC-001",  # Same as self.tool
                description="This should fail"
            )


class EmployeeModelEnhancementTestCase(TestCase):
    """Test enhanced Employee model functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.employee = Employee.objects.create(
            employee_number="EMP-001",
            first_name="John",
            last_name="Smith",
            department="Manufacturing",
            email="john.smith@company.com"
        )

    def test_employee_properties(self):
        """Test new Employee model properties"""
        # Test full_name property
        self.assertEqual(self.employee.full_name, "John Smith")
        
        # Test display_name property
        self.assertEqual(self.employee.display_name, "John Smith (EMP-001)")
        
        # Test with legacy name field
        legacy_employee = Employee.objects.create(
            employee_number="EMP-002",
            name="Jane Doe",
            department="Quality",
            email="jane.doe@company.com"
        )
        self.assertEqual(legacy_employee.full_name, "Jane Doe")

    def test_employee_clean_method(self):
        """Test clean method auto-population"""
        employee = Employee(
            employee_number="EMP-003",
            first_name="Bob",
            last_name="Johnson",
            department="Assembly",
            email="bob.johnson@company.com"
        )
        
        # Name should be empty before clean
        self.assertEqual(employee.name, "")
        
        # Save should trigger clean
        employee.save()
        
        # Name should now be populated
        self.assertEqual(employee.name, "Bob Johnson")
        self.assertEqual(employee.employee_id, "EMP-003")

    def test_employee_number_validation(self):
        """Test employee number format validation"""
        # Valid format should work
        valid_employee = Employee(
            employee_number="EMP-999",
            first_name="Valid",
            last_name="Employee",
            name="Valid Employee",  # Required field
            employee_id="EMP-999",  # Required field
            department="Test",
            email="valid@company.com"
        )
        
        try:
            valid_employee.full_clean()
        except ValidationError as e:
            # Check if the validation error is only about employee_number format
            if 'employee_number' in e.error_dict:
                self.fail("Valid employee number should not raise ValidationError")
            # If it's other fields, that's expected in this test

    def test_employee_number_uniqueness(self):
        """Test that employee numbers must be unique"""
        with self.assertRaises(Exception):  # Django will raise an IntegrityError
            Employee.objects.create(
                employee_number="EMP-001",  # Same as self.employee
                first_name="Duplicate",
                last_name="Employee",
                department="Test",
                email="duplicate@company.com"
            )


class WorkCenterModelEnhancementTestCase(TestCase):
    """Test enhanced WorkCenter model functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.workcenter = WorkCenter.objects.create(
            name="ENHANCED-WC-01",
            location="Enhanced Building - Bay 1",
            supervisor="Enhanced Supervisor",
            description="Enhanced work center with comprehensive testing capabilities"
        )
        
        # Create test tools
        self.calibrated_tool = Tool.objects.create(
            name="Calibrated Test Tool",
            serial_number="CAL-TOOL-001",
            calibrated=True,
            location=self.workcenter
        )
        
        self.uncalibrated_tool = Tool.objects.create(
            name="Uncalibrated Test Tool", 
            serial_number="UNCAL-TOOL-001",
            calibrated=False,
            location=self.workcenter
        )

    def test_workcenter_properties(self):
        """Test new WorkCenter model properties"""
        # Test tool_count property
        self.assertEqual(self.workcenter.tool_count, 2)
        
        # Test calibrated_tool_count property
        self.assertEqual(self.workcenter.calibrated_tool_count, 1)
        
        # Test display_info property
        expected_info = "ENHANCED-WC-01 - Enhanced Building - Bay 1 (Supervisor: Enhanced Supervisor)"
        self.assertEqual(self.workcenter.display_info, expected_info)

    def test_workcenter_tool_methods(self):
        """Test WorkCenter tool retrieval methods"""
        # Test get_tools method
        all_tools = self.workcenter.get_tools()
        self.assertEqual(all_tools.count(), 2)
        
        # Test get_calibrated_tools method
        calibrated_tools = self.workcenter.get_calibrated_tools()
        self.assertEqual(calibrated_tools.count(), 1)
        self.assertIn(self.calibrated_tool, calibrated_tools)
        
        # Test get_uncalibrated_tools method
        uncalibrated_tools = self.workcenter.get_uncalibrated_tools()
        self.assertEqual(uncalibrated_tools.count(), 1)
        self.assertIn(self.uncalibrated_tool, uncalibrated_tools)

    def test_workcenter_name_uniqueness(self):
        """Test that work center names must be unique"""
        with self.assertRaises(Exception):  # Django will raise an IntegrityError
            WorkCenter.objects.create(
                name="ENHANCED-WC-01",  # Same as self.workcenter
                location="Duplicate Location",
                supervisor="Duplicate Supervisor"
            )


class ModelIntegrationTestCase(TestCase):
    """Test integration between enhanced models"""
    
    def setUp(self):
        """Set up test data for integration testing"""
        self.workcenter = WorkCenter.objects.create(
            name="INTEGRATION-WC-01",
            location="Integration Test Building",
            supervisor="Integration Supervisor"
        )
        
        self.employee = Employee.objects.create(
            employee_number="EMP-100",
            first_name="Integration",
            last_name="Tester",
            department="Testing",
            email="integration@company.com"
        )

    def test_tool_workcenter_relationship(self):
        """Test Tool-WorkCenter relationship functionality"""
        # Create tool assigned to work center
        tool = Tool.objects.create(
            name="Integration Test Tool",
            serial_number="INT-TOOL-001",
            location=self.workcenter,
            calibrated=True
        )
        
        # Test work center can access its tools
        self.assertEqual(self.workcenter.tool_count, 1)
        self.assertIn(tool, self.workcenter.get_tools())
        
        # Test tool location methods
        self.assertEqual(tool.location_name, "INTEGRATION-WC-01")
        
        # Test reassigning tool
        new_workcenter = WorkCenter.objects.create(
            name="NEW-INTEGRATION-WC",
            location="New Building",
            supervisor="New Supervisor"
        )
        
        tool.assign_to_location(new_workcenter)
        
        # Verify counts updated
        self.assertEqual(self.workcenter.tool_count, 0)
        self.assertEqual(new_workcenter.tool_count, 1)

    def test_model_string_representations(self):
        """Test that all model string representations work correctly"""
        tool = Tool.objects.create(
            name="String Test Tool",
            serial_number="STR-TOOL-001",
            location=self.workcenter
        )
        
        # Test __str__ methods
        self.assertEqual(str(self.workcenter), "INTEGRATION-WC-01")
        self.assertEqual(str(self.employee), "Integration Tester")
        self.assertEqual(str(tool), "String Test Tool (STR-TOOL-001)")

    def test_model_verbose_names(self):
        """Test that verbose names are properly set"""
        # Access meta information
        self.assertEqual(Tool._meta.verbose_name, "Tool")
        self.assertEqual(Tool._meta.verbose_name_plural, "Tools")
        
        self.assertEqual(Employee._meta.verbose_name, "Employee")
        self.assertEqual(Employee._meta.verbose_name_plural, "Employees")
        
        self.assertEqual(WorkCenter._meta.verbose_name, "Work Center")
        self.assertEqual(WorkCenter._meta.verbose_name_plural, "Work Centers")