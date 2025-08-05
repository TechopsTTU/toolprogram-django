from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Tool
from .serializers import ToolSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

# Landing page view
def landing_page(request):
    """Landing page with navigation to all sections"""
    return render(request, 'landing.html')

class ToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint for tools
    """
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['post'])
    def assign_to_workcenter(self, request, pk=None):
        """Assign a tool to a workcenter"""
        tool = self.get_object()
        workcenter_id = request.data.get('workcenter_id')

        if not workcenter_id:
            return Response(
                {"error": "WorkCenter ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        from workcenters.models import WorkCenter
        try:
            workcenter = WorkCenter.objects.get(id=workcenter_id)
            tool.location = workcenter
            tool.save()
            return Response(ToolSerializer(tool).data)
        except WorkCenter.DoesNotExist:
            return Response(
                {"error": "WorkCenter not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class ToolsListView(ListView):
    model = Tool
    template_name = 'tools/tool_list.html'
    context_object_name = 'tools'

class ToolDetailView(DetailView):
    model = Tool
    template_name = 'tools/tool_detail.html'
    context_object_name = 'tool'

class ToolCreateView(CreateView):
    model = Tool
    fields = '__all__'
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tools:tool_list')

class ToolUpdateView(UpdateView):
    model = Tool
    fields = '__all__'
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tools:tool_list')

class ToolDeleteView(DeleteView):
    model = Tool
    template_name = 'tools/tool_confirm_delete.html'
    success_url = reverse_lazy('tools:tool_list')
