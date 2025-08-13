#!/usr/bin/env python3
"""
Comprehensive Demo Data Population Script for Tool Management System
Based on Legacy VB/.NET System Analysis
"""

import os
import sys
import django
from datetime import datetime, timedelta
from django.utils import timezone
from decimal import Decimal
import random

# Add the project directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toolprogram.settings')
django.setup()

# Import Django models
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter
from tooltracker.models import ToolTransaction
from measure.models import ToolMeasure

def clear_existing_data():
    """Clear existing data to start fresh"""
    print("Clearing existing data...")
    ToolTransaction.objects.all().delete()
    ToolMeasure.objects.all().delete()
    Tool.objects.all().delete()
    Employee.objects.all().delete()
    WorkCenter.objects.all().delete()
    print("Existing data cleared")

def create_work_centers():
    """Create comprehensive work centers"""
    print("Creating work centers...")
    
    work_centers_data = [
        {'name': 'PRESS', 'description': 'Hot Press Operations - Carbon composite forming'},
        {'name': 'MACH', 'description': 'CNC Machining Center - Precision operations'},
        {'name': 'INSPECT', 'description': 'Quality Control Inspection'},
        {'name': 'GRAPH', 'description': 'Graphite Processing'},
        {'name': 'ASSEMBLY', 'description': 'Final Assembly Operations'},
        {'name': 'FURNACE', 'description': 'High Temperature Operations'},
        {'name': 'COATING', 'description': 'Surface Coating Application'},
        {'name': 'EDM', 'description': 'Electrical Discharge Machining'},
        {'name': 'GRIND', 'description': 'Precision Grinding Operations'},
        {'name': 'SHIPPING', 'description': 'Packaging and Shipping'},
        {'name': 'MAINT', 'description': 'Maintenance Workshop'},
        {'name': 'TOOL', 'description': 'Tool Room'},
        {'name': 'LAB', 'description': 'Materials Laboratory'},
        {'name': 'R&D', 'description': 'Research and Development'},
        {'name': 'OFFICE', 'description': 'Engineering Office'}
    ]
    
    work_centers = []
    for wc_data in work_centers_data:
        wc = WorkCenter.objects.create(**wc_data)
        work_centers.append(wc)
        print(f"  Created: {wc.name} - {wc.description}")
    
    print(f"Created {len(work_centers)} work centers")
    return work_centers

