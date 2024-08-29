from django.db import models
from django.contrib.auth.models import User

class TrashCollection(models.Model):
    BAG_SIZES = [
        ('10L', '10 Liters'),
        ('20L', '20 Liters'),
        ('30L', '30 Liters'),
        ('40L', '40 Liters'),
        # Add more sizes as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    volume = models.FloatField()  # Volume of trash picked up in liters
    bag_size = models.CharField(max_length=10, choices=BAG_SIZES)
    date_collected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.volume}L'