from django.db import models

class WorkCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
    
    def get_available_tools(self):
        return self.tools.filter(status='available')
    
    def get_checked_out_tools(self):
        return self.tools.filter(status='checked_out')
    
    class Meta:
        ordering = ['name']