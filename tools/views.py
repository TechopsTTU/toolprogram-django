from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta
from .models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter

class ToolListView(ListView):
    model = Tool
    template_name = 'tools/tool_list.html'

class ToolDetailView(DetailView):
    model = Tool
    template_name = 'tools/tool_detail.html'

class ToolCreateView(CreateView):
    model = Tool
    fields = ['name', 'serial_number', 'calibrated', 'status', 'assigned_to', 'current_location', 'due_date', 'last_checked_in']
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tools:tool_list')

class ToolUpdateView(UpdateView):
    model = Tool
    fields = ['name', 'serial_number', 'calibrated', 'status', 'assigned_to', 'current_location', 'due_date', 'last_checked_in']
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tools:tool_list')

class ToolDeleteView(DeleteView):
    model = Tool
    template_name = 'tools/tool_confirm_delete.html'
    success_url = reverse_lazy('tools:tool_list')

def check_out_tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    
    if tool.status != 'available':
        messages.error(request, f'Tool {tool.name} is not available for checkout.')
        return redirect('tools:tool_detail', pk=pk)
    
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        workcenter_id = request.POST.get('workcenter')
        due_date_str = request.POST.get('due_date')
        
        employee = get_object_or_404(Employee, pk=employee_id) if employee_id else None
        workcenter = get_object_or_404(WorkCenter, pk=workcenter_id) if workcenter_id else None
        
        due_date = None
        if due_date_str:
            try:
                due_date = timezone.datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M').replace(tzinfo=timezone.get_current_timezone())
            except ValueError:
                messages.error(request, 'Invalid due date format.')
                return render(request, 'tools/check_out_form.html', {
                    'tool': tool,
                    'employees': Employee.objects.filter(is_active=True),
                    'workcenters': WorkCenter.objects.filter(is_active=True),
                })
        
        tool.check_out(employee, workcenter, due_date)
        messages.success(request, f'Tool {tool.name} has been checked out successfully.')
        return redirect('tools:tool_detail', pk=pk)
    
    context = {
        'tool': tool,
        'employees': Employee.objects.filter(is_active=True),
        'workcenters': WorkCenter.objects.filter(is_active=True),
    }
    return render(request, 'tools/check_out_form.html', context)

def check_in_tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    
    if tool.status != 'checked_out':
        messages.error(request, f'Tool {tool.name} is not checked out.')
        return redirect('tools:tool_detail', pk=pk)
    
    if request.method == 'POST':
        workcenter_id = request.POST.get('workcenter')
        workcenter = get_object_or_404(WorkCenter, pk=workcenter_id) if workcenter_id else None
        
        tool.check_in(workcenter)
        messages.success(request, f'Tool {tool.name} has been checked in successfully.')
        return redirect('tools:tool_detail', pk=pk)
    
    context = {
        'tool': tool,
        'workcenters': WorkCenter.objects.filter(is_active=True),
    }
    return render(request, 'tools/check_in_form.html', context)