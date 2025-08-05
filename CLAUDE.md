# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 5.2.4 Tool Management System designed for manufacturing environments. It manages tools, employees, and work centers with both web interface and REST API capabilities. The system is architected to work with both SQLite (development) and Pervasive SQL (production) databases.

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
# Run all tests
python run_production_tests.py

# Run specific test suites
python manage.py test tests.test_sanity --verbosity=2
python manage.py test tests.test_models_simple --verbosity=2
python manage.py test tests.test_working_functionality --verbosity=2
python manage.py test tests.test_smoke --verbosity=2

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

### Development Server
```bash
# Start development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser
```

## Architecture Overview

### Core Applications
- **tools**: Tool inventory management with calibration tracking and work center assignment
- **employees**: Employee management with department tracking
- **workcenters**: Manufacturing work center management with supervisor tracking

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

### Key Model Relationships
- `Tool.location` → `WorkCenter` (ForeignKey)
- All models implement consistent `__str__` methods and Meta ordering
- Tools track calibration status, location, and check-in timestamps

## Development Workflow

### Database Environment Switching
Always use the appropriate environment for your task:
- Use **local SQLite** for development and testing
- Use **production Pervasive** only when specifically testing production database connectivity

The `switch_database.py` script manages environment files and the production test runner handles database fallbacks automatically.

### Testing Strategy
The test suite has 4 categories with specific purposes:
- **sanity**: Basic functionality verification (API, models, URLs)
- **models**: Data model validation and relationships
- **functionality**: Feature testing and initialization
- **smoke**: High-level system validation

Current test success rate is 75% (3/4 suites passing). Always run tests after changes.

### Production Database Considerations
- **Known Issue**: 64-bit Python + 32-bit Pervasive ODBC driver incompatibility
- **Workaround**: System automatically falls back to SQLite for testing
- **Resolution**: Requires 64-bit Pervasive ODBC driver or 32-bit Python installation

### Frontend Architecture
The system supports multiple frontends:
- **Django Templates**: Primary web interface with Bootstrap styling
- **Vue.js Application**: Modern SPA in `/frontend/` directory
- **REST API**: For integration with external systems

## File Structure Notes

### Key Configuration Files
- `toolprogram/settings.py`: Main Django settings with environment-based database config
- `.env*`: Environment-specific configuration files
- `run_production_tests.py`: Comprehensive test runner with database fallback
- `switch_database.py`: Database environment switching utility

### Testing Files
- `tests/test_*.py`: Test modules organized by category
- `playwright-tests/`: End-to-end browser testing

### Common Patterns
- All apps follow consistent URL patterns: list, detail, create, edit, delete
- ViewSets provide both web views and API endpoints
- Template inheritance uses base templates with app-specific overrides
- Models use consistent field naming and validation patterns