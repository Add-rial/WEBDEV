from django.db import models
from django.contrib.auth.models import User

from bus.models import Bus

# Create your models here.
class Passenger(models.Model):
    booked_under = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    
    booked_buses = models.ManyToManyField(Bus, blank=True, related_name="passenger")
    
    def save(self, *args, **kwargs):                      # to update the default name to the booked_under.username
        if not self.name:                                 # if the passenger doesn't specify it
            self.name = self.booked_under.username
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.name}"
    
