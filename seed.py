#!/usr/bin/env python
"""
Seed script to populate the tool management system with realistic data.
Run with: python manage.py shell < seed.py
"""

import os
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toolprogram.settings')
django.setup()

from workcenters.models import WorkCenter
from employees.models import Employee
from tools.models import Tool

# Clear existing data
print("Clearing existing data...")
Tool.objects.all().delete()
Employee.objects.all().delete()
WorkCenter.objects.all().delete()

print("Creating work centers...")
workcenters_data = [
    {
        'name': 'CNC Machining',
        'location': 'Building A - Floor 1',
        'supervisor': 'Mike Rodriguez',
        'description': 'Computer numerical control machining operations for precision parts manufacturing'
    },
    {
        'name': 'Assembly Line 1',
        'location': 'Building B - Floor 2',
        'supervisor': 'Sarah Johnson',
        'description': 'Primary assembly line for product integration and final assembly operations'
    },
    {
        'name': 'Quality Control',
        'location': 'Building A - Floor 2',
        'supervisor': 'David Chen',
        'description': 'Quality assurance testing and inspection department'
    },
    {
        'name': 'Welding Shop',
        'location': 'Building C - Floor 1',
        'supervisor': 'Robert Martinez',
        'description': 'Welding and fabrication operations for metal components'
    },
    {
        'name': 'Tool Crib',
        'location': 'Building A - Basement',
        'supervisor': 'Jennifer Wilson',
        'description': 'Central tool storage and distribution facility'
    },
    {
        'name': 'Maintenance',
        'location': 'Building D - Floor 1',
        'supervisor': 'Thomas Anderson',
        'description': 'Equipment maintenance and repair operations'
    }
]

workcenters = []
for wc_data in workcenters_data:
    workcenter = WorkCenter.objects.create(**wc_data)
    workcenters.append(workcenter)
    print(f"Created work center: {workcenter.name}")

print("\nCreating employees...")
employees_data = [
    # CNC Machining
    {'first_name': 'John', 'last_name': 'Smith', 'employee_number': 'EMP001', 'department': 'CNC Machining', 'email': 'john.smith@company.com'},
    {'first_name': 'Maria', 'last_name': 'Garcia', 'employee_number': 'EMP002', 'department': 'CNC Machining', 'email': 'maria.garcia@company.com'},
    {'first_name': 'Mike', 'last_name': 'Rodriguez', 'employee_number': 'EMP003', 'department': 'CNC Machining', 'email': 'mike.rodriguez@company.com'},
    
    # Assembly
    {'first_name': 'Sarah', 'last_name': 'Johnson', 'employee_number': 'EMP004', 'department': 'Assembly', 'email': 'sarah.johnson@company.com'},
    {'first_name': 'Kevin', 'last_name': 'Brown', 'employee_number': 'EMP005', 'department': 'Assembly', 'email': 'kevin.brown@company.com'},
    {'first_name': 'Lisa', 'last_name': 'Davis', 'employee_number': 'EMP006', 'department': 'Assembly', 'email': 'lisa.davis@company.com'},
    {'first_name': 'James', 'last_name': 'Wilson', 'employee_number': 'EMP007', 'department': 'Assembly', 'email': 'james.wilson@company.com'},
    
    # Quality Control
    {'first_name': 'David', 'last_name': 'Chen', 'employee_number': 'EMP008', 'department': 'Quality Control', 'email': 'david.chen@company.com'},
    {'first_name': 'Amanda', 'last_name': 'Taylor', 'employee_number': 'EMP009', 'department': 'Quality Control', 'email': 'amanda.taylor@company.com'},
    {'first_name': 'Steven', 'last_name': 'Lee', 'employee_number': 'EMP010', 'department': 'Quality Control', 'email': 'steven.lee@company.com'},
    
    # Welding
    {'first_name': 'Robert', 'last_name': 'Martinez', 'employee_number': 'EMP011', 'department': 'Welding', 'email': 'robert.martinez@company.com'},
    {'first_name': 'Carlos', 'last_name': 'Hernandez', 'employee_number': 'EMP012', 'department': 'Welding', 'email': 'carlos.hernandez@company.com'},
    {'first_name': 'Michelle', 'last_name': 'Thompson', 'employee_number': 'EMP013', 'department': 'Welding', 'email': 'michelle.thompson@company.com'},
    
    # Tool Crib
    {'first_name': 'Jennifer', 'last_name': 'Wilson', 'employee_number': 'EMP014', 'department': 'Tool Crib', 'email': 'jennifer.wilson@company.com'},
    {'first_name': 'Daniel', 'last_name': 'Moore', 'employee_number': 'EMP015', 'department': 'Tool Crib', 'email': 'daniel.moore@company.com'},
    
    # Maintenance
    {'first_name': 'Thomas', 'last_name': 'Anderson', 'employee_number': 'EMP016', 'department': 'Maintenance', 'email': 'thomas.anderson@company.com'},
    {'first_name': 'Nicole', 'last_name': 'Jackson', 'employee_number': 'EMP017', 'department': 'Maintenance', 'email': 'nicole.jackson@company.com'},
    {'first_name': 'Brian', 'last_name': 'White', 'employee_number': 'EMP018', 'department': 'Maintenance', 'email': 'brian.white@company.com'},
    
    # Management
    {'first_name': 'Patricia', 'last_name': 'Robinson', 'employee_number': 'EMP019', 'department': 'Management', 'email': 'patricia.robinson@company.com'},
    {'first_name': 'Richard', 'last_name': 'Clark', 'employee_number': 'EMP020', 'department': 'Management', 'email': 'richard.clark@company.com'},
]

