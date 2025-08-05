#!/usr/bin/env python
"""
Database Environment Switcher

This script helps you switch between different database environments:
- local: SQLite (default for development)
- production: Pervasive database (ERP integration)

Usage:
    python switch_database.py local
    python switch_database.py production
"""

import sys
import os
import shutil
from pathlib import Path


def switch_database_env(environment):
    """Switch to the specified database environment"""
    
    valid_environments = ['local', 'production']
    
    if environment not in valid_environments:
        print(f"Error: '{environment}' is not a valid environment.")
        print(f"Valid options: {', '.join(valid_environments)}")
        return False
    
    # Path to environment files
    base_dir = Path(__file__).parent
    env_file = base_dir / '.env'
    source_file = base_dir / f'.env.{environment}'
    
    # Check if source environment file exists
    if not source_file.exists():
        print(f"Error: Environment file '{source_file}' not found.")
        print("Available environment files:")
        for env_type in valid_environments:
            env_path = base_dir / f'.env.{env_type}'
            if env_path.exists():
                print(f"  [OK] .env.{env_type}")
            else:
                print(f"  [MISSING] .env.{env_type}")
        return False
    
    try:
        # Backup current .env if it exists
        if env_file.exists():
            backup_file = base_dir / '.env.backup'
            shutil.copy2(env_file, backup_file)
            print(f"Backed up current .env to .env.backup")
        
        # Copy the new environment file
        shutil.copy2(source_file, env_file)
        print(f"[SUCCESS] Switched to '{environment}' environment")
        print(f"[SUCCESS] Copied {source_file.name} to .env")
        
        # Display current configuration
        print("\nCurrent database configuration:")
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if 'PASSWORD' in line or 'PASS' in line:
                        key, value = line.split('=', 1)
                        print(f"  {key}={'*' * len(value) if value else ''}")
                    else:
                        print(f"  {line}")
        
        print(f"\nNext steps:")
        print(f"1. Review and update credentials in .env file if needed")
        print(f"2. Test connection: python manage.py test_db_connection")
        print(f"3. Run migrations if needed: python manage.py migrate")
        
        return True
        
    except Exception as e:
        print(f"Error switching environment: {e}")
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python switch_database.py <environment>")
        print("Environments: local, production")
        sys.exit(1)
    
    environment = sys.argv[1].lower()
    
    if switch_database_env(environment):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()