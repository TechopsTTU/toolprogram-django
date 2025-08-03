from rest_framework import serializers
from .models import Employee
from tools.models import Tool

class EmployeeSerializer(serializers.ModelSerializer):
    assigned_tools = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'department', 'position', 'assigned_tools']

    def get_assigned_tools(self, obj):
        """Get tools assigned to this employee"""
        tools = Tool.objects.filter(assigned_to=obj)
        return [{
            'id': tool.id,
            'name': tool.name,
            'serial_number': tool.serial_number,
            'calibrated': tool.calibrated
        } for tool in tools]
