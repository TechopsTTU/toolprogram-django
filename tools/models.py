from django.db import models
from django.utils import timezone

class Tool(models.Model):
    TOOL_STATUS_CHOICES = [
        ('available', 'Available'),
        ('checked_out', 'Checked Out'),
        ('maintenance', 'In Maintenance'),
        ('calibration', 'In Calibration'),
    ]
    
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    calibrated = models.BooleanField(default=False)
    last_checked_in = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=TOOL_STATUS_CHOICES, default='available')
    assigned_to = models.ForeignKey('employees.Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tools')
    current_location = models.ForeignKey('workcenters.WorkCenter', on_delete=models.SET_NULL, null=True, blank=True, related_name='tools')
    checked_out_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"
    
    def is_overdue(self):
        if self.due_date and self.status == 'checked_out':
            return timezone.now() > self.due_date
        return False
    
    def check_out(self, employee, workcenter=None, due_date=None):
        self.assigned_to = employee
        self.current_location = workcenter
        self.status = 'checked_out'
        self.checked_out_date = timezone.now()
        self.due_date = due_date
        self.save()
    
    def check_in(self, workcenter=None):
        self.assigned_to = None
        self.current_location = workcenter
        self.status = 'available'
        self.last_checked_in = timezone.now()
        self.checked_out_date = None
        self.due_date = None
        self.save()