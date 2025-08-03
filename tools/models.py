from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    calibrated = models.BooleanField(default=False)
    last_checked_in = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, default='')
    location = models.ForeignKey('workcenters.WorkCenter', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.serial_number})"