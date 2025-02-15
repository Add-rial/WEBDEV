from django.db import models
from django.contrib.auth.models import User

from bus.models import Bus

class Passenger(models.Model):
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booked_for")
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="passengers")
    name = models.CharField(max_length=50, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.booked_by.username
        if not self.pk:
            self.bus.available_seats -= 1
            self.bus.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Name: {self.name}, Bus: {self.bus}'

User.add_to_class('wallet', models.IntegerField(blank=True, null=True, default=20000))