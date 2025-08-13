#!/usr/bin/env python3
"""
Comprehensive Demo Data Population Script for Tool Management System
Based on Legacy VB/.NET System Analysis

This script populates the Django application with extensive realistic manufacturing data
following patterns extracted from the original Tool_Tracking system.

Key patterns from legacy system:
- Employee Clock Codes: B#### format (4-digit numbers)
- Work Centers: 2-10 character names with manufacturing descriptions
- Tools: Professional precision instruments with serial numbers
- Calibration tracking and location management
"""

import os
import sys
import django
from datetime import datetime, timedelta
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
    """Create comprehensive work centers based on real manufacturing environment"""
    print("Creating work centers...")
    
    work_centers_data = [
        # Main Manufacturing Areas
        {
            'name': 'PRESS',
            'description': 'Hot Press Operations - Carbon composite forming and consolidation'
        },
        {
            'name': 'MACH',
            'description': 'CNC Machining Center - Precision turning and milling operations'
        },
        {
            'name': 'INSPECT',
            'description': 'Quality Control Inspection - Dimensional and material verification'
        },
        {
            'name': 'GRAPH',
            'description': 'Graphite Processing - Purification and grade preparation'
        },
        {
            'name': 'ASSEMBLY',
            'description': 'Final Assembly - Component integration and finishing'
        },
        
        # Specialized Production Areas
        {
            'name': 'FURNACE',
            'description': 'High Temperature Furnace Operations - Heat treatment and carbonization'
        },
        {
            'name': 'COATING',
            'description': 'Surface Coating Application - CVD/PVD processes'
        },
        {
            'name': 'EDM',
            'description': 'Electrical Discharge Machining - Precision electrode fabrication'
        },
        {
            'name': 'GRIND',
            'description': 'Precision Grinding - Surface finishing and dimensional control'
        },
        {
            'name': 'SHIPPING',
            'description': 'Packaging and Shipping - Final inspection and logistics'
        },
        
        # Support Areas
        {
            'name': 'MAINT',
            'description': 'Maintenance Workshop - Equipment repair and calibration'
        },
        {
            'name': 'TOOL',
            'description': 'Tool Room - Cutting tool preparation and storage'
        },
        {
            'name': 'LAB',
            'description': 'Materials Laboratory - Chemical and physical testing'
        },
        {
            'name': 'R&D',
            'description': 'Research and Development - Process innovation and testing'
        },
        {
            'name': 'OFFICE',
            'description': 'Engineering Office - Design, planning, and documentation'
        }
    ]
    
    work_centers = []
    for wc_data in work_centers_data:
        wc = WorkCenter.objects.create(**wc_data)
        work_centers.append(wc)
        print(f"  ➕ Created work center: {wc.name} - {wc.description}")
    
    print(f"✅ Created {len(work_centers)} work centers")
    return work_centers