employees = []
for emp_data in employees_data:
    # Set the legacy name field for backward compatibility
    emp_data['name'] = f"{emp_data['first_name']} {emp_data['last_name']}"
    emp_data['employee_id'] = emp_data['employee_number']  # Also set employee_id
    
    employee = Employee.objects.create(**emp_data)
    employees.append(employee)
    print(f"Created employee: {employee.first_name} {employee.last_name} ({employee.employee_number})")

print("\nCreating tools...")
tools_data = [
    # CNC Machining Tools
    {'name': 'Haas VF-2 CNC Mill', 'serial_number': 'HAS001', 'calibrated': True, 'description': 'Vertical machining center for precision milling operations', 'location': workcenters[0]},
    {'name': 'Okuma LB3000 Lathe', 'serial_number': 'OKU001', 'calibrated': True, 'description': 'CNC turning center for cylindrical parts', 'location': workcenters[0]},
    {'name': 'Mitutoyo CMM', 'serial_number': 'MIT001', 'calibrated': True, 'description': 'Coordinate measuring machine for dimensional inspection', 'location': workcenters[0]},
    {'name': 'End Mill Set 1/4"', 'serial_number': 'EM001', 'calibrated': False, 'description': 'Set of carbide end mills for milling operations', 'location': workcenters[0]},
    {'name': 'Drill Bit Set', 'serial_number': 'DB001', 'calibrated': False, 'description': 'High-speed steel drill bits various sizes', 'location': workcenters[0]},
    
    # Assembly Tools
    {'name': 'Pneumatic Torque Wrench', 'serial_number': 'PTW001', 'calibrated': True, 'description': 'Air-powered torque wrench for consistent fastening', 'location': workcenters[1]},
    {'name': 'Electric Screwdriver Set', 'serial_number': 'ESD001', 'calibrated': False, 'description': 'Battery-powered screwdrivers for assembly work', 'location': workcenters[1]},
    {'name': 'Overhead Crane', 'serial_number': 'OHC001', 'calibrated': True, 'description': '5-ton overhead crane for heavy lifting', 'location': workcenters[1]},
    {'name': 'Pneumatic Lift Table', 'serial_number': 'PLT001', 'calibrated': True, 'description': 'Air-powered lift table for ergonomic assembly', 'location': workcenters[1]},
    {'name': 'Impact Wrench Set', 'serial_number': 'IWS001', 'calibrated': False, 'description': 'Pneumatic impact wrenches various sizes', 'location': workcenters[1]},
    
    # Quality Control Tools
    {'name': 'Digital Calipers', 'serial_number': 'DC001', 'calibrated': True, 'description': 'Mitutoyo digital calipers 0-6" range', 'location': workcenters[2]},
    {'name': 'Micrometer Set', 'serial_number': 'MIC001', 'calibrated': True, 'description': 'Outside micrometers 0-4" range', 'location': workcenters[2]},
    {'name': 'Surface Plate', 'serial_number': 'SP001', 'calibrated': True, 'description': 'Granite surface plate 24"x36" Grade A', 'location': workcenters[2]},
    {'name': 'Dial Indicator Set', 'serial_number': 'DI001', 'calibrated': True, 'description': 'Dial indicators with magnetic bases', 'location': workcenters[2]},
    {'name': 'Go/No-Go Gauges', 'serial_number': 'GNG001', 'calibrated': True, 'description': 'Thread and bore gauge set', 'location': workcenters[2]},
    {'name': 'Digital Multimeter', 'serial_number': 'DMM001', 'calibrated': True, 'description': 'Fluke digital multimeter for electrical testing', 'location': workcenters[2]},
    
    # Welding Tools
    {'name': 'Miller TIG Welder', 'serial_number': 'MIL001', 'calibrated': True, 'description': 'AC/DC TIG welding machine 200A', 'location': workcenters[3]},
    {'name': 'Lincoln MIG Welder', 'serial_number': 'LIN001', 'calibrated': True, 'description': 'MIG/MAG welding machine 250A', 'location': workcenters[3]},
    {'name': 'Plasma Cutter', 'serial_number': 'PC001', 'calibrated': True, 'description': 'CNC plasma cutting table', 'location': workcenters[3]},
    {'name': 'Welding Helmet Set', 'serial_number': 'WH001', 'calibrated': False, 'description': 'Auto-darkening welding helmets', 'location': workcenters[3]},
    {'name': 'Angle Grinder Set', 'serial_number': 'AG001', 'calibrated': False, 'description': 'Pneumatic angle grinders various sizes', 'location': workcenters[3]},
    
    # Tool Crib Storage
    {'name': 'Tool Dispensing System', 'serial_number': 'TDS001', 'calibrated': False, 'description': 'Automated tool vending machine', 'location': workcenters[4]},
    {'name': 'Tool Presetter', 'serial_number': 'TP001', 'calibrated': True, 'description': 'CNC tool length and diameter measurement', 'location': workcenters[4]},
    {'name': 'Carbide Insert Inventory', 'serial_number': 'CII001', 'calibrated': False, 'description': 'Organized carbide insert storage system', 'location': workcenters[4]},
    {'name': 'Cutting Fluid System', 'serial_number': 'CFS001', 'calibrated': True, 'description': 'Centralized coolant mixing and distribution', 'location': workcenters[4]},
    
    # Maintenance Tools
    {'name': 'Fluke Vibration Analyzer', 'serial_number': 'FLK001', 'calibrated': True, 'description': 'Portable vibration analysis equipment', 'location': workcenters[5]},
    {'name': 'Infrared Thermometer', 'serial_number': 'IRT001', 'calibrated': True, 'description': 'Non-contact temperature measurement', 'location': workcenters[5]},
    {'name': 'Hydraulic Press', 'serial_number': 'HP001', 'calibrated': True, 'description': '50-ton hydraulic press for bearing installation', 'location': workcenters[5]},
    {'name': 'Ultrasonic Cleaner', 'serial_number': 'UC001', 'calibrated': False, 'description': 'Industrial ultrasonic cleaning tank', 'location': workcenters[5]},
    {'name': 'Torque Wrench Set', 'serial_number': 'TWS001', 'calibrated': True, 'description': 'Click-type torque wrenches 10-200 ft-lbs', 'location': workcenters[5]},
    {'name': 'Bearing Puller Set', 'serial_number': 'BPS001', 'calibrated': False, 'description': 'Mechanical bearing removal tools', 'location': workcenters[5]},
]

# Add some check-in times for tools (some recently used, some not)
base_time = timezone.now()

for i, tool_data in enumerate(tools_data):
    # Vary the last check-in times
    if i % 3 == 0:  # Recently checked in
        tool_data['last_checked_in'] = base_time - timedelta(hours=2 + (i % 24))
    elif i % 3 == 1:  # Checked in a few days ago
        tool_data['last_checked_in'] = base_time - timedelta(days=1 + (i % 7))
    # else: Never checked in (None)
    
    tool = Tool.objects.create(**tool_data)
    print(f"Created tool: {tool.name} ({tool.serial_number}) - Location: {tool.location.name if tool.location else 'Unassigned'}")

print(f"\nData seeding completed!")
print(f"Created {WorkCenter.objects.count()} work centers")
print(f"Created {Employee.objects.count()} employees")
print(f"Created {Tool.objects.count()} tools")

# Show some statistics
print(f"\nCalibrated tools: {Tool.objects.filter(calibrated=True).count()}")
print(f"Tools with recent check-ins: {Tool.objects.filter(last_checked_in__gte=base_time - timedelta(days=1)).count()}")
print(f"Tools never checked in: {Tool.objects.filter(last_checked_in__isnull=True).count()}")