from rest_framework import serializers
from .models import WorkCenter
from tools.models import Tool

class WorkCenterSerializer(serializers.ModelSerializer):
    tools = serializers.SerializerMethodField()
    
    class Meta:
        model = WorkCenter
        fields = ['id', 'name', 'location', 'supervisor', 'description', 'tools']
        
    def get_tools(self, obj):
        """Get tools assigned to this work center"""
        tools = Tool.objects.filter(location=obj)
        return [{
            'id': tool.id,
            'name': tool.name,
            'serial_number': tool.serial_number,
            'calibrated': tool.calibrated
        } for tool in tools]
