from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from tools.views import ToolViewSet, landing_page
from employees.views import EmployeeViewSet
from workcenters.views import WorkCenterViewSet

def db_status_view(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({'status': 'connected', 'message': 'Database connection successful'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# Create a main API router
api_router = DefaultRouter()
api_router.register(r'tools', ToolViewSet)
api_router.register(r'employees', EmployeeViewSet)
api_router.register(r'workcenters', WorkCenterViewSet)

urlpatterns = [
    path('', landing_page, name='landing'),
    path('admin/', admin.site.urls),
    path('api/db-status/', db_status_view, name='db-status'),
    path('api/', include(api_router.urls)),
    path('tools/', include('tools.urls', namespace='tools')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('workcenters/', include('workcenters.urls', namespace='workcenters')),
]