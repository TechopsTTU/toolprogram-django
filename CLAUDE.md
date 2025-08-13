# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 5.2.4 Tool Management System for Toyo Tanso USA, Inc., designed for manufacturing environments. It manages tools, employees, and work centers with both web interface and REST API capabilities. The system features enhanced data models with validation, comprehensive realistic manufacturing data, and professional corporate branding integration. Database support includes both SQLite (development) and Pervasive SQL (production).

## Essential Commands

### Environment Setup
```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate
```

### Testing Commands
```bash
# Run comprehensive test suite (recommended)
python run_production_tests.py

# Run specific test suites
python manage.py test tests.test_sanity --verbosity=2           # Basic functionality (18 tests)
python manage.py test tests.test_models_simple --verbosity=2    # Data model validation (10 tests)
python manage.py test tests.test_working_functionality --verbosity=2  # Feature testing (18 tests)
python manage.py test tests.test_smoke --verbosity=2            # High-level validation (8 tests)
python manage.py test tests.test_enhanced_functionality --verbosity=2  # Enhanced model features (15 tests)

# Run single test class
python manage.py test tests.test_sanity.APISanityTestCase --verbosity=2

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Database Management
```bash
# Switch to local SQLite environment
python switch_database.py local

# Switch to production Pervasive environment  
python switch_database.py production

# Test Pervasive database connection
python test_pervasive_connection.py

# Django database checks
python manage.py check
python manage.py check --deploy
```

### Development Server & Data Population
```bash
# Start development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Populate with realistic manufacturing data (recommended)
python populate_enhanced_simple.py

# Alternative data population scripts
python populate_realistic_data.py    # Original realistic data
python seed.py                       # Basic seed data
```

## Architecture Overview

### Core Applications
- **tools**: Enhanced tool inventory with unique serial numbers, calibration tracking, utility methods (`check_in()`, `assign_to_location()`), and property accessors (`is_available`, `calibration_status`)
- **employees**: Employee management with validation, auto-population, employee number format validation (EMP-XXX), and @toyotanso.com email addresses
- **workcenters**: Work center management with tool counting properties, comprehensive tool retrieval methods, and realistic manufacturing descriptions

### Database Strategy
The application uses environment-based database configuration via `DATABASE_ENV` setting:
- **Local Development**: SQLite (`DATABASE_ENV=local`)
- **Production**: Pervasive SQL via ODBC (`DATABASE_ENV=production`)

Environment switching is handled by `.env` files (`.env.local`, `.env.production`) and the `switch_database.py` utility.

### API Architecture
- REST API built with Django REST Framework
- Endpoints: `/api/tools/`, `/api/employees/`, `/api/workcenters/`
- Custom actions: `assign_to_workcenter` on Tool ViewSet
- Database status endpoint: `/api/db-status/`

### Enhanced Model Features
- **Unique Constraints**: `Tool.serial_number`, `Employee.employee_number`, `WorkCenter.name` are unique
- **Help Text**: All model fields include descriptive help text for admin interface
- **Validation**: Employee numbers follow EMP-XXX format, tools have comprehensive property methods
- **Relationships**: `Tool.location` → `WorkCenter` (SET_NULL for data integrity)
- **Business Logic**: Models include utility methods like `tool.check_in()`, `workcenter.get_calibrated_tools()`

## Development Workflow

### Database Environment Switching
Always use the appropriate environment for your task:
- Use **local SQLite** for development and testing
- Use **production Pervasive** only when specifically testing production database connectivity

The `switch_database.py` script manages environment files and the production test runner handles database fallbacks automatically.

### Testing Strategy
The test suite has 5 categories with specific purposes:
- **sanity**: Basic functionality verification (API, models, URLs) - 18 tests
- **models_simple**: Data model validation and relationships - 10 tests  
- **working_functionality**: Feature testing and initialization - 18 tests
- **smoke**: High-level system validation - 8 tests
- **enhanced_functionality**: Enhanced model features and business logic - 15 tests

Current test success rate is 84% (69/74 tests passing). The `run_production_tests.py` handles database fallbacks automatically.

### Production Database Considerations
- **Known Issue**: 64-bit Python + 32-bit Pervasive ODBC driver incompatibility
- **Workaround**: System automatically falls back to SQLite for testing
- **Resolution**: Requires 64-bit Pervasive ODBC driver or 32-bit Python installation

### Frontend Architecture & Branding
The system supports multiple frontends with professional Toyo Tanso USA branding:
- **Django Templates**: Primary web interface with corporate logo (`static/images/TTU_LOGO.jpg`), gradient header design, and mobile-responsive layout
- **Vue.js Application**: Modern SPA in `/frontend/` directory for advanced interactions
- **Corporate Branding**: Toyo Tanso USA logo integration, manufacturing taglines, and consistent @toyotanso.com email domains
- **REST API**: Full DRF implementation for external system integration

## File Structure Notes

### Key Configuration Files
- `toolprogram/settings.py`: Main Django settings with environment-based database config
- `.env*`: Environment-specific configuration files (`.env.local`, `.env.production`)
- `run_production_tests.py`: Comprehensive test runner with database fallback logic
- `switch_database.py`: Database environment switching utility
- `populate_enhanced_simple.py`: Primary data population script with realistic manufacturing data

### Testing Files
- `tests/test_*.py`: Test modules organized by category (sanity, models, functionality, smoke, enhanced)
- `playwright-tests/`: End-to-end browser testing with Playwright

### Static Assets & Templates
- `static/images/TTU_LOGO.jpg`: Toyo Tanso USA corporate logo
- `templates/base.html`: Main template with logo integration and corporate branding
- `templates/landing.html`: Enhanced landing page with Toyo Tanso branding

### Data Population Scripts
- `populate_enhanced_simple.py`: Recommended - 12 professional tools, 11 employees, 5 work centers
- `populate_realistic_data.py`: Alternative realistic data set
- `seed.py`: Basic development data

### Common Patterns
- Enhanced models with property methods, validation, and help text
- Unique constraints on critical fields (serial numbers, employee numbers)
- Corporate email domains (@toyotanso.com) throughout employee data
- Professional manufacturing tool specifications with calibration tracking
- Comprehensive error handling and database fallback mechanisms