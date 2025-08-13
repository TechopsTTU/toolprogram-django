from django.urls import path
from . import views

app_name = 'measure'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('add/', views.add_measure_view, name='add'),
    path('details/<int:measurement_id>/', views.details_view, name='details'),
    path('export/', views.export_view, name='export'),
]