def create_employees():
    """Create comprehensive employee roster"""
    print("Creating employees...")
    
    employees_data = [
        {'employee_number': 'EMP-001', 'first_name': 'Michael', 'last_name': 'Johnson', 'department': 'Management', 'email': 'mjohnson@toyotanso.com'},
        {'employee_number': 'EMP-002', 'first_name': 'Sarah', 'last_name': 'Chen', 'department': 'Engineering', 'email': 'schen@toyotanso.com'},
        {'employee_number': 'EMP-003', 'first_name': 'Robert', 'last_name': 'Williams', 'department': 'Engineering', 'email': 'rwilliams@toyotanso.com'},
        {'employee_number': 'EMP-004', 'first_name': 'Maria', 'last_name': 'Rodriguez', 'department': 'Production', 'email': 'mrodriguez@toyotanso.com'},
        {'employee_number': 'EMP-005', 'first_name': 'David', 'last_name': 'Kim', 'department': 'Production', 'email': 'dkim@toyotanso.com'},
        {'employee_number': 'EMP-006', 'first_name': 'James', 'last_name': 'Thompson', 'department': 'Manufacturing', 'email': 'jthompson@toyotanso.com'},
        {'employee_number': 'EMP-007', 'first_name': 'Lisa', 'last_name': 'Anderson', 'department': 'Manufacturing', 'email': 'landerson@toyotanso.com'},
        {'employee_number': 'EMP-008', 'first_name': 'Carlos', 'last_name': 'Martinez', 'department': 'Manufacturing', 'email': 'cmartinez@toyotanso.com'},
        {'employee_number': 'EMP-009', 'first_name': 'Jennifer', 'last_name': 'Taylor', 'department': 'Quality Control', 'email': 'jtaylor@toyotanso.com'},
        {'employee_number': 'EMP-010', 'first_name': 'Antonio', 'last_name': 'Garcia', 'department': 'Manufacturing', 'email': 'agarcia@toyotanso.com'},
        {'employee_number': 'EMP-011', 'first_name': 'Thomas', 'last_name': 'Wilson', 'department': 'Maintenance', 'email': 'twilson@toyotanso.com'},
        {'employee_number': 'EMP-012', 'first_name': 'Patricia', 'last_name': 'Brown', 'department': 'Maintenance', 'email': 'pbrown@toyotanso.com'},
        {'employee_number': 'EMP-013', 'first_name': 'Kevin', 'last_name': 'Lee', 'department': 'IT', 'email': 'klee@toyotanso.com'},
        {'employee_number': 'EMP-014', 'first_name': 'Rebecca', 'last_name': 'Davis', 'department': 'R&D', 'email': 'rdavis@toyotanso.com'},
        {'employee_number': 'EMP-015', 'first_name': 'Mark', 'last_name': 'Miller', 'department': 'Laboratory', 'email': 'mmiller@toyotanso.com'},
        {'employee_number': 'EMP-016', 'first_name': 'Angela', 'last_name': 'Moore', 'department': 'Manufacturing', 'email': 'amoore@toyotanso.com'},
        {'employee_number': 'EMP-017', 'first_name': 'Daniel', 'last_name': 'Jackson', 'department': 'Manufacturing', 'email': 'djackson@toyotanso.com'},
        {'employee_number': 'EMP-018', 'first_name': 'Michelle', 'last_name': 'White', 'department': 'Manufacturing', 'email': 'mwhite@toyotanso.com'},
        {'employee_number': 'EMP-019', 'first_name': 'Christopher', 'last_name': 'Harris', 'department': 'Shipping', 'email': 'charris@toyotanso.com'},
        {'employee_number': 'EMP-020', 'first_name': 'Sandra', 'last_name': 'Clark', 'department': 'Shipping', 'email': 'sclark@toyotanso.com'}
    ]
    
    employees = []
    for emp_data in employees_data:
        employee = Employee.objects.create(**emp_data)
        employees.append(employee)
        print(f"  Created: {employee.employee_number} - {employee.first_name} {employee.last_name}")
    
    print(f"Created {len(employees)} employees")
    return employees

