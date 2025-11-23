from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list_view, name='device_list'),
    path('settings/<int:device_id>/', views.device_settings_view, name='device_settings'),
    path('add/', views.add_device_view, name='add_device'),
]