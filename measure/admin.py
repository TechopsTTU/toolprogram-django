from django.contrib import admin
from .models import ToolMeasure


@admin.register(ToolMeasure)
class ToolMeasureAdmin(admin.ModelAdmin):
    list_display = ['tool', 'employee', 'work_center', 'size_measured', 'condition', 'measurement_date', 'is_within_tolerance']
    list_filter = ['condition', 'measurement_date', 'work_center', 'tool']
    search_fields = ['tool__name', 'tool__serial_number', 'employee__first_name', 'employee__last_name', 'notes']
    readonly_fields = ['measurement_date']
    ordering = ['-measurement_date']
    
    def is_within_tolerance(self, obj):
        tolerance_result = obj.is_within_tolerance
        if tolerance_result is None:
            return "N/A"
        return tolerance_result
    is_within_tolerance.boolean = True
    is_within_tolerance.short_description = 'Within Tolerance'
