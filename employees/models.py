from django.db import models

class Employee(models.Model):
    # example fields
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    employee_number = models.CharField(max_length=20, default='')

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.name