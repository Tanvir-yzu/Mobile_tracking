from django.contrib import admin
from .models import LocationData

@admin.register(LocationData)
class LocationDataAdmin(admin.ModelAdmin):
    list_display = ('device', 'latitude', 'longitude', 'timestamp', 'is_online')
    list_filter = ('is_online', 'timestamp')
    search_fields = ('device__name', 'device__owner__username')
    date_hierarchy = 'timestamp'  # Allows filtering by date
    raw_id_fields = ('device',)  # Improves performance