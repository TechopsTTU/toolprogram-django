from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/tools/', permanent=False)),
    path('admin/', admin.site.urls),
    path('tools/', include('tools.urls', namespace='tools')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('workcenters/', include('workcenters.urls', namespace='workcenters')),
]