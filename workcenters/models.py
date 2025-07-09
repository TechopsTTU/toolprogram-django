from django.db import models

class WorkCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)

    def __str__(self):
        return self.name