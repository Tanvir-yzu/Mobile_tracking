from django.db import models
from users.models import CustomUser

class Device(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tracking_interval = models.IntegerField(default=60)  # in seconds
    is_tracking_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (Owner: {self.owner.username})"