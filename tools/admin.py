from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'status', 'assigned_to', 'current_location', 'calibrated', 'last_checked_in']
    list_filter = ['status', 'calibrated', 'current_location', 'assigned_to']
    search_fields = ['name', 'serial_number']
    list_editable = ['status', 'calibrated']
    readonly_fields = ['checked_out_date', 'last_checked_in']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'serial_number', 'calibrated')
        }),
        ('Status & Assignment', {
            'fields': ('status', 'assigned_to', 'current_location')
        }),
        ('Dates', {
            'fields': ('due_date', 'checked_out_date', 'last_checked_in'),
            'classes': ('collapse',)
        }),
    )
