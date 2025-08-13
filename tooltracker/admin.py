from django.contrib import admin
from .models import ToolTransaction


@admin.register(ToolTransaction)
class ToolTransactionAdmin(admin.ModelAdmin):
    list_display = ['tool', 'employee', 'from_location', 'to_location', 'checkout_date', 'status', 'is_overdue']
    list_filter = ['status', 'checkout_date', 'from_location', 'to_location']
    search_fields = ['tool__name', 'tool__serial_number', 'employee__first_name', 'employee__last_name']
    readonly_fields = ['checkout_date', 'return_date']
    ordering = ['-checkout_date']
    
    def is_overdue(self, obj):
        return obj.is_overdue
    is_overdue.boolean = True
    is_overdue.short_description = 'Overdue'
