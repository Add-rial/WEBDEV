from django.contrib import admin

from .models import Passenger

@admin.register(Passenger)
class AdminPassenger(admin.ModelAdmin):
    list_display = ('name', 'booked_by', 'bus')
    search_fields = ('name', 'booked_by', 'bus')