def create_employees():
    """Create comprehensive employee roster with realistic manufacturing roles"""
    print("👥 Creating employees...")
    
    # Employee data following B#### clock code pattern from legacy system
    employees_data = [
        # Management and Engineering
        {'employee_number': 'EMP-001', 'clock_code': 'B1001', 'first_name': 'Michael', 'last_name': 'Johnson', 'department': 'Management', 'position': 'Plant Manager', 'email': 'mjohnson@toyotanso.com'},
        {'employee_number': 'EMP-002', 'clock_code': 'B1002', 'first_name': 'Sarah', 'last_name': 'Chen', 'department': 'Engineering', 'position': 'Process Engineer', 'email': 'schen@toyotanso.com'},
        {'employee_number': 'EMP-003', 'clock_code': 'B1003', 'first_name': 'Robert', 'last_name': 'Williams', 'department': 'Engineering', 'position': 'Quality Engineer', 'email': 'rwilliams@toyotanso.com'},
        
        # Production Supervisors
        {'employee_number': 'EMP-004', 'clock_code': 'B2001', 'first_name': 'Maria', 'last_name': 'Rodriguez', 'department': 'Production', 'position': 'Production Supervisor', 'email': 'mrodriguez@toyotanso.com'},
        {'employee_number': 'EMP-005', 'clock_code': 'B2002', 'first_name': 'David', 'last_name': 'Kim', 'department': 'Production', 'position': 'Shift Supervisor', 'email': 'dkim@toyotanso.com'},
        
        # Skilled Technicians and Operators
        {'employee_number': 'EMP-006', 'clock_code': 'B3001', 'first_name': 'James', 'last_name': 'Thompson', 'department': 'Manufacturing', 'position': 'CNC Operator', 'email': 'jthompson@toyotanso.com'},
        {'employee_number': 'EMP-007', 'clock_code': 'B3002', 'first_name': 'Lisa', 'last_name': 'Anderson', 'department': 'Manufacturing', 'position': 'Press Operator', 'email': 'landerson@toyotanso.com'},
        {'employee_number': 'EMP-008', 'clock_code': 'B3003', 'first_name': 'Carlos', 'last_name': 'Martinez', 'department': 'Manufacturing', 'position': 'Furnace Technician', 'email': 'cmartinez@toyotanso.com'},
        {'employee_number': 'EMP-009', 'clock_code': 'B3004', 'first_name': 'Jennifer', 'last_name': 'Taylor', 'department': 'Quality Control', 'position': 'QC Inspector', 'email': 'jtaylor@toyotanso.com'},
        {'employee_number': 'EMP-010', 'clock_code': 'B3005', 'first_name': 'Antonio', 'last_name': 'Garcia', 'department': 'Manufacturing', 'position': 'EDM Specialist', 'email': 'agarcia@toyotanso.com'},
        
        # Maintenance and Technical Support
        {'employee_number': 'EMP-011', 'clock_code': 'B4001', 'first_name': 'Thomas', 'last_name': 'Wilson', 'department': 'Maintenance', 'position': 'Maintenance Technician', 'email': 'twilson@toyotanso.com'},
        {'employee_number': 'EMP-012', 'clock_code': 'B4002', 'first_name': 'Patricia', 'last_name': 'Brown', 'department': 'Maintenance', 'position': 'Calibration Technician', 'email': 'pbrown@toyotanso.com'},
        {'employee_number': 'EMP-013', 'clock_code': 'B4003', 'first_name': 'Kevin', 'last_name': 'Lee', 'department': 'IT', 'position': 'Systems Administrator', 'email': 'klee@toyotanso.com'},
        
        # Laboratory and R&D
        {'employee_number': 'EMP-014', 'clock_code': 'B5001', 'first_name': 'Dr. Rebecca', 'last_name': 'Davis', 'department': 'R&D', 'position': 'Materials Scientist', 'email': 'rdavis@toyotanso.com'},
        {'employee_number': 'EMP-015', 'clock_code': 'B5002', 'first_name': 'Mark', 'last_name': 'Miller', 'department': 'Laboratory', 'position': 'Lab Technician', 'email': 'mmiller@toyotanso.com'},
        
        # Production Operators
        {'employee_number': 'EMP-016', 'clock_code': 'B6001', 'first_name': 'Angela', 'last_name': 'Moore', 'department': 'Manufacturing', 'position': 'Assembly Operator', 'email': 'amoore@toyotanso.com'},
        {'employee_number': 'EMP-017', 'clock_code': 'B6002', 'first_name': 'Daniel', 'last_name': 'Jackson', 'department': 'Manufacturing', 'position': 'Coating Technician', 'email': 'djackson@toyotanso.com'},
        {'employee_number': 'EMP-018', 'clock_code': 'B6003', 'first_name': 'Michelle', 'last_name': 'White', 'department': 'Manufacturing', 'position': 'Grinder Operator', 'email': 'mwhite@toyotanso.com'},
        
        # Shipping and Logistics
        {'employee_number': 'EMP-019', 'clock_code': 'B7001', 'first_name': 'Christopher', 'last_name': 'Harris', 'department': 'Shipping', 'position': 'Shipping Coordinator', 'email': 'charris@toyotanso.com'},
        {'employee_number': 'EMP-020', 'clock_code': 'B7002', 'first_name': 'Sandra', 'last_name': 'Clark', 'department': 'Shipping', 'position': 'Packaging Specialist', 'email': 'sclark@toyotanso.com'},
        
        # Additional Production Staff
        {'employee_number': 'EMP-021', 'clock_code': 'B8001', 'first_name': 'Ryan', 'last_name': 'Lewis', 'department': 'Manufacturing', 'position': 'Machine Operator', 'email': 'rlewis@toyotanso.com'},
        {'employee_number': 'EMP-022', 'clock_code': 'B8002', 'first_name': 'Nicole', 'last_name': 'Robinson', 'department': 'Quality Control', 'position': 'Final Inspector', 'email': 'nrobinson@toyotanso.com'},
        {'employee_number': 'EMP-023', 'clock_code': 'B8003', 'first_name': 'Steven', 'last_name': 'Walker', 'department': 'Manufacturing', 'position': 'Process Technician', 'email': 'swalker@toyotanso.com'},
        {'employee_number': 'EMP-024', 'clock_code': 'B8004', 'first_name': 'Amanda', 'last_name': 'Hall', 'department': 'Engineering', 'position': 'Manufacturing Engineer', 'email': 'ahall@toyotanso.com'},
        {'employee_number': 'EMP-025', 'clock_code': 'B8005', 'first_name': 'Brian', 'last_name': 'Young', 'department': 'Manufacturing', 'position': 'Setup Technician', 'email': 'byoung@toyotanso.com'}
    ]
    
    employees = []
    for emp_data in employees_data:
        employee = Employee.objects.create(**emp_data)
        employees.append(employee)
        print(f"  ➕ Created employee: {employee.clock_code} - {employee.first_name} {employee.last_name} ({employee.position})")
    
    print(f"✅ Created {len(employees)} employees")
    return employees

