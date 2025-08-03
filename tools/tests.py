from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from .models import Tool
from django.utils.timezone import make_aware

class ToolModelTest(TestCase):
    def setUp(self):
        self.test_date = make_aware(datetime(2024, 1, 1, 12, 0, 0))
        self.tool = Tool.objects.create(
            name="Test Tool",
            serial_number="TEST123",
            calibrated=True,
            last_checked_in=self.test_date
        )

    def test_tool_creation(self):
        self.assertEqual(self.tool.name, "Test Tool")
        self.assertEqual(self.tool.serial_number, "TEST123")
        self.assertTrue(self.tool.calibrated)
        self.assertEqual(self.tool.last_checked_in, self.test_date)

    def test_tool_str_representation(self):
        expected_str = "Test Tool (TEST123)"
        self.assertEqual(str(self.tool), expected_str)

    def test_default_calibration_status(self):
        new_tool = Tool.objects.create(
            name="Uncalibrated Tool",
            serial_number="UNCAL123"
        )
        self.assertFalse(new_tool.calibrated)

    def test_optional_last_checked_in(self):
        new_tool = Tool.objects.create(
            name="No Check-in Tool",
            serial_number="NOCHECK123"
        )
        self.assertIsNone(new_tool.last_checked_in)

class ToolViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_date = make_aware(datetime(2024, 1, 1, 12, 0, 0))
        self.tool = Tool.objects.create(
            name="Test Tool",
            serial_number="TEST123",
            calibrated=True,
            last_checked_in=self.test_date
        )
        # URLs
        self.list_url = reverse('tools:tool_list')
        self.detail_url = reverse('tools:tool_detail', args=[self.tool.id])
        self.create_url = reverse('tools:tool_add')
        self.update_url = reverse('tools:tool_edit', args=[self.tool.id])
        self.delete_url = reverse('tools:tool_delete', args=[self.tool.id])

    def test_tool_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools/tool_list.html')
        self.assertContains(response, "Test Tool")

    def test_tool_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools/tool_detail.html')
        self.assertContains(response, "Test Tool")
        self.assertContains(response, "TEST123")

    def test_tool_create_view(self):
        new_tool_data = {
            'name': 'New Tool',
            'serial_number': 'NEW123',
            'calibrated': False,
            'last_checked_in': self.test_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        response = self.client.post(self.create_url, new_tool_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tool.objects.filter(name='New Tool').exists())

    def test_tool_update_view(self):
        updated_data = {
            'name': 'Updated Tool',
            'serial_number': 'TEST123',
            'calibrated': False,
            'last_checked_in': self.test_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        response = self.client.post(self.update_url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.tool.refresh_from_db()
        self.assertEqual(self.tool.name, 'Updated Tool')

    def test_tool_delete_view(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tool.objects.filter(id=self.tool.id).exists())

    def test_invalid_tool_creation(self):
        invalid_data = {
            'name': '',  # Empty name should fail
            'serial_number': 'TEST123'
        }
        response = self.client.post(self.create_url, invalid_data)
        self.assertEqual(response.status_code, 200)  # Returns to form
        self.assertFalse(Tool.objects.filter(serial_number='TEST123', name='').exists())

    def test_nonexistent_tool_detail(self):
        response = self.client.get(reverse('tools:tool_detail', args=[99999]))
        self.assertEqual(response.status_code, 404)
