from django.contrib import admin
from .models import Bus, Bus_Stop
# Register your models here.

class BusStopAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'description')
    search_fields = ('city', 'state')
    
class BusAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'bus_details', 'cost')
    search_fields = ('origin', 'destination', 'cost')

admin.site.register(Bus, BusAdmin)