def create_comprehensive_tools(work_centers):
    """Create extensive tool inventory with realistic precision manufacturing tools"""
    print("🔧 Creating comprehensive tool inventory...")
    
    # Comprehensive tool data based on real manufacturing operations
    tools_data = [
        # Precision Measuring Instruments
        {'serial_number': 'MIT-001-2024', 'name': 'Mitutoyo Digital Caliper', 'description': '6" Digital Caliper, 0.0005" accuracy, IP67 rated', 'calibrated': True, 'location': work_centers[2]},  # INSPECT
        {'serial_number': 'MIT-002-2024', 'name': 'Mitutoyo Height Gauge', 'description': '12" Digital Height Gauge with scriber, granite base', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'MIT-003-2024', 'name': 'Mitutoyo Micrometer Set', 'description': '0-6" Outside Micrometer Set, carbide faces, ±0.00005"', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'STR-001-2024', 'name': 'Starrett Surface Plate', 'description': '18x24" Grade A Granite Surface Plate, NIST certified', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'FED-001-2024', 'name': 'Federal Testmaster', 'description': 'Digital Indicator, 0.00005" resolution, IP54', 'calibrated': True, 'location': work_centers[11]},  # TOOL
        
        # CNC Machining Tools
        {'serial_number': 'KEN-101-2024', 'name': 'Kennametal End Mill', 'description': '1/2" 4-Flute Carbide End Mill, TiAlN coated', 'calibrated': False, 'location': work_centers[1]},  # MACH
        {'serial_number': 'SAN-201-2024', 'name': 'Sandvik Turning Insert', 'description': 'CNMG432 Carbide Insert for steel/carbon turning', 'calibrated': False, 'location': work_centers[1]},
        {'serial_number': 'HAM-301-2024', 'name': 'Haimer Tool Holder', 'description': 'CAT40 ER32 Collet Chuck, balanced to 25,000 RPM', 'calibrated': False, 'location': work_centers[1]},
        {'serial_number': 'MIT-401-2024', 'name': 'Mitsubishi Face Mill', 'description': '4" Face Mill with APKT inserts, flood coolant', 'calibrated': False, 'location': work_centers[1]},
        {'serial_number': 'WAL-501-2024', 'name': 'Walter Drill', 'description': '0.375" Carbide Drill, through coolant, 3xD length', 'calibrated': False, 'location': work_centers[1]},
        
        # EDM and Wire EDM Tools
        {'serial_number': 'EDM-001-2024', 'name': 'EDM Electrode Set', 'description': 'Graphite Electrode Set, grades ET-10 through ET-35', 'calibrated': False, 'location': work_centers[7]},  # EDM
        {'serial_number': 'BRA-002-2024', 'name': 'Brass Wire EDM', 'description': '0.010" Brass Wire, high conductivity, 44lb spool', 'calibrated': False, 'location': work_centers[7]},
        {'serial_number': 'FIL-003-2024', 'name': 'Filter System', 'description': 'EDM Dielectric Filter, 5 micron, automatic backwash', 'calibrated': False, 'location': work_centers[7]},
        
        # Grinding and Finishing Tools
        {'serial_number': 'NOR-101-2024', 'name': 'Norton Grinding Wheel', 'description': '14x1x5" A60-K5-V Grinding Wheel, surface grinding', 'calibrated': False, 'location': work_centers[8]},  # GRIND
        {'serial_number': '3M-201-2024', 'name': '3M Diamond Paste', 'description': 'Diamond Polishing Compound, 1 micron, water base', 'calibrated': False, 'location': work_centers[8]},
        {'serial_number': 'FEL-301-2024', 'name': 'Felt Polishing Wheel', 'description': '6" x 1" Felt Wheel, medium density, buffing compound', 'calibrated': False, 'location': work_centers[8]},
        
        # Furnace and Heat Treatment
        {'serial_number': 'FUR-001-2024', 'name': 'Thermocouple Type K', 'description': 'High temp thermocouple, 2300°F rating, Inconel sheath', 'calibrated': True, 'location': work_centers[5]},  # FURNACE
        {'serial_number': 'FUR-002-2024', 'name': 'Graphite Fixture Set', 'description': 'High purity graphite holding fixtures, vacuum rated', 'calibrated': False, 'location': work_centers[5]},
        {'serial_number': 'INS-003-2024', 'name': 'Insulation Blanket', 'description': 'Ceramic fiber insulation, 2400°F rating, 2" thick', 'calibrated': False, 'location': work_centers[5]},
        
        # Coating and Surface Treatment
        {'serial_number': 'CVD-001-2024', 'name': 'CVD Reactor Tube', 'description': 'Quartz reaction tube, 4" ID, high purity gas inlet', 'calibrated': False, 'location': work_centers[6]},  # COATING
        {'serial_number': 'GAS-002-2024', 'name': 'Gas Flow Controller', 'description': 'Mass flow controller, 0-100 SCCM, ±1% accuracy', 'calibrated': True, 'location': work_centers[6]},
        {'serial_number': 'VAC-003-2024', 'name': 'Vacuum Pump System', 'description': 'Turbo-molecular pump, 10⁻⁸ torr, oil-free', 'calibrated': True, 'location': work_centers[6]},
        
        # Press Operations
        {'serial_number': 'PRE-001-2024', 'name': 'Hydraulic Press Dies', 'description': 'Tool steel die set, 4" x 4" cavity, hardened H13', 'calibrated': False, 'location': work_centers[0]},  # PRESS
        {'serial_number': 'PRE-002-2024', 'name': 'Pressure Gauge', 'description': 'Digital pressure gauge, 0-3000 PSI, ±0.25% FS', 'calibrated': True, 'location': work_centers[0]},
        {'serial_number': 'TEM-003-2024', 'name': 'Temperature Controller', 'description': 'PID temperature controller, 0-500°C, ±1°C accuracy', 'calibrated': True, 'location': work_centers[0]},
        
        # Assembly Tools
        {'serial_number': 'ASM-001-2024', 'name': 'Torque Wrench Set', 'description': '1/4" Drive Torque Wrench Set, 20-200 in-lbs, ±3%', 'calibrated': True, 'location': work_centers[4]},  # ASSEMBLY
        {'serial_number': 'HEX-002-2024', 'name': 'Hex Key Set', 'description': 'Metric Hex Key Set, 1.5-10mm, ball end, hardened', 'calibrated': False, 'location': work_centers[4]},
        {'serial_number': 'PIN-003-2024', 'name': 'Pin Gauge Set', 'description': 'Precision Pin Gauge Set, 0.011-0.250", Class ZZ', 'calibrated': True, 'location': work_centers[4]},
        
        # Laboratory Equipment
        {'serial_number': 'LAB-001-2024', 'name': 'Analytical Balance', 'description': 'Precision balance, 0.1mg readability, internal calibration', 'calibrated': True, 'location': work_centers[12]},  # LAB
        {'serial_number': 'DEN-002-2024', 'name': 'Density Meter', 'description': 'Digital density meter, 0.0001 g/cm³ resolution', 'calibrated': True, 'location': work_centers[12]},
        {'serial_number': 'HAR-003-2024', 'name': 'Hardness Tester', 'description': 'Rockwell Hardness Tester, scales A, B, C, digital display', 'calibrated': True, 'location': work_centers[12]},
        
        # Maintenance Tools
        {'serial_number': 'MAI-001-2024', 'name': 'Vibration Analyzer', 'description': 'Portable vibration analyzer, FFT analysis, data logging', 'calibrated': True, 'location': work_centers[10]},  # MAINT
        {'serial_number': 'INF-002-2024', 'name': 'Infrared Thermometer', 'description': 'Non-contact IR thermometer, -50 to 800°C, laser sight', 'calibrated': True, 'location': work_centers[10]},
        {'serial_number': 'MUL-003-2024', 'name': 'Digital Multimeter', 'description': 'True RMS DMM, 50,000 count, CAT IV safety rating', 'calibrated': True, 'location': work_centers[10]},
        
        # Specialized Carbon Processing Tools
        {'serial_number': 'CAR-001-2024', 'name': 'Carbon Grade Classifier', 'description': 'Sieve analysis set for carbon powder classification', 'calibrated': True, 'location': work_centers[3]},  # GRAPH
        {'serial_number': 'MIX-002-2024', 'name': 'High Energy Mixer', 'description': 'Planetary mixer for carbon-binder systems, 5L capacity', 'calibrated': False, 'location': work_centers[3]},
        {'serial_number': 'EXT-003-2024', 'name': 'Extrusion Dies', 'description': 'Tungsten carbide extrusion dies, various profiles', 'calibrated': False, 'location': work_centers[3]},
        
        # Quality Control Instruments
        {'serial_number': 'CMM-001-2024', 'name': 'Coordinate Measuring Machine', 'description': 'CMM Bridge Type, 24x16x12" envelope, Renishaw probe', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'OPT-002-2024', 'name': 'Optical Comparator', 'description': '14" Screen Optical Comparator, 10x/50x lenses', 'calibrated': True, 'location': work_centers[2]},
        {'serial_number': 'SUR-003-2024', 'name': 'Surface Roughness Tester', 'description': 'Portable surface roughness tester, Ra/Rz/Rq parameters', 'calibrated': True, 'location': work_centers[2]},
        
        # Additional Precision Tools
        {'serial_number': 'GAU-101-2024', 'name': 'Thread Gauge Set', 'description': 'Metric thread pitch gauges, 0.4-6.0mm pitch', 'calibrated': True, 'location': work_centers[11]},
        {'serial_number': 'RAD-102-2024', 'name': 'Radius Gauge Set', 'description': 'Radius gauges, 0.5-15mm concave/convex', 'calibrated': True, 'location': work_centers[11]},
        {'serial_number': 'ANG-103-2024', 'name': 'Angle Blocks', 'description': 'Precision angle blocks, 1-30° in 1° steps', 'calibrated': True, 'location': work_centers[11]},
        {'serial_number': 'SQU-104-2024', 'name': 'Precision Square Set', 'description': 'Hardened steel squares, 2", 4", 6", DIN 875 Grade 0', 'calibrated': True, 'location': work_centers[11]},
        
        # Environmental Monitoring
        {'serial_number': 'HUM-001-2024', 'name': 'Humidity Monitor', 'description': 'Digital humidity/temperature monitor, ±2%RH accuracy', 'calibrated': True, 'location': work_centers[14]},  # OFFICE
        {'serial_number': 'AIR-002-2024', 'name': 'Air Quality Monitor', 'description': 'Particle counter, 0.3-10μm, data logging capability', 'calibrated': True, 'location': work_centers[13]},  # R&D
        
        # Shipping and Packaging
        {'serial_number': 'SCA-001-2024', 'name': 'Precision Scale', 'description': 'Industrial scale, 100kg capacity, 1g resolution', 'calibrated': True, 'location': work_centers[9]},  # SHIPPING
        {'serial_number': 'PAC-002-2024', 'name': 'Heat Sealer', 'description': 'Impulse heat sealer, adjustable time/temperature', 'calibrated': False, 'location': work_centers[9]}
    ]
    
    tools = []
    for tool_data in tools_data:
        tool = Tool.objects.create(**tool_data)
        tools.append(tool)
        cal_status = "📏 CAL" if tool.calibrated else "🔧 TOOL"
        print(f"  ➕ {cal_status} {tool.serial_number}: {tool.name} → {tool.location.name}")
    
    print(f"✅ Created {len(tools)} tools")
    return tools

