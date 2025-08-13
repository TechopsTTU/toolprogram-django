#!/usr/bin/env python
"""
Enhanced data population script with comprehensive realistic manufacturing data
Populates all database fields with detailed, realistic information for:
- WorkCenters with detailed manufacturing locations and operations
- Employees with complete contact information and realistic departments
- Tools with comprehensive calibration data, manufacturers, and specifications
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
        {
            'name': 'QC-TEST-01',
            'location': 'Building C - Materials Testing Lab',
            'supervisor': 'Jennifer Liu-Wang',
            'description': 'Materials testing and validation laboratory with Instron universal testing machines, hardness testers, metallurgical microscopes, and non-destructive testing equipment including ultrasonic and dye penetrant inspection capabilities.'
        },
        {
            'name': 'WELD-FAB-01',
            'location': 'Building D - Fabrication Shop (High Bay)',
            'supervisor': 'Robert Martinez-Silva',
            'description': 'Advanced welding and fabrication facility with Miller Dynasty TIG welders, Lincoln Power Wave MIG systems, and automated orbital welding equipment. Certified for aerospace, nuclear, and medical device welding standards including AWS D17.1 and ASME IX.'
        },
        {
            'name': 'TOOL-CRIB-01',
            'location': 'Building A - Central Tool Storage (Basement Level)',
            'supervisor': 'Amanda Thompson-Lee',
            'description': 'Centralized tool management facility with automated dispensing systems, tool life tracking, and comprehensive inventory management. Features climate-controlled precision tool storage, tool presetting capabilities, and 24/7 automated access for production staff.'
        },
        {
            'name': 'MAINT-SHOP-01',
            'location': 'Building E - Maintenance & Repair (Ground Floor)',
            'supervisor': 'Thomas Anderson-Clark',
            'description': 'Comprehensive maintenance facility supporting all production equipment. Features machine rebuild capabilities, hydraulic system repair, electrical troubleshooting stations, and predictive maintenance equipment including vibration analysis and thermal imaging systems.'
        },
        {
            'name': 'HEAT-TREAT-01',
            'location': 'Building F - Heat Treatment (Isolated Wing)',
            'supervisor': 'Lisa Garcia-Johnson',
            'description': 'Heat treatment facility with vacuum furnaces, atmosphere controlled ovens, and rapid cooling systems. Capable of stress relieving, annealing, hardening, and tempering operations. Includes metallurgical lab for heat treatment validation and certification.'
        }
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
        {'employee_number': 'EMP-005', 'first_name': 'Jennifer', 'last_name': 'Park', 'name': 'Jennifer Park', 'employee_id': 'EMP-005', 'department': 'CNC Machining', 'email': 'jennifer.park@toyotanso.com'},
        {'employee_number': 'EMP-006', 'first_name': 'Daniel', 'last_name': 'Thompson', 'name': 'Daniel Thompson', 'employee_id': 'EMP-006', 'department': 'CNC Machining', 'email': 'daniel.thompson@toyotanso.com'},
        
        # Assembly Staff
        {'employee_number': 'EMP-007', 'first_name': 'James', 'last_name': 'Patterson', 'name': 'James Patterson', 'employee_id': 'EMP-007', 'department': 'Assembly Operations', 'email': 'james.patterson@toyotanso.com'},
        {'employee_number': 'EMP-008', 'first_name': 'Maria', 'last_name': 'Gonzalez-Torres', 'name': 'Maria Gonzalez-Torres', 'employee_id': 'EMP-008', 'department': 'Assembly Operations', 'email': 'maria.gonzalez-torres@toyotanso.com'},
        {'employee_number': 'EMP-009', 'first_name': 'David', 'last_name': 'Kim', 'name': 'David Kim', 'employee_id': 'EMP-009', 'department': 'Assembly Operations', 'email': 'david.kim@toyotanso.com'},
        {'employee_number': 'EMP-010', 'first_name': 'Lisa', 'last_name': 'Anderson', 'name': 'Lisa Anderson', 'employee_id': 'EMP-010', 'department': 'Assembly Operations', 'email': 'lisa.anderson@toyotanso.com'},
        {'employee_number': 'EMP-011', 'first_name': 'Carlos', 'last_name': 'Rivera', 'name': 'Carlos Rivera', 'employee_id': 'EMP-011', 'department': 'Assembly Operations', 'email': 'carlos.rivera@toyotanso.com'},
        {'employee_number': 'EMP-012', 'first_name': 'Michelle', 'last_name': 'Wu', 'name': 'Michelle Wu', 'employee_id': 'EMP-012', 'department': 'Assembly Operations', 'email': 'michelle.wu@toyotanso.com'},
        
        # Quality Control Staff
        {'employee_number': 'EMP-013', 'first_name': 'David', 'last_name': 'Kumar', 'name': 'Dr. David Kumar', 'employee_id': 'EMP-013', 'department': 'Quality Assurance', 'email': 'david.kumar@toyotanso.com'},
        {'employee_number': 'EMP-014', 'first_name': 'Jennifer', 'last_name': 'Liu-Wang', 'name': 'Jennifer Liu-Wang', 'employee_id': 'EMP-014', 'department': 'Quality Assurance', 'email': 'jennifer.liu-wang@toyotanso.com'},
        {'employee_number': 'EMP-015', 'first_name': 'Steven', 'last_name': 'Martinez', 'name': 'Steven Martinez', 'employee_id': 'EMP-015', 'department': 'Quality Assurance', 'email': 'steven.martinez@toyotanso.com'},
        {'employee_number': 'EMP-016', 'first_name': 'Rebecca', 'last_name': 'Johnson', 'name': 'Rebecca Johnson', 'employee_id': 'EMP-016', 'department': 'Quality Assurance', 'email': 'rebecca.johnson@toyotanso.com'},
        
        # Welding & Fabrication Staff
        {'employee_number': 'EMP-017', 'first_name': 'Robert', 'last_name': 'Martinez-Silva', 'name': 'Robert Martinez-Silva', 'employee_id': 'EMP-017', 'department': 'Welding & Fabrication', 'email': 'robert.martinez-silva@toyotanso.com'},
        {'employee_number': 'EMP-018', 'first_name': 'Joseph', 'last_name': 'Brown', 'name': 'Joseph Brown', 'employee_id': 'EMP-018', 'department': 'Welding & Fabrication', 'email': 'joseph.brown@toyotanso.com'},
        {'employee_number': 'EMP-019', 'first_name': 'Amanda', 'last_name': 'Garcia', 'name': 'Amanda Garcia', 'employee_id': 'EMP-019', 'department': 'Welding & Fabrication', 'email': 'amanda.garcia@toyotanso.com'},
        {'employee_number': 'EMP-020', 'first_name': 'Ryan', 'last_name': 'Lee', 'name': 'Ryan Lee', 'employee_id': 'EMP-020', 'department': 'Welding & Fabrication', 'email': 'ryan.lee@toyotanso.com'},
        
        # Tool Crib Staff
        {'employee_number': 'EMP-021', 'first_name': 'Amanda', 'last_name': 'Thompson-Lee', 'name': 'Amanda Thompson-Lee', 'employee_id': 'EMP-021', 'department': 'Tool Management', 'email': 'amanda.thompson-lee@toyotanso.com'},
        {'employee_number': 'EMP-022', 'first_name': 'Brian', 'last_name': 'Wilson', 'name': 'Brian Wilson', 'employee_id': 'EMP-022', 'department': 'Tool Management', 'email': 'brian.wilson@toyotanso.com'},
        {'employee_number': 'EMP-023', 'first_name': 'Nicole', 'last_name': 'Davis', 'name': 'Nicole Davis', 'employee_id': 'EMP-023', 'department': 'Tool Management', 'email': 'nicole.davis@toyotanso.com'},
        
        # Maintenance Staff
        {'employee_number': 'EMP-024', 'first_name': 'Thomas', 'last_name': 'Anderson-Clark', 'name': 'Thomas Anderson-Clark', 'employee_id': 'EMP-024', 'department': 'Maintenance & Repair', 'email': 'thomas.anderson-clark@toyotanso.com'},
        {'employee_number': 'EMP-025', 'first_name': 'Christopher', 'last_name': 'Miller', 'name': 'Christopher Miller', 'employee_id': 'EMP-025', 'department': 'Maintenance & Repair', 'email': 'christopher.miller@toyotanso.com'},
        {'employee_number': 'EMP-026', 'first_name': 'Patricia', 'last_name': 'Robinson', 'name': 'Patricia Robinson', 'employee_id': 'EMP-026', 'department': 'Maintenance & Repair', 'email': 'patricia.robinson@toyotanso.com'},
        
        # Heat Treatment Staff
        {'employee_number': 'EMP-027', 'first_name': 'Lisa', 'last_name': 'Garcia-Johnson', 'name': 'Lisa Garcia-Johnson', 'employee_id': 'EMP-027', 'department': 'Heat Treatment', 'email': 'lisa.garcia-johnson@toyotanso.com'},
        {'employee_number': 'EMP-028', 'first_name': 'Richard', 'last_name': 'White', 'name': 'Richard White', 'employee_id': 'EMP-028', 'department': 'Heat Treatment', 'email': 'richard.white@toyotanso.com'},
        
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
            print(f"✓ Created Employee: {emp.first_name} {emp.last_name} - {emp.department}")
        else:
            # Update existing with enhanced data
            for key, value in emp_data.items():
                setattr(emp, key, value)
            emp.save()
            print(f"⟳ Updated Employee: {emp.first_name} {emp.last_name} - {emp.department}")
        created_employees.append(emp)
    
    return created_employees

def populate_tools(workcenters):
    """Create comprehensive tool database with detailed specifications and calibration data"""
    
    # Realistic tool manufacturers and their typical products
    tool_catalog = [
        # CNC Machining Tools - Building A
        {
            'name': 'Haas VF-4SS Vertical Machining Center',
            'serial_number': 'HAAS-VF4SS-2019-001',
            'description': 'High-performance vertical machining center with 40" x 20" x 25" travels, 15,000 RPM spindle, and 24-station automatic tool changer. Features Haas CNC control with wireless probing and advanced machining cycles.',
            'calibrated': True,
            'manufacturer': 'Haas Automation',
            'model': 'VF-4SS',
            'purchase_date': '2019-03-15'
        },
        {
            'name': 'Okuma LB3000EX CNC Lathe',
            'serial_number': 'OKUMA-LB3000-2020-002',
            'description': 'High-precision CNC turning center with 12" chuck, 20" maximum turning diameter, live tooling, and sub-spindle. OSP-P300L control with advanced turning and milling capabilities.',
            'calibrated': True,
            'manufacturer': 'Okuma Corporation',
            'model': 'LB3000EX',
            'purchase_date': '2020-07-22'
        },
        {
            'name': 'Mazak Integrex i-400ST Multi-Tasking Center',
            'serial_number': 'MAZAK-I400ST-2021-001',
            'description': 'Multi-axis turning and milling center with done-in-one capability. Features twin spindles, Y-axis machining, and SmoothX CNC control for complex aerospace components.',
            'calibrated': True,
            'manufacturer': 'Mazak Corporation',
            'model': 'Integrex i-400ST',
            'purchase_date': '2021-01-10'
        },
        {
            'name': 'Mitutoyo CRYSTA-Apex S574 CMM',
            'serial_number': 'MITU-APEX-S574-2018-001',
            'description': 'High-accuracy coordinate measuring machine with 500x700x400mm measuring range, TP20 touch probe system, and MCOSMOS measurement software. Housed in temperature-controlled environment.',
            'calibrated': True,
            'manufacturer': 'Mitutoyo Corporation',
            'model': 'CRYSTA-Apex S574',
            'purchase_date': '2018-09-05'
        },
        {
            'name': 'Sandvik Coromant CoroCut QD Tooling System',
            'serial_number': 'SANDVIK-QD-SET-001',
            'description': 'Quick-change turning and grooving tooling system with carbide insert compatibility. Includes tool holders for external turning, internal boring, and cut-off operations.',
            'calibrated': False,
            'manufacturer': 'Sandvik Coromant',
            'model': 'CoroCut QD System',
            'purchase_date': '2022-06-18'
        },
        {
            'name': 'Kennametal Beyond Drive Tool Holders',
            'serial_number': 'KENNA-BD-SET-002',
            'description': 'High-performance milling tool holders with shrink-fit technology for maximum rigidity and precision. Includes various sizes for end mills, face mills, and drilling applications.',
            'calibrated': False,
            'manufacturer': 'Kennametal Inc.',
            'model': 'Beyond Drive Series',
            'purchase_date': '2022-04-12'
        },
        
        # Assembly Tools - Building B
        {
            'name': 'Atlas Copco ETP ST61-25 Electric Torque Wrench',
            'serial_number': 'ATLAS-ST61-25-001',
            'description': 'High-precision electric torque wrench with 10-250 Nm torque range, ±2% accuracy, and data logging capability. Features ergonomic design and angle measurement for critical fastening applications.',
            'calibrated': True,
            'manufacturer': 'Atlas Copco',
            'model': 'ETP ST61-25',
            'purchase_date': '2021-11-30'
        },
        {
            'name': 'Demag KBK Crane System 2-Ton',
            'serial_number': 'DEMAG-KBK-2T-001',
            'description': 'Modular crane system with 2-ton capacity, electric hoist, and precision positioning controls. Features anti-sway technology and wireless remote operation for safe material handling.',
            'calibrated': True,
            'manufacturer': 'Demag Cranes',
            'model': 'KBK-II 2000kg',
            'purchase_date': '2019-08-14'
        },
        {
            'name': 'Southworth LS4-48 Pneumatic Lift Table',
            'serial_number': 'SOUTH-LS4-48-001',
            'description': 'Heavy-duty pneumatic scissor lift table with 4,000 lb capacity, 48" x 96" platform, and 48" maximum lift height. Includes safety velocity fuses and pendant controls.',
            'calibrated': True,
            'manufacturer': 'Southworth Products',
            'model': 'LS4-48',
            'purchase_date': '2020-02-28'
        },
        {
            'name': 'Stanley Bostitch Pneumatic Assembly Tools',
            'serial_number': 'STANLEY-PNEU-SET-001',
            'description': 'Professional pneumatic tool set including impact wrenches, ratchets, and screwdrivers. Features quick-change couplers and ergonomic grips for extended use in assembly operations.',
            'calibrated': False,
            'manufacturer': 'Stanley Bostitch',
            'model': 'Industrial Pro Series',
            'purchase_date': '2021-09-07'
        },
        
        # Quality Control Tools - Building C  
        {
            'name': 'Mitutoyo Absolute Digimatic Calipers 8"',
            'serial_number': 'MITU-CD-8-001',
            'description': 'High-precision digital calipers with 0-8" range, 0.0005" resolution, and absolute linear encoder. Features data output capability and carbide-tipped jaws for durability.',
            'calibrated': True,
            'manufacturer': 'Mitutoyo Corporation',
            'model': '500-196-30',
            'purchase_date': '2021-03-22'
        },
        {
            'name': 'Starrett Micrometer Set 0-4"',
            'serial_number': 'STARR-MIC-SET-001',
            'description': 'Professional micrometer set covering 0-4" range in 1" increments. Features carbide-faced anvils, ratchet stops, and includes setting standards and case.',
            'calibrated': True,
            'manufacturer': 'L.S. Starrett Company',
            'model': 'T436.1XRLZ-4',
            'purchase_date': '2020-05-19'
        },
        {
            'name': 'Brown & Sharpe Tesa-Hite Plus Height Gauge',
            'serial_number': 'BS-TESA-HP-001',
            'description': 'Electronic height gauge with 24" range, 0.00005" resolution, and motorized carriage. Features air bearing for smooth operation and statistical analysis capability.',
            'calibrated': True,
            'manufacturer': 'Brown & Sharpe',
            'model': 'Tesa-Hite Plus 600',
            'purchase_date': '2019-10-08'
        },
        {
            'name': 'Fluke 8845A Precision Multimeter',
            'serial_number': 'FLUKE-8845A-001',
            'description': '6.5-digit precision digital multimeter with dual display, data logging, and statistical functions. Features high accuracy and stability for calibration and testing applications.',
            'calibrated': True,
            'manufacturer': 'Fluke Corporation',
            'model': '8845A',
            'purchase_date': '2022-01-15'
        },
        {
            'name': 'Mahr MarSurf PS10 Surface Roughness Tester',
            'serial_number': 'MAHR-PS10-001',
            'description': 'Portable surface roughness measurement system with skidless probe, 17 surface parameters, and wireless data transfer. Includes measurement standards and carrying case.',
            'calibrated': True,
            'manufacturer': 'Mahr Federal Inc.',
            'model': 'MarSurf PS10',
            'purchase_date': '2021-07-03'
        },
        
        # Welding Tools - Building D
        {
            'name': 'Miller Dynasty 350 TIG Welder',
            'serial_number': 'MILLER-DYN350-001',
            'description': 'Advanced AC/DC TIG welding system with 350A output, Dynasty waveform control, and wireless foot control. Features auto line voltage and advanced arc starting for precision welding.',
            'calibrated': True,
            'manufacturer': 'Miller Electric',
            'model': 'Dynasty 350',
            'purchase_date': '2020-11-12'
        },
        {
            'name': 'Lincoln PowerWave AC/DC 1000SD',
            'serial_number': 'LINCOLN-PW1000-001',
            'description': 'Industrial welding power source with 1000A capability, advanced waveform control, and multi-process capability including stick, TIG, and MIG welding.',
            'calibrated': True,
            'manufacturer': 'Lincoln Electric',
            'model': 'PowerWave AC/DC 1000SD',
            'purchase_date': '2019-04-25'
        },
        {
            'name': 'Hypertherm Powermax125 Plasma System',
            'serial_number': 'HYPER-PM125-001',
            'description': 'High-performance plasma cutting system with 125A output, precision cutting capability up to 2" thick steel, and automated height control for CNC integration.',
            'calibrated': True,
            'manufacturer': 'Hypertherm Inc.',
            'model': 'Powermax125',
            'purchase_date': '2021-08-17'
        },
        {
            'name': '3M Speedglas 9100XXi Welding Helmet',
            'serial_number': '3M-SG-9100-SET-001',
            'description': 'Advanced auto-darkening welding helmet with true color technology, grinding mode, and respiratory protection compatibility. Includes side windows and various shade options.',
            'calibrated': False,
            'manufacturer': '3M Safety',
            'model': 'Speedglas 9100XXi',
            'purchase_date': '2022-02-09'
        },
        
        # Tool Crib Equipment - Building A Basement
        {
            'name': 'Zoller Genius 3s Tool Presetter',
            'serial_number': 'ZOLLER-G3S-001',
            'description': 'High-precision CNC tool presetting machine with automatic measurement, tool data management, and direct machine communication. Features touch-screen operation and database integration.',
            'calibrated': True,
            'manufacturer': 'Zoller Inc.',
            'model': 'Genius 3s',
            'purchase_date': '2020-12-03'
        },
        {
            'name': 'Lista Tool Vending System',
            'serial_number': 'LISTA-TVS-001',
            'description': 'Automated tool dispensing system with 200+ item capacity, employee tracking, and inventory management integration. Features secure access control and real-time reporting.',
            'calibrated': False,
            'manufacturer': 'Lista International',
            'model': 'TVMS-200',
            'purchase_date': '2021-05-14'
        },
        {
            'name': 'Coolant Management System CMS-5000',
            'serial_number': 'CMS-5000-001',
            'description': 'Centralized coolant mixing and distribution system with automatic concentration monitoring, filtration, and temperature control for multiple CNC machines.',
            'calibrated': True,
            'manufacturer': 'Industrial Fluid Systems',
            'model': 'CMS-5000',
            'purchase_date': '2019-12-18'
        },
        
        # Maintenance Tools - Building E
        {
            'name': 'SKF TKSA 71 Shaft Alignment Tool',
            'serial_number': 'SKF-TKSA71-001',
            'description': 'Laser shaft alignment system for precision machinery alignment. Features wireless sensors, thermal growth compensation, and comprehensive reporting capabilities.',
            'calibrated': True,
            'manufacturer': 'SKF Group',
            'model': 'TKSA 71',
            'purchase_date': '2021-10-26'
        },
        {
            'name': 'Fluke 810 Vibration Tester',
            'serial_number': 'FLUKE-810-001',
            'description': 'Advanced vibration meter with diagnostic intelligence for bearing, coupling, belt, and gear fault detection. Features built-in analysis and maintenance recommendations.',
            'calibrated': True,
            'manufacturer': 'Fluke Corporation',
            'Model': '810',
            'purchase_date': '2020-09-11'
        },
        {
            'name': 'FLIR E95 Thermal Imaging Camera',
            'serial_number': 'FLIR-E95-001',
            'description': 'Professional thermal imaging camera with 464x348 resolution, temperature measurement accuracy ±2°C, and WiFi connectivity for real-time reporting.',
            'calibrated': True,
            'manufacturer': 'FLIR Systems',
            'model': 'E95',
            'purchase_date': '2022-03-08'
        },
        {
            'name': 'Proto J6070C Torque Wrench Set',
            'serial_number': 'PROTO-J6070C-001',
            'description': 'Professional torque wrench set covering 10-200 ft-lbs with ±3% accuracy. Includes ratcheting heads, extension bars, and calibration certificates.',
            'calibrated': True,
            'manufacturer': 'Proto Industrial Tools',
            'model': 'J6070C',
            'purchase_date': '2021-06-29'
        },
        
        # Heat Treatment Tools - Building F
        {
            'name': 'Vacuum Furnace VF-4824-HT',
            'serial_number': 'VAC-FURN-4824-001',
            'description': 'High-temperature vacuum furnace with 48"x24"x48" work zone, 2400°F maximum temperature, and automated atmosphere control. Features data logging and recipe management.',
            'calibrated': True,
            'manufacturer': 'Solar Manufacturing',
            'model': 'VF-4824-HT',
            'purchase_date': '2018-11-20'
        },
        {
            'name': 'Lindberg Box Furnace BF51842C',
            'serial_number': 'LIND-BF51842C-001',
            'description': 'Atmosphere controlled heat treatment furnace with 18"x42"x18" chamber, 2100°F maximum temperature, and programmable controller with multiple zones.',
            'calibrated': True,
            'manufacturer': 'Lindberg MPH',
            'model': 'BF51842C',
            'purchase_date': '2019-06-13'
        }
    ]
    
    print("Creating comprehensive tool database...")
    created_tools = []
    
    # Assign tools to appropriate work centers
    wc_assignments = {
        'CNC': [0, 1],     # CNC machines to CNC work centers
        'Assembly': [2, 3], # Assembly tools to assembly work centers  
        'QC': [4, 5],      # Quality tools to QC work centers
        'Welding': [6],    # Welding tools to welding center
        'Tool Crib': [7],  # Tool management to tool crib
        'Maintenance': [8], # Maintenance tools to maintenance center
        'Heat Treatment': [9] # Heat treatment tools to heat treatment center
    }
    
    base_time = timezone.now()
    
    for i, tool_data in enumerate(tool_catalog):
        # Determine work center assignment based on tool type
        if 'CNC' in tool_data['name'] or 'Machining' in tool_data['name'] or 'CMM' in tool_data['name']:
            location = workcenters[random.choice(wc_assignments['CNC'])]
        elif 'Assembly' in tool_data['name'] or 'Crane' in tool_data['name'] or 'Lift' in tool_data['name'] or 'Torque' in tool_data['name']:
            location = workcenters[random.choice(wc_assignments['Assembly'])]
        elif 'Caliper' in tool_data['name'] or 'Micrometer' in tool_data['name'] or 'Height' in tool_data['name'] or 'Multimeter' in tool_data['name'] or 'Roughness' in tool_data['name']:
            location = workcenters[random.choice(wc_assignments['QC'])]
        elif 'Weld' in tool_data['name'] or 'Plasma' in tool_data['name'] or 'TIG' in tool_data['name'] or 'MIG' in tool_data['name']:
            location = workcenters[wc_assignments['Welding'][0]]
        elif 'Tool' in tool_data['name'] or 'Presetter' in tool_data['name'] or 'Vending' in tool_data['name'] or 'Coolant' in tool_data['name']:
            location = workcenters[wc_assignments['Tool Crib'][0]]
        elif 'Alignment' in tool_data['name'] or 'Vibration' in tool_data['name'] or 'Thermal' in tool_data['name'] or 'Torque Wrench' in tool_data['name']:
            location = workcenters[wc_assignments['Maintenance'][0]]
        elif 'Furnace' in tool_data['name'] or 'Heat' in tool_data['name']:
            location = workcenters[wc_assignments['Heat Treatment'][0]]
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
            calibration_status = "✓ Calibrated" if tool.calibrated else "⚠ Requires Calibration"
            checkin_status = f"Last used: {tool.last_checked_in.strftime('%Y-%m-%d %H:%M')}" if tool.last_checked_in else "Never checked in"
            print(f"✓ Created Tool: {tool.name}")
            print(f"   Location: {tool.location.name} | {calibration_status} | {checkin_status}")
        else:
            # Update existing tool with enhanced data
            for key, value in enhanced_tool_data.items():
                setattr(tool, key, value)
            tool.save()
            print(f"⟳ Updated Tool: {tool.name} in {tool.location.name}")
            
    return created_tools

def generate_statistics():
    """Generate comprehensive statistics about the populated data"""
    print("\n" + "="*80)
    print("COMPREHENSIVE DATABASE STATISTICS")
    print("="*80)
    
    # Work Center Statistics
    wc_count = WorkCenter.objects.count()
    print(f"\n📍 WORK CENTERS ({wc_count} total):")
    for wc in WorkCenter.objects.all():
        tool_count = Tool.objects.filter(location=wc).count()
        print(f"   {wc.name}: {tool_count} tools assigned - Supervisor: {wc.supervisor}")
    
    # Employee Statistics  
    emp_count = Employee.objects.count()
    print(f"\n👥 EMPLOYEES ({emp_count} total):")
    departments = Employee.objects.values_list('department', flat=True).distinct()
    for dept in departments:
        dept_count = Employee.objects.filter(department=dept).count()
        print(f"   {dept}: {dept_count} employees")
    
    # Tool Statistics
    tool_count = Tool.objects.count()
    calibrated_count = Tool.objects.filter(calibrated=True).count()
    uncalibrated_count = tool_count - calibrated_count
    
    print(f"\n🔧 TOOLS ({tool_count} total):")
    print(f"   ✓ Calibrated: {calibrated_count} ({calibrated_count/tool_count*100:.1f}%)")
    print(f"   ⚠ Requires Calibration: {uncalibrated_count} ({uncalibrated_count/tool_count*100:.1f}%)")
    
    # Check-in Statistics
    base_time = timezone.now()
    never_checked_in = Tool.objects.filter(last_checked_in__isnull=True).count()
    recent_checkin = Tool.objects.filter(last_checked_in__gte=base_time - timedelta(days=1)).count()
    week_checkin = Tool.objects.filter(last_checked_in__gte=base_time - timedelta(days=7), last_checked_in__lt=base_time - timedelta(days=1)).count()
    month_checkin = Tool.objects.filter(last_checked_in__gte=base_time - timedelta(days=30), last_checked_in__lt=base_time - timedelta(days=7)).count()
    
    print(f"\n📊 TOOL USAGE PATTERNS:")
    print(f"   🔄 Used today: {recent_checkin} tools")
    print(f"   📅 Used this week: {week_checkin} tools") 
    print(f"   📆 Used this month: {month_checkin} tools")
    print(f"   ❌ Never checked in: {never_checked_in} tools")
    
    # Location Distribution
    assigned_tools = Tool.objects.exclude(location__isnull=True).count()
    unassigned_tools = tool_count - assigned_tools
    
    print(f"\n📍 TOOL LOCATIONS:")
    print(f"   ✓ Assigned to work centers: {assigned_tools} ({assigned_tools/tool_count*100:.1f}%)")
    print(f"   ⚠ Unassigned: {unassigned_tools} ({unassigned_tools/tool_count*100:.1f}%)")

def main():
    """Enhanced main function with comprehensive data population"""
    print("="*80)
    print("ENHANCED MANUFACTURING DATA POPULATION SYSTEM")
    print("Comprehensive realistic data for Tool Management System")
    print("="*80)
    
    print("\n🗃️  CLEARING EXISTING DATA...")
    tool_count = Tool.objects.count()
    employee_count = Employee.objects.count() 
    wc_count = WorkCenter.objects.count()
    
    Tool.objects.all().delete()
    Employee.objects.all().delete()
    WorkCenter.objects.all().delete()
    
    print(f"   Cleared {tool_count} tools, {employee_count} employees, {wc_count} work centers")
    
    # Populate in dependency order
    print(f"\n🏭 CREATING WORK CENTERS...")
    workcenters = populate_workcenters()
    
    print(f"\n👥 CREATING EMPLOYEE DATABASE...")
    employees = populate_employees()
    
    print(f"\n🔧 CREATING COMPREHENSIVE TOOL INVENTORY...")
    tools = populate_tools(workcenters)
    
    # Generate comprehensive statistics
    generate_statistics()
    
    print(f"\n✅ POPULATION COMPLETE!")
    print(f"📊 Database now contains realistic manufacturing data suitable for:")
    print(f"   • Production testing and validation")
    print(f"   • User training and demonstrations") 
    print(f"   • System performance evaluation")
    print(f"   • API endpoint testing")
    print("="*80)

if __name__ == '__main__':
    main()