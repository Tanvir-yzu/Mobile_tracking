from django.db import models
from devices.models import Device

class LocationData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    speed = models.FloatField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
    is_online = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.device.name} - {self.timestamp}"