#!/usr/bin/env python
"""
Enhanced data population script with comprehensive realistic manufacturing data
Populates all database fields with detailed, realistic information
"""
import os
import sys
import django
from datetime import datetime, timedelta
import random
from django.utils import timezone

# Setup Django - Force local environment for safety
os.environ['DJANGO_SETTINGS_MODULE'] = 'toolprogram.settings'
os.environ['DATABASE_ENV'] = 'local'
django.setup()

from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter

def populate_workcenters():
    """Create comprehensive work centers with detailed manufacturing information"""
    workcenters_data = [
        {
            'name': 'CNC-MC-01',
            'location': 'Building A - Bay 101 (North Wing)',
            'supervisor': 'Michael Rodriguez',
            'description': 'Primary CNC Machining Center featuring Haas VF-4SS vertical mills, Okuma LB3000EX turning centers, and Mazak Integrex multi-axis machines. Specializes in precision aerospace components, medical device parts, and automotive transmission components with tolerances to ±0.0001". Operates 24/7 with full automation including robot tool changers and pallet systems.'
        },
        {
            'name': 'CNC-MC-02', 
            'location': 'Building A - Bay 102 (North Wing)',
            'supervisor': 'Sarah Chen-Williams',
            'description': 'Secondary CNC Machining Center with DMG Mori NLX series lathes and Makino horizontal machining centers. Focus on high-volume production runs for industrial equipment manufacturers. Features advanced workpiece handling systems and in-process quality monitoring with Renishaw probing systems.'
        },
        {
            'name': 'ASSEMBLY-01',
            'location': 'Building B - Floor 2 (Main Assembly Hall)', 
            'supervisor': 'James Patterson',
            'description': 'Primary assembly line for complex mechanical assemblies including gearboxes, pump systems, and precision instruments. Equipped with pneumatic torque tools, overhead cranes up to 5 tons, and ergonomic workstations. Includes clean room section for sensitive electronic component integration.'
        },
        {
            'name': 'ASSEMBLY-02',
            'location': 'Building B - Floor 3 (Secondary Assembly)',
            'supervisor': 'Maria Gonzalez-Torres',
            'description': 'Secondary assembly line specializing in sub-assemblies and component preparation. Features modular workstations, automated fastener systems, and comprehensive testing equipment. Supports just-in-time delivery to primary assembly lines.'
        },
        {
            'name': 'QC-INSPECT-01',
            'location': 'Building C - Climate Control Lab',
            'supervisor': 'Dr. David Kumar',
            'description': 'Primary quality control laboratory featuring Zeiss coordinate measuring machines, Mitutoyo surface roughness testers, and comprehensive dimensional inspection equipment. Temperature controlled to ±1°F with humidity control. Capable of first article inspections, statistical process control, and failure analysis.'
        },
    ]
    
    print("Creating enhanced work centers...")
    created_wcs = []
    for wc_data in workcenters_data:
        wc, created = WorkCenter.objects.get_or_create(
            name=wc_data['name'],
            defaults=wc_data
        )
        if created:
            print(f"[+] Created WorkCenter: {wc.name} - {wc.supervisor}")
        else:
            # Update existing with enhanced data
            for key, value in wc_data.items():
                setattr(wc, key, value)
            wc.save()
            print(f"[U] Updated WorkCenter: {wc.name} - {wc.supervisor}")
        created_wcs.append(wc)
    
    return created_wcs

