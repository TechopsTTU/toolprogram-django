from django.db import models
from django.db.models import Count


class WorkCenter(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True,
        help_text="Work center identifier or code"
    )
    location = models.CharField(
        max_length=100, 
        help_text="Physical location (building, floor, bay)"
    )
    supervisor = models.CharField(
        max_length=100, 
        help_text="Work center supervisor name"
    )
    description = models.TextField(
        blank=True, 
        help_text="Detailed description of work center operations and capabilities"
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Work Center"
        verbose_name_plural = "Work Centers"

    def __str__(self):
        return self.name

    @property
    def tool_count(self):
        """Return number of tools assigned to this work center"""
        return self.tool_set.count()

    @property
    def calibrated_tool_count(self):
        """Return number of calibrated tools in this work center"""
        return self.tool_set.filter(calibrated=True).count()

    @property
    def display_info(self):
        """Return formatted display information"""
        return f"{self.name} - {self.location} (Supervisor: {self.supervisor})"

    def get_tools(self):
        """Return all tools assigned to this work center"""
        return self.tool_set.all()

    def get_calibrated_tools(self):
        """Return all calibrated tools in this work center"""
        return self.tool_set.filter(calibrated=True)

    def get_uncalibrated_tools(self):
        """Return all uncalibrated tools in this work center"""
        return self.tool_set.filter(calibrated=False)