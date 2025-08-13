from django.db import models
from django.utils import timezone
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter


class ToolMeasure(models.Model):
    """Model for tool measurement records - matches legacy ToolMeasure functionality"""
    
    CONDITION_CHOICES = [
        ('GOOD', 'Good'),
        ('FAIR', 'Fair'), 
        ('POOR', 'Poor'),
        ('NEEDS_REPAIR', 'Needs Repair'),
    ]
    
    tool = models.ForeignKey(
        Tool,
        on_delete=models.CASCADE,
        help_text="Tool being measured"
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        help_text="Employee performing the measurement"
    )
    work_center = models.ForeignKey(
        WorkCenter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Work center where measurement was performed"
    )
    
    # Measurement date and time
    measurement_date = models.DateTimeField(
        default=timezone.now,
        help_text="Date and time measurement was performed"
    )
    
    # Measurement details
    size_measured = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        help_text="Measured size/dimension"
    )
    expected_size = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        null=True,
        blank=True,
        help_text="Expected/nominal size"
    )
    tolerance = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        null=True,
        blank=True,
        help_text="Acceptable tolerance"
    )
    
    # Condition assessment
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='GOOD',
        help_text="Overall tool condition"
    )
    
    # Additional details
    notes = models.TextField(
        blank=True,
        help_text="Additional notes about the measurement"
    )
    
    class Meta:
        ordering = ['-measurement_date']
        verbose_name = "Tool Measure"
        verbose_name_plural = "Tool Measures"
        
    def __str__(self):
        return f"{self.tool.name} - {self.measurement_date.strftime('%m/%d/%Y')}"
    
    @property
    def is_within_tolerance(self):
        """Check if measurement is within tolerance"""
        if not self.expected_size or not self.tolerance:
            return None
        difference = abs(self.size_measured - self.expected_size)
        return difference <= self.tolerance
    
    @property
    def variance(self):
        """Calculate variance from expected size"""
        if not self.expected_size:
            return None
        return self.size_measured - self.expected_size