def create_tools(work_centers):
    """Create extensive tool inventory"""
    print("Creating tool inventory...")
    
    tools_data = [
        # Precision Measuring Instruments
        {'serial_number': 'MIT-001-2024', 'name': 'Mitutoyo Digital Caliper', 'description': '6" Digital Caliper, 0.0005" accuracy', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'MIT-002-2024', 'name': 'Mitutoyo Height Gauge', 'description': '12" Digital Height Gauge with scriber', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'MIT-003-2024', 'name': 'Mitutoyo Micrometer Set', 'description': '0-6" Outside Micrometer Set, carbide faces', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'STR-001-2024', 'name': 'Starrett Surface Plate', 'description': '18x24" Grade A Granite Surface Plate', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'FED-001-2024', 'name': 'Federal Testmaster', 'description': 'Digital Indicator, 0.00005" resolution', 'calibrated': True, 'location': work_centers[11]},
        
        # CNC Machining Tools
        {'serial_number': 'KEN-101-2024', 'name': 'Kennametal End Mill', 'description': '1/2" 4-Flute Carbide End Mill, TiAlN coated', 'calibrated': False, 'location': work_centers[1]},
        {'serial_number': 'SAN-201-2024', 'name': 'Sandvik Turning Insert', 'description': 'CNMG432 Carbide Insert for steel turning', 'calibrated': False, 'location': work_centers[1]},
        {'serial_number': 'HAM-301-2024', 'name': 'Haimer Tool Holder', 'description': 'CAT40 ER32 Collet Chuck, balanced', 'calibrated': False, 'location': work_centers[1]},
        {'serial_number': 'MIT-401-2024', 'name': 'Mitsubishi Face Mill', 'description': '4" Face Mill with APKT inserts', 'calibrated': False, 'location': work_centers[1]},
        {'serial_number': 'WAL-501-2024', 'name': 'Walter Drill', 'description': '0.375" Carbide Drill, through coolant', 'calibrated': False, 'location': work_centers[1]},
        
        # EDM Tools
        {'serial_number': 'EDM-001-2024', 'name': 'EDM Electrode Set', 'description': 'Graphite Electrode Set, various grades', 'calibrated': False, 'location': work_centers[7]},
        {'serial_number': 'BRA-002-2024', 'name': 'Brass Wire EDM', 'description': '0.010" Brass Wire, high conductivity', 'calibrated': False, 'location': work_centers[7]},
        
        # Grinding Tools
        {'serial_number': 'NOR-101-2024', 'name': 'Norton Grinding Wheel', 'description': '14x1x5" A60-K5-V Grinding Wheel', 'calibrated': False, 'location': work_centers[8]},
        {'serial_number': '3M-201-2024', 'name': '3M Diamond Paste', 'description': 'Diamond Polishing Compound, 1 micron', 'calibrated': False, 'location': work_centers[8]},
        
        # Furnace Equipment
        {'serial_number': 'FUR-001-2024', 'name': 'Thermocouple Type K', 'description': 'High temp thermocouple, 2300F rating', 'calibrated': True, 'location': work_centers[5]},
        {'serial_number': 'FUR-002-2024', 'name': 'Graphite Fixture Set', 'description': 'High purity graphite fixtures', 'calibrated': False, 'location': work_centers[5]},
        
        # Coating Equipment
        {'serial_number': 'CVD-001-2024', 'name': 'CVD Reactor Tube', 'description': 'Quartz reaction tube, 4" ID', 'calibrated': False, 'location': work_centers[6]},
        {'serial_number': 'GAS-002-2024', 'name': 'Gas Flow Controller', 'description': 'Mass flow controller, 0-100 SCCM', 'calibrated': True, 'location': work_centers[6]},
        
        # Press Tools
        {'serial_number': 'PRE-001-2024', 'name': 'Hydraulic Press Dies', 'description': 'Tool steel die set, 4x4 cavity', 'calibrated': False, 'location': work_centers[0]},
        {'serial_number': 'PRE-002-2024', 'name': 'Pressure Gauge', 'description': 'Digital pressure gauge, 0-3000 PSI', 'calibrated': True, 'location': work_centers[0]},
        
        # Assembly Tools
        {'serial_number': 'ASM-001-2024', 'name': 'Torque Wrench Set', 'description': '1/4" Drive Torque Wrench Set', 'calibrated': True, 'location': work_centers[4]},
        {'serial_number': 'HEX-002-2024', 'name': 'Hex Key Set', 'description': 'Metric Hex Key Set, 1.5-10mm', 'calibrated': False, 'location': work_centers[4]},
        
        # Lab Equipment
        {'serial_number': 'LAB-001-2024', 'name': 'Analytical Balance', 'description': 'Precision balance, 0.1mg readability', 'calibrated': True, 'location': work_centers[12]},
        {'serial_number': 'DEN-002-2024', 'name': 'Density Meter', 'description': 'Digital density meter, 0.0001 g/cm3', 'calibrated': True, 'location': work_centers[12]},
        
        # Maintenance Tools
        {'serial_number': 'MAI-001-2024', 'name': 'Vibration Analyzer', 'description': 'Portable vibration analyzer, FFT', 'calibrated': True, 'location': work_centers[10]},
        {'serial_number': 'INF-002-2024', 'name': 'Infrared Thermometer', 'description': 'Non-contact IR thermometer', 'calibrated': True, 'location': work_centers[10]},
    ]
    
    tools = []
    for tool_data in tools_data:
        tool = Tool.objects.create(**tool_data)
        tools.append(tool)
        cal_status = "CAL" if tool.calibrated else "TOOL"
        print(f"  Created {cal_status}: {tool.serial_number} - {tool.name}")
    
    print(f"Created {len(tools)} tools")
    return tools

