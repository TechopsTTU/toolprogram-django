from django.urls import path
from . import views

app_name = 'tooltracker'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('return/<int:transaction_id>/', views.return_tool, name='return'),
    path('get-wc/', views.get_work_center, name='get_wc'),
]