def create_tool_measures(tools):
    """Create calibration and measurement records"""
    print("📏 Creating tool measurement records...")
    
    calibrated_tools = [tool for tool in tools if tool.calibrated]
    measures = []
    
    for tool in calibrated_tools[:20]:  # Create measures for first 20 calibrated tools
        # Create recent calibration record
        recent_date = datetime.now() - timedelta(days=random.randint(30, 180))
        measure = ToolMeasure.objects.create(
            tool=tool,
            measurement_date=recent_date,
            measured_value=Decimal(f"{random.uniform(0.0001, 25.5000):.4f}"),
            standard_value=Decimal(f"{random.uniform(0.0001, 25.5000):.4f}"),
            tolerance=Decimal(f"{random.uniform(0.0001, 0.0050):.4f}"),
            notes=f"Calibration verified against NIST traceable standards. Temperature: {random.randint(68, 72)}°F, Humidity: {random.randint(45, 55)}%RH"
        )
        measures.append(measure)
        print(f"  📊 Calibration record: {tool.serial_number} - {measure.measurement_date.strftime('%Y-%m-%d')}")
    
    print(f"✅ Created {len(measures)} measurement records")
    return measures

def create_realistic_checkouts(tools, employees):
    """Create realistic tool checkout scenarios"""
    print("📋 Creating tool checkout records...")
    
    available_tools = [tool for tool in tools if not tool.calibrated or random.choice([True, False])]
    checkouts = []
    
    # Create some current checkouts
    for _ in range(8):
        tool = random.choice(available_tools)
        employee = random.choice(employees)
        checkout_date = datetime.now() - timedelta(days=random.randint(1, 14))
        promise_date = checkout_date + timedelta(days=random.randint(1, 7))
        
        checkout = ToolTransaction.objects.create(
            tool=tool,
            employee=employee,
            checkout_date=checkout_date,
            promise_return_date=promise_date.date(),
            from_location=tool.location,
            to_location=tool.location,  # Simplified for demo
            status='CHECKED_OUT',
            notes=f"Checked out for {random.choice(['maintenance', 'calibration', 'setup', 'inspection', 'repair'])}"
        )
        checkouts.append(checkout)
        print(f"  🔄 Active checkout: {tool.serial_number} → {employee.first_name} {employee.last_name}")
    
    # Create some returned tools
    for _ in range(12):
        tool = random.choice(available_tools)
        employee = random.choice(employees)
        checkout_date = datetime.now() - timedelta(days=random.randint(15, 90))
        promise_date = checkout_date + timedelta(days=random.randint(1, 7))
        return_date = checkout_date + timedelta(days=random.randint(1, 10))
        
        checkout = ToolTransaction.objects.create(
            tool=tool,
            employee=employee,
            checkout_date=checkout_date,
            promise_return_date=promise_date.date(),
            return_date=return_date,
            from_location=tool.location,
            to_location=tool.location,  # Simplified for demo
            status='RETURNED',
            notes=f"Returned after {random.choice(['successful repair', 'calibration complete', 'project finished', 'routine maintenance'])}"
        )
        checkouts.append(checkout)
    
    print(f"✅ Created {len(checkouts)} checkout records")
    return checkouts

