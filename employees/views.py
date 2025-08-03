from rest_framework import viewsets, permissions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for employees
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employees:employee_list')
