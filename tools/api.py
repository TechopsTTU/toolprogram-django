from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError

def check_database_connection(request):
    """
    API endpoint to check database connection status
    Returns a JSON response with connection status
    """
    db_conn = connections['default']
    try:
        # Attempt a simple query to verify connection
        db_conn.cursor()

        # If we get here, connection is successful
        response_data = {
            'status': 'connected',
            'database': db_conn.settings_dict['ENGINE'],
            'name': db_conn.settings_dict['NAME'],
        }

        # Additional info for non-SQLite databases
        if 'sqlite' not in db_conn.settings_dict['ENGINE']:
            response_data.update({
                'host': db_conn.settings_dict['HOST'],
                'port': db_conn.settings_dict['PORT'],
            })

        return JsonResponse(response_data)
    except OperationalError as e:
        # Connection failed
        return JsonResponse({
            'status': 'error',
            'message': str(e),
            'database': db_conn.settings_dict['ENGINE'],
        }, status=500)
