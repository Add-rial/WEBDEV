from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from django.db.models import F

from bus.models import Bus
from .models import *

# Create your views here.
def index(request): 
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    buses = Bus.objects.filter(passengers__booked_by=request.user).distinct()
    bus_names = {}
    for bus in buses:
        p = bus.passengers.filter(booked_by=request.user)
        names = [ f'{x.name}' for x in p]
        bus_names[bus.id] = (f'{bus}-------->Booked For: {names}')

        
    return render(request, 'users/index.html', {
        "booked_buses": bus_names.items()
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
    
def book_bus_redirect(request, bus_id):
    name = request.GET.get('name')
    return redirect('users:book_bus', bus_id, name)    

def book_bus(request, bus_id, name):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
  
    current_bus = Bus.objects.get(pk = bus_id)
    if current_bus.available_seats == 0:
        return render(request, 'users/book_bus.html', {
            "bus_to_book": current_bus,
            "message": "NO AVAILABLE SEATS"
        }) 
    elif request.user.wallet < current_bus.cost:
        return render(request, "users/book_bus.html", {
            "bus_to_book": current_bus,
            "message": "NOT ENOUGH MONEY, GET BETTER LOSER"
        })
    else:
        p = Passenger(booked_by=request.user, bus=current_bus, name = name)
        p.save()                                       #available seats updated while saving Passenger object
        
        request.user.wallet -= current_bus.cost
        request.user.save()
        return HttpResponseRedirect(reverse("users:index"))
        