def populate_employees():
    """Create comprehensive employee database with full contact information"""
    employees_data = [
        # CNC Machining Staff
        {'employee_number': 'EMP-001', 'first_name': 'Michael', 'last_name': 'Rodriguez', 'name': 'Michael Rodriguez', 'employee_id': 'EMP-001', 'department': 'CNC Machining', 'email': 'michael.rodriguez@toyotanso.com'},
        {'employee_number': 'EMP-002', 'first_name': 'Kevin', 'last_name': 'Chen', 'name': 'Kevin Chen', 'employee_id': 'EMP-002', 'department': 'CNC Machining', 'email': 'kevin.chen@toyotanso.com'},
        {'employee_number': 'EMP-003', 'first_name': 'Sarah', 'last_name': 'Chen-Williams', 'name': 'Sarah Chen-Williams', 'employee_id': 'EMP-003', 'department': 'CNC Machining', 'email': 'sarah.chen-williams@toyotanso.com'},
        {'employee_number': 'EMP-004', 'first_name': 'Roberto', 'last_name': 'Santos', 'name': 'Roberto Santos', 'employee_id': 'EMP-004', 'department': 'CNC Machining', 'email': 'roberto.santos@toyotanso.com'},
        
        # Assembly Staff
        {'employee_number': 'EMP-007', 'first_name': 'James', 'last_name': 'Patterson', 'name': 'James Patterson', 'employee_id': 'EMP-007', 'department': 'Assembly Operations', 'email': 'james.patterson@toyotanso.com'},
        {'employee_number': 'EMP-008', 'first_name': 'Maria', 'last_name': 'Gonzalez-Torres', 'name': 'Maria Gonzalez-Torres', 'employee_id': 'EMP-008', 'department': 'Assembly Operations', 'email': 'maria.gonzalez-torres@toyotanso.com'},
        {'employee_number': 'EMP-009', 'first_name': 'David', 'last_name': 'Kim', 'name': 'David Kim', 'employee_id': 'EMP-009', 'department': 'Assembly Operations', 'email': 'david.kim@toyotanso.com'},
        
        # Quality Control Staff
        {'employee_number': 'EMP-013', 'first_name': 'David', 'last_name': 'Kumar', 'name': 'Dr. David Kumar', 'employee_id': 'EMP-013', 'department': 'Quality Assurance', 'email': 'david.kumar@toyotanso.com'},
        {'employee_number': 'EMP-014', 'first_name': 'Jennifer', 'last_name': 'Liu-Wang', 'name': 'Jennifer Liu-Wang', 'employee_id': 'EMP-014', 'department': 'Quality Assurance', 'email': 'jennifer.liu-wang@toyotanso.com'},
        
        # Management & Engineering
        {'employee_number': 'EMP-029', 'first_name': 'Catherine', 'last_name': 'Moore', 'name': 'Catherine Moore', 'employee_id': 'EMP-029', 'department': 'Manufacturing Engineering', 'email': 'catherine.moore@toyotanso.com'},
        {'employee_number': 'EMP-030', 'first_name': 'Jonathan', 'last_name': 'Taylor', 'name': 'Jonathan Taylor', 'employee_id': 'EMP-030', 'department': 'Production Management', 'email': 'jonathan.taylor@toyotanso.com'},
    ]
    
    print("Creating comprehensive employee database...")
    created_employees = []
    for emp_data in employees_data:
        emp, created = Employee.objects.get_or_create(
            employee_number=emp_data['employee_number'],
            defaults=emp_data
        )
        if created:
            print(f"[+] Created Employee: {emp.first_name} {emp.last_name} - {emp.department}")
        else:
            # Update existing with enhanced data
            for key, value in emp_data.items():
                setattr(emp, key, value)
            emp.save()
            print(f"[U] Updated Employee: {emp.first_name} {emp.last_name} - {emp.department}")
        created_employees.append(emp)
    
    return created_employees

