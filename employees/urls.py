app_name = "employees"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

# Create a router for API endpoints
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_edit'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail_alt'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_edit_alt'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete_alt'),
    # Include the API routes
    path('api/', include(router.urls)),

    # Keep existing URL patterns
    # ...
]
