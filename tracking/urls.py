from django.urls import path
from . import views

urlpatterns = [
    path('live-map/', views.live_map_view, name='live_map'),
    path('history/<int:device_id>/', views.location_history_view, name='location_history'),
    path('add-location/', views.add_location_data, name='add_location'),
    path('add-location-data/', views.add_location_data, name='add_location_data'),
]