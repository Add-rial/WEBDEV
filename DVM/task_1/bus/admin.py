from django.contrib import admin
from .models import Bus, Bus_Stop
# Register your models here.

@admin.register(Bus_Stop)
class BusStopAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'description')
    search_fields = ('city', 'state')
    
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'bus_details', 'cost')
    search_fields = ('origin', 'destination', 'cost')
