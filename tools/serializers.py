from rest_framework import serializers
from .models import Tool
from workcenters.models import WorkCenter
from employees.models import Employee

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name', 'serial_number', 'calibrated', 'last_checked_in', 'workcenter', 'assigned_to']
        
    def to_representation(self, instance):
        """Add more detailed representation of related fields"""
        ret = super().to_representation(instance)
        
        if instance.workcenter:
            ret['workcenter'] = {
                'id': instance.workcenter.id,
                'name': instance.workcenter.name
            }
            
        if instance.assigned_to:
            ret['assigned_to'] = {
                'id': instance.assigned_to.id,
                'first_name': instance.assigned_to.first_name,
                'last_name': instance.assigned_to.last_name
            }
            
        return ret
