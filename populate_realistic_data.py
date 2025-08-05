#!/usr/bin/env python
"""
Populate SQLite database with realistic manufacturing data
"""
import os
import sys
import django
from datetime import datetime, timedelta
import random

# Setup Django - Force local environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'toolprogram.settings'
os.environ['DATABASE_ENV'] = 'local'
django.setup()

from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter

def populate_workcenters():
    """Create realistic work centers"""
    workcenters_data = [
        {'name': 'WC001', 'description': 'CNC Machining Center 1', 'supervisor': 'John Smith'},
        {'name': 'WC002', 'description': 'CNC Machining Center 2', 'supervisor': 'Jane Doe'},
        {'name': 'WC003', 'description': 'Manual Lathe Station', 'supervisor': 'Bob Johnson'},
        {'name': 'WC004', 'description': 'Milling Operations', 'supervisor': 'Alice Brown'},
        {'name': 'WC005', 'description': 'Quality Control', 'supervisor': 'Mike Wilson'},
        {'name': 'WC006', 'description': 'Assembly Line A', 'supervisor': 'Sarah Davis'},
        {'name': 'WC007', 'description': 'Assembly Line B', 'supervisor': 'Tom Miller'},
        {'name': 'WC008', 'description': 'Grinding Station', 'supervisor': 'Lisa Garcia'},
        {'name': 'WC009', 'description': 'Heat Treatment', 'supervisor': 'Chris Lee'},
        {'name': 'WC010', 'description': 'Tool Crib', 'supervisor': 'Pat Martinez'},
    ]
    
    created_wcs = []
    for wc_data in workcenters_data:
        wc, created = WorkCenter.objects.get_or_create(
            name=wc_data['name'],
            defaults={
                'description': wc_data['description'],
                'supervisor': wc_data['supervisor']
            }
        )
        if created:
            print(f"Created WorkCenter: {wc}")
        created_wcs.append(wc)
    
    return created_wcs

def populate_employees():
    """Create realistic employees"""
    employees_data = [
        {'employee_number': 'E001', 'first_name': 'John', 'last_name': 'Smith', 'department': 'Manufacturing'},
        {'employee_number': 'E002', 'first_name': 'Jane', 'last_name': 'Doe', 'department': 'Manufacturing'},
        {'employee_number': 'E003', 'first_name': 'Bob', 'last_name': 'Johnson', 'department': 'Manufacturing'},
        {'employee_number': 'E004', 'first_name': 'Alice', 'last_name': 'Brown', 'department': 'Manufacturing'},
        {'employee_number': 'E005', 'first_name': 'Mike', 'last_name': 'Wilson', 'department': 'Quality'},
        {'employee_number': 'E006', 'first_name': 'Sarah', 'last_name': 'Davis', 'department': 'Assembly'},
        {'employee_number': 'E007', 'first_name': 'Tom', 'last_name': 'Miller', 'department': 'Assembly'},
        {'employee_number': 'E008', 'first_name': 'Lisa', 'last_name': 'Garcia', 'department': 'Manufacturing'},
        {'employee_number': 'E009', 'first_name': 'Chris', 'last_name': 'Lee', 'department': 'Heat Treatment'},
        {'employee_number': 'E010', 'first_name': 'Pat', 'last_name': 'Martinez', 'department': 'Tool Crib'},
        {'employee_number': 'E011', 'first_name': 'David', 'last_name': 'Anderson', 'department': 'Manufacturing'},
        {'employee_number': 'E012', 'first_name': 'Emily', 'last_name': 'Taylor', 'department': 'Quality'},
        {'employee_number': 'E013', 'first_name': 'Ryan', 'last_name': 'Thomas', 'department': 'Manufacturing'},
        {'employee_number': 'E014', 'first_name': 'Michelle', 'last_name': 'White', 'department': 'Assembly'},
        {'employee_number': 'E015', 'first_name': 'Kevin', 'last_name': 'Harris', 'department': 'Manufacturing'},
    ]
    
    created_employees = []
    for emp_data in employees_data:
        emp, created = Employee.objects.get_or_create(
            employee_number=emp_data['employee_number'],
            defaults={
                'first_name': emp_data['first_name'],
                'last_name': emp_data['last_name'],
                'department': emp_data['department']
            }
        )
        if created:
            print(f"Created Employee: {emp}")
        created_employees.append(emp)
    
    return created_employees

