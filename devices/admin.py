from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'owner', 'name', 'tracking_interval', 'is_tracking_active', 'last_updated')
    list_filter = ('is_tracking_active', 'owner')
    search_fields = ('device_id', 'name', 'owner__username')
    raw_id_fields = ('owner',)  # Helps with large user bases