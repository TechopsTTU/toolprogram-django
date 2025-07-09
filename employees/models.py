from django.db import models

class Employee(models.Model):
    # example fields
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name