def populate_tools(workcenters):
    """Create realistic tools with various calibration statuses"""
    tool_types = [
        'Micrometer', 'Caliper', 'Dial Indicator', 'Height Gauge', 'Go/No-Go Gauge',
        'Thread Gauge', 'Pin Gauge', 'Ring Gauge', 'Torque Wrench', 'Pressure Gauge',
        'Temperature Sensor', 'CMM Probe', 'Surface Roughness Tester', 'Hardness Tester',
        'Flow Meter', 'Load Cell', 'Digital Scale', 'Oscilloscope', 'Multimeter', 'pH Meter'
    ]
    
    manufacturers = ['Mitutoyo', 'Starrett', 'Brown & Sharpe', 'Mahr', 'Tesa', 'Fowler', 'SPI', 'Insize']
    
    tools_created = 0
    
    for i in range(1, 51):  # Create 50 tools
        tool_type = random.choice(tool_types)
        manufacturer = random.choice(manufacturers)
        
        # Generate realistic model numbers
        model_number = f"{manufacturer[:3].upper()}-{random.randint(100, 999)}{random.choice(['A', 'B', 'C', 'X', 'M'])}"
        
        # Generate serial numbers
        serial_number = f"{random.randint(10000, 99999)}"
        
        # Random calibration dates and statuses
        calibration_due = datetime.now() + timedelta(days=random.randint(-30, 365))
        is_calibrated = calibration_due > datetime.now()
        
        # Random last calibration (1-365 days ago)
        last_calibration = datetime.now() - timedelta(days=random.randint(1, 365))
        
        # Random location assignment (some tools unassigned)
        location = random.choice(workcenters) if random.random() > 0.2 else None
        
        # Random check-in status
        checked_in = random.choice([True, False])
        last_checked_in = datetime.now() - timedelta(days=random.randint(0, 30)) if not checked_in else None
        
        tool_data = {
            'name': f"T{i:04d} - {manufacturer} {tool_type}",
            'description': f"{manufacturer} {tool_type} Model: {model_number}",
            'serial_number': serial_number,
            'calibrated': is_calibrated,
            'location': location,
            'last_checked_in': last_checked_in,
        }
        
        tool, created = Tool.objects.get_or_create(
            serial_number=tool_data['serial_number'],
            defaults=tool_data
        )
        
        if created:
            tools_created += 1
            print(f"Created Tool: {tool}")
    
    print(f"\nTotal tools created: {tools_created}")
    return tools_created

def main():
    """Main population function"""
    print("=== Populating Database with Realistic Manufacturing Data ===\n")
    
    # Clear existing data
    print("Clearing existing data...")
    Tool.objects.all().delete()
    Employee.objects.all().delete()
    WorkCenter.objects.all().delete()
    
    # Populate in order (workcenters first, then employees, then tools)
    print("\n1. Creating Work Centers...")
    workcenters = populate_workcenters()
    
    print(f"\n2. Creating Employees...")
    employees = populate_employees()
    
    print(f"\n3. Creating Tools...")
    tools_count = populate_tools(workcenters)
    
    # Summary
    print(f"\n=== Population Complete ===")
    print(f"Work Centers: {len(workcenters)}")
    print(f"Employees: {len(employees)}")
    print(f"Tools: {tools_count}")
    
    # Show some statistics
    calibrated_tools = Tool.objects.filter(is_calibrated=True).count()
    assigned_tools = Tool.objects.exclude(location__isnull=True).count()
    checked_in_tools = Tool.objects.filter(checked_in=True).count()
    
    print(f"\nTool Statistics:")
    print(f"  Calibrated: {calibrated_tools}")
    print(f"  Assigned to work centers: {assigned_tools}")
    print(f"  Currently checked in: {checked_in_tools}")
    
    print(f"\nDatabase populated successfully! You can now test the application with realistic data.")

if __name__ == '__main__':
    main()