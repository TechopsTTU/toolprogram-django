from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'employee_id', 'department', 'email', 'phone', 'primary_workcenter', 'hire_date', 'is_active']
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'employee_id', 'department', 'email', 'phone', 'primary_workcenter', 'hire_date', 'is_active']
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employees:employee_list')