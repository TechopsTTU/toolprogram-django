#!/usr/bin/env python
"""
Test Pervasive Database Connection

This script tests direct connection to the Pervasive database
using pyodbc without Django to isolate connection issues.
"""
import pyodbc
from decouple import config

def test_pervasive_connection():
    """Test direct connection to Pervasive database"""
    
    try:
        # Load configuration
        driver = config('NDUSTROS_DRIVER', default='Pervasive ODBC Client Interface')
        server = config('NDUSTROS_SERVER', default='PLATSRVR')
        port = config('NDUSTROS_PORT', default='1583')
        database = config('NDUSTROS_DB', default='NdustrOS')
        username = config('NDUSTROS_USER', default='')
        password = config('NDUSTROS_PASS', default='')
        
        print("Pervasive Database Connection Test")
        print("=" * 50)
        print(f"Driver: {driver}")
        print(f"Server: {server}")
        print(f"Port: {port}")
        print(f"Database: {database}")
        print(f"Username: {username}")
        print(f"Password: {'*' * len(password) if password else '(not set)'}")
        
        # Check if driver is available
        print("\nChecking available ODBC drivers...")
        drivers = [driver for driver in pyodbc.drivers()]
        pervasive_drivers = [d for d in drivers if 'Pervasive' in d]
        
        print(f"Available ODBC drivers: {len(drivers)}")
        print(f"Pervasive drivers found: {pervasive_drivers}")
        
        if not pervasive_drivers:
            print("ERROR: No Pervasive ODBC drivers found!")
            print("Available drivers:")
            for d in sorted(drivers):
                print(f"  - {d}")
            return False
        
        # Try connection with different connection strings
        connection_strings = [
            f"DRIVER={{{driver}}};ServerName={server};Port={port};DBQ={database};UID={username};PWD={password}",
            f"DRIVER={{{driver}}};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}",
            f"DRIVER={{{driver}}};DSN=;ServerName={server};Port={port};DBQ={database};UID={username};PWD={password}",
        ]
        
        for i, conn_str in enumerate(connection_strings, 1):
            print(f"\nAttempt {i}: Testing connection...")
            print(f"Connection string: {conn_str.replace(password, '*' * len(password) if password else '')}")
            
            try:
                conn = pyodbc.connect(conn_str, timeout=10)
                print("SUCCESS: Connected to Pervasive database!")
                
                # Test basic query
                cursor = conn.cursor()
                cursor.execute("SELECT 1 as test_value")
                result = cursor.fetchone()
                print(f"Test query result: {result[0]}")
                
                # Get database info
                try:
                    cursor.execute("SELECT @@VERSION")
                    version = cursor.fetchone()
                    print(f"Database version: {version[0] if version else 'Unknown'}")
                except:
                    print("Could not retrieve database version")
                
                cursor.close()
                conn.close()
                return True
                
            except pyodbc.Error as e:
                print(f"FAILED: {e}")
                continue
            except Exception as e:
                print(f"UNEXPECTED ERROR: {e}")
                continue
        
        print("\nAll connection attempts failed!")
        return False
        
    except Exception as e:
        print(f"SCRIPT ERROR: {e}")
        return False

if __name__ == '__main__':
    success = test_pervasive_connection()
    exit(0 if success else 1)