def main():
    """Main execution function"""
    print("TOYO TANSO USA COMPREHENSIVE DEMO DATA POPULATION")
    print("=" * 60)
    print("Populating Django Tool Management System with extensive realistic manufacturing data")
    print("Based on patterns from legacy Tool_Tracking VB/.NET system")
    print()
    
    try:
        # Clear existing data
        clear_existing_data()
        print()
        
        # Create all data
        work_centers = create_work_centers()
        print()
        
        employees = create_employees()
        print()
        
        tools = create_comprehensive_tools(work_centers)
        print()
        
        measures = create_tool_measures(tools)
        print()
        
        checkouts = create_realistic_checkouts(tools, employees)
        print()
        
        # Summary
        print("📊 POPULATION COMPLETE - SUMMARY")
        print("=" * 40)
        print(f"🏭 Work Centers: {len(work_centers)}")
        print(f"👥 Employees: {len(employees)}")
        print(f"🔧 Tools: {len(tools)}")
        print(f"📏 Calibration Records: {len(measures)}")
        print(f"📋 Checkout Records: {len(checkouts)}")
        print()
        print("🎯 System ready for comprehensive manufacturing demo!")
        print("🌐 Access the application at http://localhost:8000")
        
    except Exception as e:
        print(f"❌ Error during population: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()