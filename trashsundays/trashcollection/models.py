from django.db import models
from django.contrib.auth.models import User

class TrashCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bags_collected = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} collected {self.bags_collected} bags'