def create_transactions(tools, employees):
    """Create realistic tool checkout transactions"""
    print("Creating tool transactions...")
    
    transactions = []
    
    # Create some current checkouts
    for i in range(8):
        tool = tools[i]
        employee = random.choice(employees)
        checkout_date = timezone.now() - timedelta(days=random.randint(1, 14))
        promise_date = checkout_date + timedelta(days=random.randint(1, 7))
        
        transaction = ToolTransaction.objects.create(
            tool=tool,
            employee=employee,
            checkout_date=checkout_date,
            promise_return_date=promise_date.date(),
            from_location=tool.location,
            to_location=tool.location,
            status='CHECKED_OUT',
            notes=f"Checked out for {random.choice(['maintenance', 'calibration', 'setup', 'inspection'])}"
        )
        transactions.append(transaction)
        print(f"  Active: {tool.serial_number} -> {employee.first_name} {employee.last_name}")
    
    # Create some returned tools
    for i in range(8, 16):
        tool = tools[i]
        employee = random.choice(employees)
        checkout_date = timezone.now() - timedelta(days=random.randint(15, 90))
        promise_date = checkout_date + timedelta(days=random.randint(1, 7))
        return_date = checkout_date + timedelta(days=random.randint(1, 10))
        
        transaction = ToolTransaction.objects.create(
            tool=tool,
            employee=employee,
            checkout_date=checkout_date,
            promise_return_date=promise_date.date(),
            return_date=return_date,
            from_location=tool.location,
            to_location=tool.location,
            status='RETURNED',
            notes=f"Returned after {random.choice(['repair', 'calibration', 'project'])}"
        )
        transactions.append(transaction)
    
    print(f"Created {len(transactions)} transactions")
    return transactions

def create_measurements(tools):
    """Create calibration records"""
    print("Creating measurement records...")
    
    calibrated_tools = [tool for tool in tools if tool.calibrated]
    measures = []
    
    for tool in calibrated_tools[:10]:
        recent_date = timezone.now() - timedelta(days=random.randint(30, 180))
        measure = ToolMeasure.objects.create(
            tool=tool,
            employee=random.choice(Employee.objects.all()),
            measurement_date=recent_date,
            size_measured=Decimal(f"{random.uniform(0.0001, 25.5000):.4f}"),
            expected_size=Decimal(f"{random.uniform(0.0001, 25.5000):.4f}"),
            tolerance=Decimal(f"{random.uniform(0.0001, 0.0050):.4f}"),
            condition='GOOD',
            notes=f"Calibration verified against NIST standards. Temp: {random.randint(68, 72)}F"
        )
        measures.append(measure)
        print(f"  Calibration: {tool.serial_number} - {measure.measurement_date.strftime('%Y-%m-%d')}")
    
    print(f"Created {len(measures)} measurement records")
    return measures

def main():
    """Main execution function"""
    print("TOYO TANSO USA COMPREHENSIVE DEMO DATA POPULATION")
    print("=" * 60)
    print()
    
    try:
        clear_existing_data()
        print()
        
        work_centers = create_work_centers()
        print()
        
        employees = create_employees()
        print()
        
        tools = create_tools(work_centers)
        print()
        
        transactions = create_transactions(tools, employees)
        print()
        
        measures = create_measurements(tools)
        print()
        
        # Summary
        print("POPULATION COMPLETE - SUMMARY")
        print("=" * 40)
        print(f"Work Centers: {len(work_centers)}")
        print(f"Employees: {len(employees)}")
        print(f"Tools: {len(tools)}")
        print(f"Transactions: {len(transactions)}")
        print(f"Calibration Records: {len(measures)}")
        print()
        print("System ready for manufacturing demo!")
        print("Access at: http://localhost:8000")
        
    except Exception as e:
        print(f"Error during population: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()