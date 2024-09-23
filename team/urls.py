from django.urls import path
from . import views

urlpatterns = [
    path('', views.teammate_list, name='teammate_list'),
    path('<int:pk>/', views.teammate_detail, name='teammate_detail'),
    #path('portfolio/<int:pk>/', views.portfolio_view, name='teammate_portfolio'), 

]
