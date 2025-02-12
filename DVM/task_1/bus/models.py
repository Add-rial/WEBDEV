from django.db import models

import datetime


now = datetime.datetime.now()

# Create your models here.

class Bus_Stop(models.Model):
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null = True, blank=True)
    
    def __str__(self):
        return f"{self.city}, {self.state}"

class Bus(models.Model):
    origin = models.ForeignKey(Bus_Stop, on_delete=models.CASCADE, related_name = "departuress")
    destination = models.ForeignKey(Bus_Stop, on_delete=models.CASCADE, related_name = "arrivals")
    bus_details = models.CharField(max_length=100, null = True, blank=True)
    registration_number = models.CharField(max_length=15, null = True, blank=True)
    
    cost = models.IntegerField(default=500)
    max_capacity = models.IntegerField(default=50)
    filled_seats = models.IntegerField(null = True, blank=True, default=0)
    
    start_time = models.DateTimeField(max_length = 32, default=now)
    end_time = models.DateTimeField(max_length = 32, default=now)
    
    def __str__(self):
        return f"{self.origin} --> {self.destination}"
