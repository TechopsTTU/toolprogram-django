from django.db import models
from django.utils import timezone


class Tool(models.Model):
    name = models.CharField(max_length=100, help_text="Tool name or model designation")
    serial_number = models.CharField(max_length=50, unique=True, help_text="Unique serial number or identifier")
    calibrated = models.BooleanField(default=False, help_text="Current calibration status")
    last_checked_in = models.DateTimeField(null=True, blank=True, help_text="Last time tool was checked in/used")
    description = models.TextField(blank=True, default='', help_text="Detailed tool description and specifications")
    location = models.ForeignKey(
        'workcenters.WorkCenter', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        help_text="Current work center assignment"
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Tool"
        verbose_name_plural = "Tools"

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

    @property
    def is_available(self):
        """Check if tool is currently available (not checked out)"""
        return self.last_checked_in is None or self.last_checked_in < timezone.now()

    @property
    def calibration_status(self):
        """Return human-readable calibration status"""
        return "Calibrated" if self.calibrated else "Requires Calibration"

    @property
    def location_name(self):
        """Return location name or 'Unassigned' if no location"""
        return self.location.name if self.location else "Unassigned"

    def check_in(self):
        """Mark tool as checked in"""
        self.last_checked_in = timezone.now()
        self.save(update_fields=['last_checked_in'])

    def assign_to_location(self, workcenter):
        """Assign tool to a work center"""
        self.location = workcenter
        self.save(update_fields=['location'])