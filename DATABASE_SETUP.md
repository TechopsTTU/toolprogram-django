# Database Configuration Guide

This Django application supports two database environments:

## 🗂️ Database Environments

### 1. **Local Development** (SQLite)
- **Environment**: `local` (default)
- **Database**: SQLite file (`db.sqlite3`)
- **Use case**: Local development and testing

### 2. **Production** (Pervasive)
- **Environment**: `production`  
- **Database**: Pervasive SQL (`NdustrOS` on `PLATSRVR`)
- **Use case**: Production environment with ERP integration

## 🚀 Quick Start

### Method 1: Using the Switch Script (Recommended)

```bash
# Switch to local development (SQLite)
python switch_database.py local

# Switch to production (Pervasive)
python switch_database.py production
```

### Method 2: Manual Environment Variables

Set the `DATABASE_ENV` environment variable:

```bash
# Windows
set DATABASE_ENV=production

# Linux/Mac
export DATABASE_ENV=production
```

## 📋 Setup Instructions

### 1. Install Required Packages

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Files

Copy and customize the environment files:

```bash
# For local development
cp .env.local .env

# For production (edit with your credentials)
cp .env.production .env
```

### 3. Update Credentials

Edit the `.env` file with your database credentials:

**For Production (Pervasive):**
```env
DATABASE_ENV=production
NDUSTROS_SERVER=PLATSRVR
NDUSTROS_DB=NdustrOS
NDUSTROS_USER=your_username
NDUSTROS_PASS=your_password
```

### 4. Test Connection

```bash
python manage.py test_db_connection
```

### 5. Run Migrations

```bash
python manage.py migrate
```

## 🔧 Troubleshooting

### Pervasive Issues

**Driver Installation:**
- Install "Pervasive ODBC Client Interface"
- Ensure client version matches server version

**Common Issues:**
- Check server name and port (default: 1583)
- Verify DSN configuration
- Ensure proper network connectivity to ERP server

### Connection Testing

Use the built-in connection test command:

```bash
python manage.py test_db_connection
```

This will:
- Display current configuration
- Test database connectivity
- Provide troubleshooting hints if connection fails

## 🏗️ Database Drivers Required

| Database | Driver | Package |
|----------|--------|---------|
| SQLite | Built-in | Django default |
| Pervasive | Pervasive ODBC | `django-pyodbc-azure` |

## 📁 Environment Files

- `.env.local` - Local SQLite development
- `.env.production` - Production template
- `.env.example` - Example with all options
- `.env` - Active configuration (created by switch script)

## 🔐 Security Notes

- Never commit `.env` files with real credentials
- Keep database credentials secure and rotate regularly
- The `.env` file is already in `.gitignore`

## 🧪 Testing Different Environments

```bash
# Test local SQLite
python switch_database.py local
python manage.py test_db_connection
python manage.py runserver

# Test production Pervasive
python switch_database.py production
python manage.py test_db_connection
python manage.py migrate  
python manage.py runserver
```