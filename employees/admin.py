from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee_id', 'department', 'email', 'primary_workcenter', 'is_active']
    list_filter = ['department', 'is_active', 'primary_workcenter']
    search_fields = ['name', 'employee_id', 'email']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'employee_id', 'email', 'phone')
        }),
        ('Work Information', {
            'fields': ('department', 'primary_workcenter', 'hire_date', 'is_active')
        }),
    )
