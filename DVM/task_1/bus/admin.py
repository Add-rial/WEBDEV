from django.contrib import admin
from .models import Bus, Bus_Stop
from users.models import Passenger
# Register your models here.

class PassengerInLine(admin.TabularInline):
    model = Passenger
    extra = 1

class BusStopAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'description')
    search_fields = ('city', 'state')
    
class BusAdmin(admin.ModelAdmin):
    inlines = [PassengerInLine]
    list_display = ('origin', 'destination', 'bus_details', 'cost')
    search_fields = ('origin', 'destination', 'cost')

admin.site.register(Bus, BusAdmin)
admin.site.register(Bus_Stop, BusStopAdmin) 