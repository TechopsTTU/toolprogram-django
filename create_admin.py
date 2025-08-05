#!/usr/bin/env python
"""
Create Django admin user for local environment
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
        print("Password: (unchanged)")
        
        change = input("\nDo you want to change the password? (y/n): ")
        if change.lower() == 'y':
            new_password = input("Enter new password (or press Enter for 'admin123'): ")
            if not new_password:
                new_password = 'admin123'
            admin_user.set_password(new_password)
            admin_user.save()
            print(f"Password updated successfully!")
            print(f"Username: admin")
            print(f"Password: {new_password}")
    else:
        # Create new admin user
        print("Creating new admin user...")
        
        password = input("Enter password (or press Enter for 'admin123'): ")
        if not password:
            password = 'admin123'
            
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@toolmanagement.com',
            password=password
        )
        
        print("Admin user created successfully!")
        print(f"Username: admin")
        print(f"Email: admin@toolmanagement.com")
        print(f"Password: {password}")
    
    print("\nYou can now log in to the admin panel at:")
    print("http://127.0.0.1:8000/admin/")
    print("\nAdmin Panel Features:")
    print("- Manage all tools, employees, work centers")
    print("- View and edit user accounts")
    print("- Access system logs")
    print("- Bulk operations on data")

if __name__ == '__main__':
    try:
        create_admin_user()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure the Django server is not running when creating users.")
        print("If you get database errors, check your .env file:")
        print("DATABASE_ENV=local")