from rest_framework import serializers
from .models import Employee
from tools.models import Tool

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name', 'first_name', 'last_name', 'employee_id', 'employee_number', 'department', 'email']
