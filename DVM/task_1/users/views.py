from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from django.db.models import F

from bus.models import Bus
from .models import *

# Create your views here.
def index(request): 
    if not request.user.is_authenticated:
        #print("1")
        return HttpResponseRedirect(reverse("users:login"))
    
    buses = Bus.objects.filter(passengers__booked_by=request.user).distinct()
    bus_names = {}
    for bus in buses:
        p = bus.passengers.filter(booked_by=request.user)
        names = [ f'{x.name}' for x in p]
        bus_names[bus.id] = (f'{bus}-------->Booked For: {names}')
    
    return render(request, 'users/index.html', {
        "booked_buses": bus_names.items(), 
        
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        
        return render(request, 'users/login.html', {
            "message": "Invalid credentials"
        })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        "message": "Logged out"
    })        
    
def available_buses(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    buses = Bus.objects.all()
    
    return render(request, 'users/available_buses.html', {
        "available_buses": buses
    })
    
def book_bus(request, bus_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
  
    current_bus = Bus.objects.get(pk = bus_id)
    if current_bus.available_seats == 0:
        return render(request, 'users/book_bus.html', {
            "bus_to_book": current_bus,
            "message": "NO AVAILABLE SEATS"
        })
    else:
        p = Passenger(booked_by=request.user, bus=current_bus)
        p.save()
        
        current_bus.available_seats = current_bus.available_seats - 1
        current_bus.save()
        return render(request, 'users/book_bus.html', {
            "bus_to_book": current_bus,
            "message": "BOOKING SUCCESSFUL"
        })
        