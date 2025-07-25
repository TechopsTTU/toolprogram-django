from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.ToolListView.as_view(), name='tool_list'),
    path('tool/<int:pk>/', views.ToolDetailView.as_view(), name='tool_detail'),
    path('tool/add/', views.ToolCreateView.as_view(), name='tool_add'),
    path('tool/<int:pk>/edit/', views.ToolUpdateView.as_view(), name='tool_edit'),
    path('tool/<int:pk>/delete/', views.ToolDeleteView.as_view(), name='tool_delete'),
    path('tool/<int:pk>/checkout/', views.check_out_tool, name='tool_checkout'),
    path('tool/<int:pk>/checkin/', views.check_in_tool, name='tool_checkin'),
]