from django.contrib import admin
from .models import WorkCenter

@admin.register(WorkCenter)
class WorkCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'supervisor', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'location', 'supervisor']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location', 'supervisor')
        }),
        ('Details', {
            'fields': ('description', 'is_active')
        }),
    )
