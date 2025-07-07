from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    calibrated = models.BooleanField(default=False)
    last_checked_in = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"