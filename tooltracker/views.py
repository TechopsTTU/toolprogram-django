from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db import models
from .models import ToolTransaction
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter


def checkout_view(request):
    """Tool checkout form - matches legacy CheckOut.cshtml"""
    context = {
        'tools': Tool.objects.all().order_by('name'),
        'employees': Employee.objects.all().order_by('last_name', 'first_name'),
        'workcenters': WorkCenter.objects.all().order_by('name'),
    }
    
    if request.method == 'POST':
        try:
            # Get form data
            tool_id = request.POST.get('tool_id')
            employee_id = request.POST.get('employee_id')
            from_wc_id = request.POST.get('from_wc_id')
            to_wc_id = request.POST.get('to_wc_id')
            promise_return_date = request.POST.get('promise_return_date')
            
            # Validate required fields
            if not all([tool_id, employee_id, to_wc_id]):
                messages.error(request, 'Tool, Employee, and Destination Work Center are required.')
                return render(request, 'tooltracker/checkout.html', context)
            
            # Get objects
            tool = get_object_or_404(Tool, id=tool_id)
            employee = get_object_or_404(Employee, id=employee_id)
            from_wc = get_object_or_404(WorkCenter, id=from_wc_id) if from_wc_id else None
            to_wc = get_object_or_404(WorkCenter, id=to_wc_id)
            
            # Check if tool is already checked out
            if ToolTransaction.objects.filter(tool=tool, status='CHECKED_OUT').exists():
                messages.error(request, f'Tool {tool.name} is already checked out.')
                return render(request, 'tooltracker/checkout.html', context)
            
            # Create transaction
            transaction = ToolTransaction.objects.create(
                tool=tool,
                employee=employee,
                from_location=from_wc,
                to_location=to_wc,
                promise_return_date=promise_return_date if promise_return_date else None,
            )
            
            # Update tool location
            tool.location = to_wc
            tool.save(update_fields=['location'])
            
            messages.success(request, f'Tool {tool.name} successfully checked out to {employee.full_name}.')
            return redirect('tooltracker:index')
            
        except Exception as e:
            messages.error(request, f'Error checking out tool: {str(e)}')
    
    return render(request, 'tooltracker/checkout.html', context)


def index_view(request):
    """List of checked out tools for return - matches legacy Index.cshtml"""
    # Get all checked out tools
    checked_out_transactions = ToolTransaction.objects.filter(
        status='CHECKED_OUT'
    ).select_related('tool', 'employee', 'from_location', 'to_location')
    
    context = {
        'transactions': checked_out_transactions,
        'title': 'Tool Return List'
    }
    
    return render(request, 'tooltracker/index.html', context)


def return_tool(request, transaction_id):
    """Process tool return"""
    transaction = get_object_or_404(ToolTransaction, id=transaction_id, status='CHECKED_OUT')
    
    if request.method == 'POST':
        try:
            # Process return
            transaction.return_tool()
            messages.success(request, f'Tool {transaction.tool.name} returned successfully.')
        except Exception as e:
            messages.error(request, f'Error returning tool: {str(e)}')
    
    return redirect('tooltracker:index')


@require_POST
def get_work_center(request):
    """AJAX endpoint to get work center for a tool - matches legacy GetWC functionality"""
    tool_serial = request.POST.get('Tool', '')
    
    try:
        # Look up tool by serial number (matching legacy logic)
        if len(tool_serial) > 5:  # Match legacy validation
            tool = Tool.objects.filter(serial_number__icontains=tool_serial).first()
            if tool and tool.location:
                return JsonResponse({'wc': tool.location.name})
    except Exception:
        pass
    
    return JsonResponse({'wc': ''})
