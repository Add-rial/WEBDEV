from django.db import models
from django.contrib.auth.models import User

from bus.models import Bus

User.add_to_class('booked_buses', models.ManyToManyField(Bus, blank=True, related_name="passengers"))
