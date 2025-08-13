from django.db import models
from django.core.validators import RegexValidator


class Employee(models.Model):
    name = models.CharField(max_length=100, help_text="Full name (legacy field)")
    employee_id = models.CharField(max_length=20, help_text="Legacy employee ID field")
    department = models.CharField(max_length=100, help_text="Department or work area assignment")
    email = models.EmailField(help_text="Corporate email address")
    first_name = models.CharField(max_length=50, default='', help_text="Employee first name")
    last_name = models.CharField(max_length=50, default='', help_text="Employee last name")
    employee_number = models.CharField(
        max_length=20, 
        default='', 
        unique=True,
        validators=[RegexValidator(
            regex=r'^EMP-\d{3}$',
            message='Employee number must be in format EMP-XXX (e.g., EMP-001)',
            code='invalid_employee_number'
        )],
        help_text="Unique employee number in format EMP-XXX"
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.name

    @property
    def full_name(self):
        """Return formatted full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.name

    @property
    def display_name(self):
        """Return name for display with employee number"""
        return f"{self.full_name} ({self.employee_number})"

    def clean(self):
        """Ensure name field is populated from first/last name"""
        from django.core.exceptions import ValidationError
        
        if self.first_name and self.last_name and not self.name:
            self.name = f"{self.first_name} {self.last_name}"
        
        if not self.employee_id and self.employee_number:
            self.employee_id = self.employee_number

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)