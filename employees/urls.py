from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
]