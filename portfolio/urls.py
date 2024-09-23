from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),  # General portfolio view
    path('admin/', admin.site.urls),  # This handles /admin/
    path('team/', include('team.urls')),  # This includes the team URLs
    path('portfolio/<int:pk>/', views.portfolio_view, name='teammate_portfolio'),  # For individual teammate portfolios
]
