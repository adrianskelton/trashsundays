from django.db import models
from django.contrib.auth.models import User

class TrashCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bags_collected = models.IntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} collected {self.bags_collected} bags'

class TrashPickup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    picked_up_at = models.DateTimeField(auto_now_add=True)
    trash_volume = models.FloatField()  # In liters or bags


