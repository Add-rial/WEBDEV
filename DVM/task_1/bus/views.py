from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Bus, Bus_Stop

def index(request):
    return render(request, 'bus/index.html', {
        "buses": Bus.objects.all()
    })
    
def bus_details(request, bus_id, from_where = "from bus"):
    bus = Bus.objects.get(pk = bus_id)
    
    if "users" in from_where:
        return render(request, "bus/bus_details.html", {
            "bus_to_show": bus,
            "message": "users"
        })
    else:
        return render(request, "bus/bus_details.html", {
            "bus_to_show": bus
        })