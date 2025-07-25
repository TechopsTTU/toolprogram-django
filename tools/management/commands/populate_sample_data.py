from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from workcenters.models import WorkCenter
from employees.models import Employee
from tools.models import Tool

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample work centers...')
        
        # Create Work Centers
        workcenters_data = [
            {'name': 'Machine Shop', 'location': 'Building A - Floor 1', 'supervisor': 'John Smith', 'description': 'Main machine shop with CNC equipment'},
            {'name': 'Assembly Line', 'location': 'Building B - Floor 2', 'supervisor': 'Sarah Johnson', 'description': 'Final assembly and quality control'},
            {'name': 'Maintenance Bay', 'location': 'Building A - Basement', 'supervisor': 'Mike Brown', 'description': 'Equipment maintenance and repair'},
            {'name': 'Quality Control', 'location': 'Building C - Floor 1', 'supervisor': 'Lisa Davis', 'description': 'Quality testing and inspection'},
        ]
        
        for wc_data in workcenters_data:
            WorkCenter.objects.get_or_create(name=wc_data['name'], defaults=wc_data)
        
        self.stdout.write('Creating sample employees...')
        
        # Create Employees
        employees_data = [
            {'name': 'Alice Cooper', 'employee_id': 'EMP001', 'department': 'Manufacturing', 'email': 'alice.cooper@company.com', 'phone': '555-0101'},
            {'name': 'Bob Wilson', 'employee_id': 'EMP002', 'department': 'Quality Control', 'email': 'bob.wilson@company.com', 'phone': '555-0102'},
            {'name': 'Carol Martinez', 'employee_id': 'EMP003', 'department': 'Maintenance', 'email': 'carol.martinez@company.com', 'phone': '555-0103'},
            {'name': 'David Lee', 'employee_id': 'EMP004', 'department': 'Manufacturing', 'email': 'david.lee@company.com', 'phone': '555-0104'},
            {'name': 'Eva Rodriguez', 'employee_id': 'EMP005', 'department': 'Assembly', 'email': 'eva.rodriguez@company.com', 'phone': '555-0105'},
        ]
        
        workcenters = list(WorkCenter.objects.all())
        for i, emp_data in enumerate(employees_data):
            emp_data['primary_workcenter'] = workcenters[i % len(workcenters)]
            emp_data['hire_date'] = timezone.now().date() - timedelta(days=365 * (i + 1))
            Employee.objects.get_or_create(employee_id=emp_data['employee_id'], defaults=emp_data)
        
        self.stdout.write('Creating sample tools...')
        
        # Create Tools
        tools_data = [
            {'name': 'Digital Caliper', 'serial_number': 'DC001', 'calibrated': True, 'status': 'available'},
            {'name': 'Torque Wrench', 'serial_number': 'TW002', 'calibrated': True, 'status': 'checked_out'},
            {'name': 'Micrometer Set', 'serial_number': 'MS003', 'calibrated': False, 'status': 'calibration'},
            {'name': 'Height Gauge', 'serial_number': 'HG004', 'calibrated': True, 'status': 'available'},
            {'name': 'Drill Press', 'serial_number': 'DP005', 'calibrated': False, 'status': 'maintenance'},
            {'name': 'Surface Plate', 'serial_number': 'SP006', 'calibrated': True, 'status': 'available'},
            {'name': 'CMM Probe', 'serial_number': 'CP007', 'calibrated': True, 'status': 'checked_out'},
            {'name': 'Go/No-Go Gauge', 'serial_number': 'GNG008', 'calibrated': True, 'status': 'available'},
        ]
        
        employees = list(Employee.objects.all())
        for i, tool_data in enumerate(tools_data):
            tool_data['current_location'] = workcenters[i % len(workcenters)]
            
            # Assign some tools to employees
            if tool_data['status'] == 'checked_out':
                tool_data['assigned_to'] = employees[i % len(employees)]
                tool_data['checked_out_date'] = timezone.now() - timedelta(days=i + 1)
                tool_data['due_date'] = timezone.now() + timedelta(days=7 - i)
            
            if tool_data['status'] == 'available':
                tool_data['last_checked_in'] = timezone.now() - timedelta(hours=i * 2)
            
            Tool.objects.get_or_create(serial_number=tool_data['serial_number'], defaults=tool_data)
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data:')
        )
        self.stdout.write(f'  - {WorkCenter.objects.count()} work centers')
        self.stdout.write(f'  - {Employee.objects.count()} employees')
        self.stdout.write(f'  - {Tool.objects.count()} tools')