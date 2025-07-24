from django.db import models
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    primary_workcenter = models.ForeignKey('workcenters.WorkCenter', on_delete=models.SET_NULL, null=True, blank=True, related_name='primary_employees')
    is_active = models.BooleanField(default=True)
    hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
    
    def get_checked_out_tools(self):
        return self.assigned_tools.filter(status='checked_out')
    
    def get_overdue_tools(self):
        return self.assigned_tools.filter(status='checked_out').filter(due_date__lt=timezone.now())

    class Meta:
        ordering = ['name']