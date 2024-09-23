from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                  # Handles /admin/
    path('team/', include('team.urls')),              # Includes team URLs
    path('portfolio/', include('portfolio.urls')),     # Includes portfolio URLs
]