def populate_tools(workcenters):
    """Create comprehensive tool database with detailed specifications and calibration data"""
    
    # Realistic tool catalog
    tool_catalog = [
        # CNC Machining Tools - Building A
        {
            'name': 'Haas VF-4SS Vertical Machining Center',
            'serial_number': 'HAAS-VF4SS-2019-001',
            'description': 'High-performance vertical machining center with 40" x 20" x 25" travels, 15,000 RPM spindle, and 24-station automatic tool changer. Features Haas CNC control with wireless probing and advanced machining cycles.',
            'calibrated': True,
        },
        {
            'name': 'Okuma LB3000EX CNC Lathe',
            'serial_number': 'OKUMA-LB3000-2020-002',
            'description': 'High-precision CNC turning center with 12" chuck, 20" maximum turning diameter, live tooling, and sub-spindle. OSP-P300L control with advanced turning and milling capabilities.',
            'calibrated': True,
        },
        {
            'name': 'Mitutoyo CRYSTA-Apex S574 CMM',
            'serial_number': 'MITU-APEX-S574-2018-001',
            'description': 'High-accuracy coordinate measuring machine with 500x700x400mm measuring range, TP20 touch probe system, and MCOSMOS measurement software. Housed in temperature-controlled environment.',
            'calibrated': True,
        },
        {
            'name': 'Atlas Copco ETP ST61-25 Electric Torque Wrench',
            'serial_number': 'ATLAS-ST61-25-001',
            'description': 'High-precision electric torque wrench with 10-250 Nm torque range, ±2% accuracy, and data logging capability. Features ergonomic design and angle measurement for critical fastening applications.',
            'calibrated': True,
        },
        {
            'name': 'Demag KBK Crane System 2-Ton',
            'serial_number': 'DEMAG-KBK-2T-001',
            'description': 'Modular crane system with 2-ton capacity, electric hoist, and precision positioning controls. Features anti-sway technology and wireless remote operation for safe material handling.',
            'calibrated': True,
        },
        {
            'name': 'Mitutoyo Absolute Digimatic Calipers 8"',
            'serial_number': 'MITU-CD-8-001',
            'description': 'High-precision digital calipers with 0-8" range, 0.0005" resolution, and absolute linear encoder. Features data output capability and carbide-tipped jaws for durability.',
            'calibrated': True,
        },
        {
            'name': 'Starrett Micrometer Set 0-4"',
            'serial_number': 'STARR-MIC-SET-001',
            'description': 'Professional micrometer set covering 0-4" range in 1" increments. Features carbide-faced anvils, ratchet stops, and includes setting standards and case.',
            'calibrated': True,
        },
        {
            'name': 'Miller Dynasty 350 TIG Welder',
            'serial_number': 'MILLER-DYN350-001',
            'description': 'Advanced AC/DC TIG welding system with 350A output, Dynasty waveform control, and wireless foot control. Features auto line voltage and advanced arc starting for precision welding.',
            'calibrated': True,
        },
        {
            'name': 'Fluke 8845A Precision Multimeter',
            'serial_number': 'FLUKE-8845A-001',
            'description': '6.5-digit precision digital multimeter with dual display, data logging, and statistical functions. Features high accuracy and stability for calibration and testing applications.',
            'calibrated': True,
        },
        {
            'name': 'Sandvik Coromant CoroCut QD Tooling System',
            'serial_number': 'SANDVIK-QD-SET-001',
            'description': 'Quick-change turning and grooving tooling system with carbide insert compatibility. Includes tool holders for external turning, internal boring, and cut-off operations.',
            'calibrated': False,
        },
        {
            'name': 'Kennametal Beyond Drive Tool Holders',
            'serial_number': 'KENNA-BD-SET-002',
            'description': 'High-performance milling tool holders with shrink-fit technology for maximum rigidity and precision. Includes various sizes for end mills, face mills, and drilling applications.',
            'calibrated': False,
        },
        {
            'name': 'Stanley Bostitch Pneumatic Assembly Tools',
            'serial_number': 'STANLEY-PNEU-SET-001',
            'description': 'Professional pneumatic tool set including impact wrenches, ratchets, and screwdrivers. Features quick-change couplers and ergonomic grips for extended use in assembly operations.',
            'calibrated': False,
        },
    ]
    
    print("Creating comprehensive tool database...")
    created_tools = []
    
    base_time = timezone.now()
    
    for i, tool_data in enumerate(tool_catalog):
        # Assign tools to work centers based on type
        if 'CNC' in tool_data['name'] or 'Machining' in tool_data['name'] or 'CMM' in tool_data['name']:
            location = workcenters[0]  # CNC center
        elif 'Assembly' in tool_data['name'] or 'Crane' in tool_data['name'] or 'Torque' in tool_data['name']:
            location = workcenters[2]  # Assembly center
        elif 'Caliper' in tool_data['name'] or 'Micrometer' in tool_data['name'] or 'Multimeter' in tool_data['name']:
            location = workcenters[4]  # QC center
        else:
            location = random.choice(workcenters)
        
        # Generate realistic check-in patterns
        check_in_patterns = [
            None,  # Never checked in
            base_time - timedelta(hours=random.randint(1, 8)),      # Recently used (same day)
            base_time - timedelta(days=random.randint(1, 3)),       # Used within last few days
            base_time - timedelta(days=random.randint(4, 14)),      # Used within last 2 weeks
            base_time - timedelta(days=random.randint(15, 30))      # Used within last month
        ]
        
        last_checked_in = random.choice(check_in_patterns)
        
        # Enhanced tool data with all fields populated
        enhanced_tool_data = {
            'name': tool_data['name'],
            'serial_number': tool_data['serial_number'],
            'description': tool_data['description'],
            'calibrated': tool_data['calibrated'],
            'location': location,
            'last_checked_in': last_checked_in
        }
        
        tool, created = Tool.objects.get_or_create(
            serial_number=enhanced_tool_data['serial_number'],
            defaults=enhanced_tool_data
        )
        
        if created:
            created_tools.append(tool)
            calibration_status = "[CAL]" if tool.calibrated else "[UNCAL]"
            checkin_status = f"Last used: {tool.last_checked_in.strftime('%Y-%m-%d %H:%M')}" if tool.last_checked_in else "Never checked in"
            print(f"[+] Created Tool: {tool.name}")
            print(f"   Location: {tool.location.name} | {calibration_status} | {checkin_status}")
        else:
            # Update existing tool with enhanced data
            for key, value in enhanced_tool_data.items():
                setattr(tool, key, value)
            tool.save()
            print(f"[U] Updated Tool: {tool.name} in {tool.location.name}")
            
    return created_tools

