from django.contrib import admin
from .models import Passenger

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('booked_under', 'name', 'get_booked_buses')
    search_fields = ('booked_under', 'name')
    
    def get_booked_buses(self, obj):
        return ", ".join([str(bus) for bus in obj.booked_buses.all()])
    get_booked_buses.short_description = 'Booked Buses'

