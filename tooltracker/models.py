from django.db import models
from django.utils import timezone
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter


class ToolTransaction(models.Model):
    """Model for tracking tool checkout/return transactions - matches legacy ToolTracker functionality"""
    
    STATUS_CHOICES = [
        ('CHECKED_OUT', 'Checked Out'),
        ('RETURNED', 'Returned'),
    ]
    
    tool = models.ForeignKey(
        Tool, 
        on_delete=models.CASCADE, 
        help_text="Tool being checked out/returned"
    )
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        help_text="Employee checking out/returning the tool"
    )
    from_location = models.ForeignKey(
        WorkCenter, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='outgoing_transactions',
        help_text="Work center tool is being taken from"
    )
    to_location = models.ForeignKey(
        WorkCenter, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='incoming_transactions',
        help_text="Work center tool is being taken to"
    )
    
    # Checkout information
    checkout_date = models.DateTimeField(
        default=timezone.now,
        help_text="Date and time tool was checked out"
    )
    promise_return_date = models.DateField(
        null=True, 
        blank=True,
        help_text="Promised return date"
    )
    
    # Return information
    return_date = models.DateTimeField(
        null=True, 
        blank=True,
        help_text="Date and time tool was returned"
    )
    return_employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='returned_transactions',
        help_text="Employee who processed the return"
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='CHECKED_OUT',
        help_text="Current status of the transaction"
    )
    
    notes = models.TextField(
        blank=True,
        help_text="Additional notes about the transaction"
    )
    
    class Meta:
        ordering = ['-checkout_date']
        verbose_name = "Tool Transaction"
        verbose_name_plural = "Tool Transactions"
        
    def __str__(self):
        status_str = f" - {self.get_status_display()}"
        return f"{self.tool.name} to {self.employee.full_name}{status_str}"
    
    @property
    def is_overdue(self):
        """Check if tool is overdue for return"""
        if self.status == 'RETURNED' or not self.promise_return_date:
            return False
        return timezone.now().date() > self.promise_return_date
    
    @property
    def days_out(self):
        """Calculate number of days tool has been checked out"""
        if self.status == 'RETURNED':
            return (self.return_date.date() - self.checkout_date.date()).days
        return (timezone.now().date() - self.checkout_date.date()).days
    
    def return_tool(self, return_employee=None):
        """Mark tool as returned"""
        self.return_date = timezone.now()
        self.return_employee = return_employee
        self.status = 'RETURNED'
        self.save(update_fields=['return_date', 'return_employee', 'status'])
        
        # Update tool location back to original location
        if self.from_location:
            self.tool.location = self.from_location
            self.tool.check_in()
