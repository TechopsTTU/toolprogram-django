from rest_framework import serializers
from .models import Tool
from workcenters.models import WorkCenter
from employees.models import Employee

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name', 'serial_number', 'calibrated', 'last_checked_in', 'description', 'location']
        
    def to_representation(self, instance):
        """Add more detailed representation of related fields"""
        ret = super().to_representation(instance)
        
        if instance.location:
            ret['location'] = {
                'id': instance.location.id,
                'name': instance.location.name
            }
            
        return ret
