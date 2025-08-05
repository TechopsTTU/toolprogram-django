#!/usr/bin/env python
"""
Create Django admin user with default credentials
"""
import os
import sys
import django

# Force local environment
os.environ['DATABASE_ENV'] = 'local'
os.environ['DJANGO_SETTINGS_MODULE'] = 'toolprogram.settings'

# Setup Django
django.setup()

from django.contrib.auth.models import User

def create_admin_user():
    print("Creating Django Admin User")
    print("=" * 30)
    
    # Check if admin user already exists
    if User.objects.filter(username='admin').exists():
        print("Admin user already exists!")
        admin_user = User.objects.get(username='admin')
        print(f"Username: admin")
        print(f"Email: {admin_user.email}")
        print("Updating password to 'tooladmin123'...")
        admin_user.set_password('tooladmin123')
        admin_user.save()
        print("Password updated!")
    else:
        # Create new admin user
        print("Creating new admin user...")
        
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@toolmanagement.com',
            password='tooladmin123'
        )
        
        print("Admin user created successfully!")
    
    print("\nAdmin Login Credentials:")
    print("========================")
    print("Username: admin")
    print("Password: tooladmin123")
    print("Email: admin@toolmanagement.com")
    print("\nAdmin Panel URL:")
    print("http://127.0.0.1:8000/admin/")
    print("\nAdmin Panel Features:")
    print("- Manage all tools, employees, work centers")
    print("- View and edit user accounts")
    print("- Access system logs and data")
    print("- Bulk operations")

if __name__ == '__main__':
    try:
        create_admin_user()
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure to stop the Django server first if it's running.")