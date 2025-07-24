from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import WorkCenter

class WorkCenterListView(ListView):
    model = WorkCenter
    template_name = 'workcenters/workcenter_list.html'

class WorkCenterDetailView(DetailView):
    model = WorkCenter
    template_name = 'workcenters/workcenter_detail.html'

class WorkCenterCreateView(CreateView):
    model = WorkCenter
    fields = ['name', 'location', 'supervisor', 'description', 'is_active']
    template_name = 'workcenters/workcenter_form.html'
    success_url = reverse_lazy('workcenters:workcenter_list')

class WorkCenterUpdateView(UpdateView):
    model = WorkCenter
    fields = ['name', 'location', 'supervisor', 'description', 'is_active']
    template_name = 'workcenters/workcenter_form.html'
    success_url = reverse_lazy('workcenters:workcenter_list')

class WorkCenterDeleteView(DeleteView):
    model = WorkCenter
    template_name = 'workcenters/workcenter_confirm_delete.html'
    success_url = reverse_lazy('workcenters:workcenter_list')