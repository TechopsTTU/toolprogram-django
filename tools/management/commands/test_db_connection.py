from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Test database connection and display current configuration'

    def handle(self, *args, **options):
        self.stdout.write("=== Database Connection Test ===")
        
        # Display current environment
        database_env = os.getenv('DATABASE_ENV', 'local')
        self.stdout.write(f"Current DATABASE_ENV: {database_env}")
        
        # Display database configuration
        db_config = settings.DATABASES['default']
        self.stdout.write(f"Database Engine: {db_config['ENGINE']}")
        
        if database_env == 'local':
            self.stdout.write(f"Database File: {db_config['NAME']}")
        else:
            self.stdout.write(f"Database Host: {db_config.get('HOST', 'N/A')}")
            self.stdout.write(f"Database Name: {db_config.get('NAME', 'N/A')}")
            self.stdout.write(f"Database Port: {db_config.get('PORT', 'N/A')}")
            self.stdout.write(f"Database User: {db_config.get('USER', 'N/A') or 'Windows Auth'}")
        
        # Test connection
        try:
            with connection.cursor() as cursor:
                if database_env == 'local':
                    cursor.execute("SELECT sqlite_version();")
                    version = cursor.fetchone()[0]
                    self.stdout.write(
                        self.style.SUCCESS(f"✓ SQLite connection successful! Version: {version}")
                    )
                elif database_env == 'production':
                    cursor.execute("SELECT CURRENT_DATE;")
                    date = cursor.fetchone()[0]
                    self.stdout.write(
                        self.style.SUCCESS(f"✓ Pervasive connection successful! Current date: {date}")
                    )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"✗ Database connection failed: {str(e)}")
            )
            
            # Provide troubleshooting hints
            if database_env == 'production':
                self.stdout.write("\nTroubleshooting Pervasive:")
                self.stdout.write("- Ensure Pervasive ODBC Client Interface is installed")
                self.stdout.write("- Check if Pervasive server is running and accessible")
                self.stdout.write("- Verify server name, port, database name, and credentials")