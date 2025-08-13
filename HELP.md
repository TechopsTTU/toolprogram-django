# HELP: Toyo Tanso USA Tool Management System

## Table of Contents
1. [System Overview](#system-overview)
2. [Getting Started](#getting-started)
3. [Core Features](#core-features)
4. [User Interface Guide](#user-interface-guide)
5. [API Documentation](#api-documentation)
6. [Database Management](#database-management)
7. [Administration](#administration)
8. [Troubleshooting](#troubleshooting)
9. [Advanced Features](#advanced-features)

---

## System Overview

### What Is This Application?

The **Toyo Tanso USA Tool Management System** is a comprehensive Django-based web application designed specifically for manufacturing environments. Built for Toyo Tanso USA, Inc., this system provides complete tool inventory management, employee tracking, and work center organization capabilities.

### Who Should Use This System?

- **Manufacturing Managers**: Track tool inventory, monitor calibration schedules, and optimize tool allocation
- **Shop Floor Supervisors**: Assign tools to work centers, check tool availability, and manage daily operations
- **Quality Assurance**: Monitor calibration status, track tool history, and ensure compliance
- **IT Administrators**: Manage user accounts, configure system settings, and maintain data integrity
- **External Systems**: Integrate via REST API for automated tool management

### Key Business Benefits

- **Inventory Control**: Real-time tracking of 12+ professional manufacturing tools with unique serial numbers
- **Compliance Management**: Automated calibration tracking and status monitoring
- **Operational Efficiency**: Quick tool assignment, location tracking, and availability checks
- **Data Integrity**: Comprehensive validation, unique constraints, and audit trails
- **Integration Ready**: Full REST API for external system integration

---

## Getting Started

### System Requirements

- **Development**: Windows/Mac/Linux with Python 3.8+
- **Database**: SQLite (development) or Pervasive SQL (production)
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)
- **Network**: Intranet access for multi-user deployment

### Quick Start Guide

#### 1. Access the Application

**Web Interface:**
- Open your web browser
- Navigate to: `http://localhost:8000` (development) or your configured server URL
- You'll see the Toyo Tanso USA branded landing page

**First-Time Setup:**
- Contact your system administrator for login credentials
- Default admin account may be available for initial configuration

#### 2. Navigation Overview

The system provides multiple access methods:
- **Landing Page**: Overview dashboard with quick access links
- **Admin Interface**: Complete administrative control at `/admin/`
- **API Endpoints**: RESTful API access for programmatic integration
- **Direct URLs**: Direct access to specific tool, employee, or work center views

#### 3. Basic Operations

**View Tools:**
- Visit `/tools/` to see all tools in the system
- Click individual tools for detailed information
- Use filters to find specific tools by status or location

**Manage Employees:**
- Access `/employees/` for employee directory
- View contact information and department assignments
- Track which employees are associated with which tools

**Work Center Management:**
- Navigate to `/workcenters/` for facility overview
- See tool assignments per work center
- Monitor work center capacity and utilization

---

## Core Features

### Tool Management

#### Tool Inventory System
- **Unique Serial Numbers**: Every tool has a unique identifier (e.g., "T001", "T002")
- **Professional Tools**: Precision measurement equipment including:
  - Digital Calipers (Mitutoyo, Starrett)
  - Micrometers (Mitutoyo, Brown & Sharpe)
  - Height Gauges, Surface Plates, Go/No-Go Gauges
  - CMM Probes, Thread Gauges, Pin Gauges

#### Tool Properties and Status
- **Availability Status**: `is_available` property shows real-time availability
- **Calibration Tracking**: `calibration_status` monitors due dates and compliance
- **Location Assignment**: Tools can be assigned to specific work centers
- **Check-in/Check-out**: Built-in methods for tool movement tracking

#### Tool Operations
```python
# Available tool operations:
tool.check_in()                    # Return tool to inventory
tool.assign_to_location(workcenter) # Assign to specific work center
tool.is_available                  # Check availability status
tool.calibration_status           # View calibration information
```

### Employee Management

#### Employee Database
- **Unique Employee Numbers**: Format "EMP-XXX" (e.g., "EMP-001")
- **Corporate Email Integration**: All employees use @toyotanso.com domain
- **Department Organization**: Engineering, Quality, Manufacturing, IT, etc.
- **Comprehensive Contact Info**: Names, emails, phone numbers, departments

#### Employee Features
- **Auto-populated Data**: 11 realistic employee profiles included
- **Validation Systems**: Employee number format validation
- **Integration Ready**: Links with tool assignment and work center management

### Work Center Management

#### Manufacturing Floor Organization
- **5 Professional Work Centers**: Machining, Assembly, Inspection, R&D, Shipping
- **Tool Capacity Tracking**: Monitor tool assignments per location
- **Realistic Descriptions**: Detailed work center capabilities and purposes
- **Tool Counting**: Built-in properties to track tool quantities

#### Work Center Operations
```python
# Work center capabilities:
workcenter.get_calibrated_tools()    # Find calibrated tools only
workcenter.tool_count               # Total tools assigned
workcenter.available_tool_count     # Available tools only
```

---

## User Interface Guide

### Landing Page

The landing page serves as your system dashboard:

**Header Section:**
- Toyo Tanso USA corporate logo and branding
- Professional gradient design matching corporate identity
- Mobile-responsive layout for tablet/phone access

**Quick Access Links:**
- **Tools**: Direct access to tool inventory management
- **Employees**: Employee directory and management
- **Work Centers**: Manufacturing floor organization
- **Admin**: Administrative control panel (admin users only)

**System Information:**
- Real-time database status indicator
- Active user count and system health metrics
- Quick statistics on total tools, employees, and work centers

### Tool Management Interface

#### Tool List View (`/tools/`)
- **Grid Layout**: Visual representation of all tools
- **Status Indicators**: Color-coded availability status
- **Filter Options**: Filter by availability, calibration status, location
- **Sort Controls**: Sort by serial number, name, calibration date

#### Tool Detail View (`/tools/<id>/`)
- **Complete Tool Information**: Serial number, specifications, description
- **Current Status**: Availability, location, calibration status
- **Action Buttons**: Check in/out, assign to location, update calibration
- **History Tracking**: Previous assignments and status changes

#### Tool Search and Filtering
- **Text Search**: Find tools by name, serial number, or description
- **Status Filters**: Available, checked out, calibration due
- **Location Filters**: Filter by assigned work center
- **Quick Actions**: Bulk operations for multiple tools

### Employee Directory Interface

#### Employee List View (`/employees/`)
- **Professional Directory**: Complete employee listings
- **Contact Information**: Email, phone, department
- **Search Functionality**: Find employees by name or department
- **Department Grouping**: Organize by business unit

#### Employee Detail View (`/employees/<id>/`)
- **Complete Profile**: Full contact and organizational information
- **Tool Assignments**: Tools currently assigned to employee
- **Work Center Associations**: Primary work locations
- **Communication Tools**: Direct email links, phone numbers

### Work Center Management Interface

#### Work Center Overview (`/workcenters/`)
- **Facility Layout**: Visual representation of manufacturing floor
- **Capacity Indicators**: Tool assignments and availability per center
- **Quick Stats**: Tool counts, utilization rates, staff assignments
- **Status Overview**: Operational status of each work center

#### Work Center Detail View (`/workcenters/<id>/`)
- **Detailed Information**: Work center capabilities and equipment
- **Tool Inventory**: All tools assigned to this location
- **Staff Directory**: Employees primarily working in this area
- **Utilization Metrics**: Usage statistics and efficiency indicators

---

## API Documentation

### REST API Overview

The system provides a complete RESTful API for external integration:

**Base URL**: `http://your-server:8000/api/`

**Authentication**: Session-based authentication (expandable to token-based)

**Response Format**: JSON with comprehensive error handling

### API Endpoints

#### Tools API (`/api/tools/`)

**List All Tools**
```http
GET /api/tools/
Response: Array of tool objects with full details
```

**Get Specific Tool**
```http
GET /api/tools/{id}/
Response: Complete tool information including status
```

**Create New Tool**
```http
POST /api/tools/
Body: {
  "name": "Digital Caliper",
  "serial_number": "T013",
  "description": "6-inch digital caliper",
  "calibrated": true,
  "location": 1
}
```

**Update Tool**
```http
PUT/PATCH /api/tools/{id}/
Body: Fields to update
```

**Delete Tool**
```http
DELETE /api/tools/{id}/
Response: 204 No Content on success
```

**Custom Action: Assign to Work Center**
```http
POST /api/tools/{id}/assign_to_workcenter/
Body: {"workcenter_id": 2}
Response: Updated tool information
```

#### Employees API (`/api/employees/`)

**List All Employees**
```http
GET /api/employees/
Response: Array of employee objects
```

**Get Employee Details**
```http
GET /api/employees/{id}/
Response: Complete employee profile
```

**Create New Employee**
```http
POST /api/employees/
Body: {
  "employee_number": "EMP-012",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@toyotanso.com",
  "phone": "555-0123",
  "department": "Engineering"
}
```

#### Work Centers API (`/api/workcenters/`)

**List All Work Centers**
```http
GET /api/workcenters/
Response: Array of work center objects with tool counts
```

**Get Work Center Details**
```http
GET /api/workcenters/{id}/
Response: Complete work center information and assigned tools
```

### Database Status API

**System Health Check**
```http
GET /api/db-status/
Response: {
  "database_type": "sqlite",
  "status": "connected",
  "total_tools": 12,
  "total_employees": 11,
  "total_workcenters": 5
}
```

### API Integration Examples

#### Python Integration
```python
import requests

# Get all tools
response = requests.get('http://localhost:8000/api/tools/')
tools = response.json()

# Assign tool to work center
assign_data = {"workcenter_id": 2}
response = requests.post(
    'http://localhost:8000/api/tools/1/assign_to_workcenter/',
    json=assign_data
)
```

#### JavaScript Integration
```javascript
// Fetch tool data
fetch('/api/tools/')
  .then(response => response.json())
  .then(tools => {
    console.log('Available tools:', tools);
  });

// Create new employee
fetch('/api/employees/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': getCsrfToken()
  },
  body: JSON.stringify({
    'employee_number': 'EMP-015',
    'first_name': 'Jane',
    'last_name': 'Smith',
    'email': 'jane.smith@toyotanso.com',
    'department': 'Quality'
  })
})
.then(response => response.json())
.then(employee => console.log('Created:', employee));
```

---

## Database Management

### Database Architecture

The system supports dual database environments:

#### Development Environment (SQLite)
- **File**: Local SQLite database file
- **Performance**: Optimized for single-user development
- **Setup**: Automatic with Django migrations
- **Backup**: Simple file copy operations

#### Production Environment (Pervasive SQL)
- **Connection**: ODBC-based Pervasive SQL integration
- **Performance**: Multi-user, high-performance manufacturing environment
- **Setup**: Requires Pervasive ODBC driver configuration
- **Backup**: Enterprise-grade backup systems

### Environment Management

#### Switch Database Environment
```bash
# Switch to local SQLite (development)
python switch_database.py local

# Switch to production Pervasive SQL
python switch_database.py production
```

#### Test Database Connection
```bash
# Test Pervasive connection
python test_pervasive_connection.py

# Django database validation
python manage.py check
python manage.py check --deploy
```

### Data Population

#### Populate Realistic Data
```bash
# Recommended: Enhanced realistic manufacturing data
python populate_enhanced_simple.py

# Creates:
# - 12 Professional manufacturing tools
# - 11 Employee profiles with @toyotanso.com emails
# - 5 Work centers with realistic descriptions
```

#### Alternative Data Scripts
```bash
# Original realistic data set
python populate_realistic_data.py

# Basic development seed data
python seed.py
```

### Migration Management

#### Apply Database Migrations
```bash
# Apply all pending migrations
python manage.py migrate

# Create new migrations after model changes
python manage.py makemigrations

# Show migration status
python manage.py showmigrations
```

#### Migration Strategy
- **Development**: Always test migrations on SQLite first
- **Production**: Schedule migrations during maintenance windows
- **Backup**: Always backup before applying production migrations
- **Rollback**: Keep rollback scripts for critical migrations

---

## Administration

### Admin Interface Overview

Access the Django admin interface at `/admin/` with administrator credentials.

#### Admin Capabilities

**Tool Management:**
- Add/Edit/Delete tools with full validation
- Bulk operations for multiple tools
- Advanced filtering and search
- Export data to CSV/Excel formats

**Employee Administration:**
- Complete employee lifecycle management
- Department organization and reporting
- Contact information maintenance
- User account linking (if implemented)

**Work Center Configuration:**
- Work center setup and modification
- Tool assignment management
- Capacity planning and optimization
- Reporting and analytics

#### Admin User Management

**Create Admin User:**
```bash
python manage.py createsuperuser
```

**Admin Permissions:**
- **Superuser**: Complete system access
- **Staff**: Admin interface access with limited permissions
- **Group-based**: Assign permissions by department/role

#### Bulk Operations

**Data Import:**
- CSV import for tools, employees, work centers
- Validation and error reporting
- Duplicate detection and handling

**Data Export:**
- Full system exports for backup
- Filtered exports for reporting
- Multiple format support (CSV, Excel, JSON)

### System Configuration

#### Environment Variables
```bash
# Critical settings
DATABASE_ENV=local          # or 'production'
SECRET_KEY=your-secret-key
DEBUG=False                 # True for development only
ALLOWED_HOSTS=localhost,your-domain.com
```

#### Production Settings
```python
# Key production configurations
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

### Security Management

#### User Authentication
- Django's built-in authentication system
- Password complexity requirements
- Session management and timeouts
- Failed login attempt monitoring

#### Data Protection
- SQL injection prevention via Django ORM
- Cross-site scripting (XSS) protection
- Cross-site request forgery (CSRF) tokens
- Input validation and sanitization

#### Access Control
- Role-based permissions
- Object-level security
- API access controls
- Admin interface restrictions

---

## Troubleshooting

### Common Issues and Solutions

#### Database Connection Problems

**Issue: Pervasive SQL Connection Failed**
```
Error: Missing '=' in connection string
```
**Solution:**
1. Check Pervasive ODBC driver installation (64-bit required)
2. Verify connection string in `.env.production`
3. Test with: `python test_pervasive_connection.py`
4. System will automatically fall back to SQLite

**Issue: SQLite Database Locked**
```
Error: database is locked
```
**Solution:**
1. Stop all Django processes: `Ctrl+C`
2. Wait 30 seconds for connections to close
3. Restart development server
4. If persistent, delete `db.sqlite3` and run migrations

#### Testing Problems

**Issue: Tests Failing with Import Errors**
```
ModuleNotFoundError: No module named 'tests'
```
**Solution:**
1. Ensure you're in project root directory
2. Run tests with: `python manage.py test tests.test_sanity`
3. Check Python path and virtual environment activation

**Issue: Smoke Tests Failing**
```
Some functionality tests are failing
```
**Solution:**
1. Run individual test suites to isolate issues
2. Use SQLite environment for testing: `python switch_database.py local`
3. Review test output for specific error messages

#### Web Interface Issues

**Issue: Static Files Not Loading**
```
CSS/Images not displaying correctly
```
**Solution:**
1. Run: `python manage.py collectstatic`
2. Verify `STATIC_URL` and `STATIC_ROOT` in settings
3. For development: `python manage.py runserver --insecure`

**Issue: Admin Interface Permissions**
```
Permission denied in admin
```
**Solution:**
1. Verify superuser status: `python manage.py shell`
2. Check user permissions in admin interface
3. Recreate superuser if necessary

### Performance Troubleshooting

#### Database Performance
- **Issue**: Slow query responses
- **Solution**: Add database indexes, optimize queries, consider database tuning

#### Memory Usage
- **Issue**: High memory consumption
- **Solution**: Monitor Django debug toolbar, optimize querysets, implement caching

#### Network Issues
- **Issue**: API timeouts
- **Solution**: Check network connectivity, increase timeout values, implement retry logic

### Log Analysis

#### Django Logs
```bash
# Enable logging in settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'toolprogram.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

#### Error Monitoring
- Review Django error logs
- Monitor API response codes
- Track database connection issues
- Analyze user access patterns

### Getting Help

#### Internal Support
1. Check this HELP document first
2. Review CLAUDE.md for technical details
3. Examine test outputs for specific errors
4. Consult Django documentation

#### External Resources
- **Django Documentation**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **Pervasive SQL**: Check vendor documentation
- **Python Issues**: https://stackoverflow.com/questions/tagged/python

---

## Advanced Features

### Business Logic Integration

#### Custom Model Methods
The system includes sophisticated business logic built into the models:

**Tool Business Logic:**
```python
# Smart availability checking
if tool.is_available:
    tool.assign_to_location(target_workcenter)

# Calibration management
if tool.calibration_status == 'due':
    schedule_calibration(tool)

# Automated check-in process
tool.check_in()  # Handles location reset and status updates
```

**Work Center Intelligence:**
```python
# Advanced tool management
calibrated_tools = workcenter.get_calibrated_tools()
available_count = workcenter.available_tool_count
capacity_utilization = workcenter.calculate_utilization()
```

### Data Validation and Integrity

#### Automatic Validation
- **Unique Constraints**: Serial numbers, employee numbers, work center names
- **Format Validation**: Employee number format (EMP-XXX)
- **Email Validation**: Corporate domain enforcement (@toyotanso.com)
- **Data Consistency**: Foreign key constraints with proper cascade handling

#### Business Rules Enforcement
- Tools cannot be assigned to multiple locations simultaneously
- Employee numbers must follow corporate format
- Calibration dates must be logical (not in future beyond reasonable limits)
- Serial numbers must be unique across the entire system

### Integration Capabilities

#### External System Integration
The API supports integration with:
- **ERP Systems**: Real-time inventory synchronization
- **Quality Management**: Calibration scheduling and compliance
- **Manufacturing Execution**: Tool assignment and tracking
- **Reporting Systems**: Data extraction for analytics

#### Custom Extensions
```python
# Example: Custom tool assignment workflow
class CustomToolAssignment:
    def assign_with_notification(self, tool, workcenter, user):
        # Validate assignment
        if not tool.is_available:
            raise ValidationError("Tool not available")
        
        # Perform assignment
        tool.assign_to_location(workcenter)
        
        # Send notifications
        notify_supervisor(workcenter, tool, user)
        update_scheduling_system(tool, workcenter)
```

### Reporting and Analytics

#### Built-in Reporting
- Tool utilization reports
- Calibration compliance dashboards
- Work center efficiency metrics
- Employee tool assignment history

#### Custom Report Development
```python
# Example: Custom utilization report
def generate_utilization_report(date_range):
    tools = Tool.objects.filter(
        assignment_history__date__range=date_range
    )
    
    return {
        'total_tools': tools.count(),
        'utilized_tools': tools.filter(location__isnull=False).count(),
        'calibration_compliance': tools.filter(calibrated=True).count(),
        'by_workcenter': WorkCenter.objects.annotate(
            tool_count=Count('tools')
        )
    }
```

### Maintenance and Monitoring

#### System Health Monitoring
```bash
# Regular maintenance commands
python manage.py check --deploy  # Production readiness
python manage.py dbshell         # Direct database access
python manage.py shell           # Django shell for debugging
```

#### Performance Monitoring
- Database query analysis
- Response time tracking
- Memory usage monitoring
- User activity logging

#### Backup Strategies
```bash
# SQLite backup
cp db.sqlite3 backups/db_$(date +%Y%m%d).sqlite3

# Data export backup
python manage.py dumpdata > backup_$(date +%Y%m%d).json

# Selective backup
python manage.py dumpdata tools employees workcenters > core_data.json
```

---

## Conclusion

This Tool Management System provides comprehensive manufacturing tool tracking with professional-grade features designed specifically for Toyo Tanso USA's operational needs. The system combines robust data management, intuitive user interfaces, and powerful API integration capabilities to deliver a complete tool management solution.

For additional support or feature requests, consult the technical documentation in `CLAUDE.md` or contact your system administrator.

**System Version**: Django 5.2.4 Tool Management System  
**Last Updated**: August 2025  
**Maintained By**: Toyo Tanso USA IT Department