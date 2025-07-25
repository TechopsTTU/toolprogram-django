from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter

def home_view(request):
    context = {
        'total_tools': Tool.objects.count(),
        'total_employees': Employee.objects.count(),
        'total_workcenters': WorkCenter.objects.count(),
        'checked_out_tools': Tool.objects.filter(status='checked_out').count(),
    }
    return render(request, 'home.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('tools/', include('tools.urls', namespace='tools')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('workcenters/', include('workcenters.urls', namespace='workcenters')),
]