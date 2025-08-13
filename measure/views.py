from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import ToolMeasure
from tools.models import Tool
from employees.models import Employee
from workcenters.models import WorkCenter


def index_view(request):
    """Recent tool measurements list - matches legacy Index.cshtml"""
    measurements = ToolMeasure.objects.all().select_related('tool', 'employee', 'work_center')
    
    # Pagination (matching original complex pagination)
    paginator = Paginator(measurements, 10)  # 10 measurements per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'measurements': page_obj,
        'title': 'Recent Tool Measure',
        'total_pages': paginator.num_pages,
        'current_page': int(page_number),
    }
    
    return render(request, 'measure/index.html', context)


def add_measure_view(request):
    """Add new tool measurement - matches legacy AddMeasure.cshtml"""
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
            work_center_id = request.POST.get('work_center_id')
            size_measured = request.POST.get('size_measured')
            expected_size = request.POST.get('expected_size')
            tolerance = request.POST.get('tolerance')
            condition = request.POST.get('condition', 'GOOD')
            notes = request.POST.get('notes', '')
            
            # Validate required fields
            if not all([tool_id, employee_id, size_measured]):
                messages.error(request, 'Tool, Employee, and Size Measured are required.')
                return render(request, 'measure/add_measure.html', context)
            
            # Get objects
            tool = Tool.objects.get(id=tool_id)
            employee = Employee.objects.get(id=employee_id)
            work_center = WorkCenter.objects.get(id=work_center_id) if work_center_id else None
            
            # Create measurement
            measurement = ToolMeasure.objects.create(
                tool=tool,
                employee=employee,
                work_center=work_center,
                size_measured=float(size_measured),
                expected_size=float(expected_size) if expected_size else None,
                tolerance=float(tolerance) if tolerance else None,
                condition=condition,
                notes=notes,
            )
            
            messages.success(request, f'Measurement recorded successfully for {tool.name}.')
            return redirect('measure:index')
            
        except Exception as e:
            messages.error(request, f'Error recording measurement: {str(e)}')
    
    return render(request, 'measure/add_measure.html', context)


def details_view(request, measurement_id):
    """View measurement details"""
    try:
        measurement = ToolMeasure.objects.select_related('tool', 'employee', 'work_center').get(id=measurement_id)
        context = {
            'measurement': measurement,
            'title': f'Measurement Details - {measurement.tool.name}',
        }
        return render(request, 'measure/details.html', context)
    except ToolMeasure.DoesNotExist:
        messages.error(request, 'Measurement not found.')
        return redirect('measure:index')


def export_view(request):
    """Export measurements to CSV - matches legacy Export functionality"""
    import csv
    from django.http import HttpResponse
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tool_measurements.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Date', 'Tool', 'Serial Number', 'Employee', 'Work Center', 'Size Measured', 'Expected Size', 'Tolerance', 'Condition', 'Notes'])
    
    measurements = ToolMeasure.objects.all().select_related('tool', 'employee', 'work_center')
    for measurement in measurements:
        writer.writerow([
            measurement.measurement_date.strftime('%m/%d/%Y'),
            measurement.tool.name,
            measurement.tool.serial_number,
            measurement.employee.full_name,
            measurement.work_center.name if measurement.work_center else 'N/A',
            measurement.size_measured,
            measurement.expected_size or 'N/A',
            measurement.tolerance or 'N/A',
            measurement.get_condition_display(),
            measurement.notes,
        ])
    
    return response
