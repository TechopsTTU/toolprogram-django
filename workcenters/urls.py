from django.urls import path
from . import views

app_name = 'workcenters'

urlpatterns = [
    path('', views.WorkCenterListView.as_view(), name='workcenter_list'),
    path('workcenter/<int:pk>/', views.WorkCenterDetailView.as_view(), name='workcenter_detail'),
    path('workcenter/add/', views.WorkCenterCreateView.as_view(), name='workcenter_add'),
    path('workcenter/<int:pk>/edit/', views.WorkCenterUpdateView.as_view(), name='workcenter_edit'),
    path('workcenter/<int:pk>/delete/', views.WorkCenterDeleteView.as_view(), name='workcenter_delete'),
]