def generate_statistics():
    """Generate comprehensive statistics about the populated data"""
    print("\n" + "="*80)
    print("COMPREHENSIVE DATABASE STATISTICS")
    print("="*80)
    
    # Work Center Statistics
    wc_count = WorkCenter.objects.count()
    print(f"\nWORK CENTERS ({wc_count} total):")
    for wc in WorkCenter.objects.all():
        tool_count = Tool.objects.filter(location=wc).count()
        print(f"   {wc.name}: {tool_count} tools assigned - Supervisor: {wc.supervisor}")
    
    # Employee Statistics  
    emp_count = Employee.objects.count()
    print(f"\nEMPLOYEES ({emp_count} total):")
    departments = Employee.objects.values_list('department', flat=True).distinct()
    for dept in departments:
        dept_count = Employee.objects.filter(department=dept).count()
        print(f"   {dept}: {dept_count} employees")
    
    # Tool Statistics
    tool_count = Tool.objects.count()
    calibrated_count = Tool.objects.filter(calibrated=True).count()
    uncalibrated_count = tool_count - calibrated_count
    
    print(f"\nTOOLS ({tool_count} total):")
    print(f"   [CAL] Calibrated: {calibrated_count} ({calibrated_count/tool_count*100:.1f}%)")
    print(f"   [UNCAL] Requires Calibration: {uncalibrated_count} ({uncalibrated_count/tool_count*100:.1f}%)")
    
    # Check-in Statistics
    base_time = timezone.now()
    never_checked_in = Tool.objects.filter(last_checked_in__isnull=True).count()
    recent_checkin = Tool.objects.filter(last_checked_in__gte=base_time - timedelta(days=1)).count()
    week_checkin = Tool.objects.filter(last_checked_in__gte=base_time - timedelta(days=7), last_checked_in__lt=base_time - timedelta(days=1)).count()
    month_checkin = Tool.objects.filter(last_checked_in__gte=base_time - timedelta(days=30), last_checked_in__lt=base_time - timedelta(days=7)).count()
    
    print(f"\nTOOL USAGE PATTERNS:")
    print(f"   [TODAY] Used today: {recent_checkin} tools")
    print(f"   [WEEK] Used this week: {week_checkin} tools") 
    print(f"   [MONTH] Used this month: {month_checkin} tools")
    print(f"   [NEVER] Never checked in: {never_checked_in} tools")
    
    # Location Distribution
    assigned_tools = Tool.objects.exclude(location__isnull=True).count()
    unassigned_tools = tool_count - assigned_tools
    
    print(f"\nTOOL LOCATIONS:")
    print(f"   [ASSIGNED] Assigned to work centers: {assigned_tools} ({assigned_tools/tool_count*100:.1f}%)")
    print(f"   [UNASSIGNED] Unassigned: {unassigned_tools} ({unassigned_tools/tool_count*100:.1f}%)")

def main():
    """Enhanced main function with comprehensive data population"""
    print("="*80)
    print("ENHANCED MANUFACTURING DATA POPULATION SYSTEM")
    print("Comprehensive realistic data for Tool Management System")
    print("="*80)
    
    print("\nCLEARING EXISTING DATA...")
    tool_count = Tool.objects.count()
    employee_count = Employee.objects.count() 
    wc_count = WorkCenter.objects.count()
    
    Tool.objects.all().delete()
    Employee.objects.all().delete()
    WorkCenter.objects.all().delete()
    
    print(f"   Cleared {tool_count} tools, {employee_count} employees, {wc_count} work centers")
    
    # Populate in dependency order
    print(f"\nCREATING WORK CENTERS...")
    workcenters = populate_workcenters()
    
    print(f"\nCREATING EMPLOYEE DATABASE...")
    employees = populate_employees()
    
    print(f"\nCREATING COMPREHENSIVE TOOL INVENTORY...")
    tools = populate_tools(workcenters)
    
    # Generate comprehensive statistics
    generate_statistics()
    
    print(f"\n[SUCCESS] POPULATION COMPLETE!")
    print(f"Database now contains realistic manufacturing data suitable for:")
    print(f"   * Production testing and validation")
    print(f"   * User training and demonstrations") 
    print(f"   * System performance evaluation")
    print(f"   * API endpoint testing")
    print("="*80)

if __name__ == '__main__':
    main()