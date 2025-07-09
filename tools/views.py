from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tool

class ToolListView(ListView):
    model = Tool
    template_name = 'tools/tool_list.html'

class ToolDetailView(DetailView):
    model = Tool
    template_name = 'tools/tool_detail.html'

class ToolCreateView(CreateView):
    model = Tool
    fields = ['name', 'serial_number', 'calibrated', 'last_checked_in']
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tools:tool_list')

class ToolUpdateView(UpdateView):
    model = Tool
    fields = ['name', 'serial_number', 'calibrated', 'last_checked_in']
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tools:tool_list')

class ToolDeleteView(DeleteView):
    model = Tool
    template_name = 'tools/tool_confirm_delete.html'
    success_url = reverse_lazy('tools:tool_list')