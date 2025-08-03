from rest_framework import viewsets, permissions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import WorkCenter
from .serializers import WorkCenterSerializer

class WorkCenterViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workcenters
    """
    queryset = WorkCenter.objects.all()
    serializer_class = WorkCenterSerializer
    permission_classes = [permissions.AllowAny]

class WorkCenterListView(ListView):
    model = WorkCenter
    template_name = 'workcenters/workcenter_list.html'
    context_object_name = 'workcenters'

class WorkCenterDetailView(DetailView):
    model = WorkCenter
    template_name = 'workcenters/workcenter_detail.html'
    context_object_name = 'workcenter'

class WorkCenterCreateView(CreateView):
    model = WorkCenter
    fields = '__all__'
    template_name = 'workcenters/workcenter_form.html'
    success_url = reverse_lazy('workcenters:workcenter_list')

class WorkCenterUpdateView(UpdateView):
    model = WorkCenter
    fields = '__all__'
    template_name = 'workcenters/workcenter_form.html'
    success_url = reverse_lazy('workcenters:workcenter_list')

class WorkCenterDeleteView(DeleteView):
    model = WorkCenter
    template_name = 'workcenters/workcenter_confirm_delete.html'
    success_url = reverse_lazy('workcenters:workcenter_list')
