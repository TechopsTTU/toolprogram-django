app_name = "tools"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToolViewSet, ToolsListView, ToolDetailView, ToolCreateView, ToolUpdateView, ToolDeleteView

# Create a router for API endpoints
router = DefaultRouter()
router.register(r'tools', ToolViewSet)

urlpatterns = [
    path('', ToolsListView.as_view(), name='tool_list'),
    path('tool/add/', ToolCreateView.as_view(), name='tool_add'),
    path('tool/<int:pk>/', ToolDetailView.as_view(), name='tool_detail'),
    path('tool/<int:pk>/edit/', ToolUpdateView.as_view(), name='tool_edit'),
    path('tool/<int:pk>/delete/', ToolDeleteView.as_view(), name='tool_delete'),
    # Include the API routes
    path('api/', include(router.urls)),

    # Keep existing URL patterns
    # ...
]
