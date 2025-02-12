from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .models import Passenger
from bus.models import Bus

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        #print("1")
        return HttpResponseRedirect(reverse("login"))
    
    passenger = Passenger.objects.filter(booked_under=request.user).first()
    booked_buses = passenger.booked_buses.all() if passenger else []
    
    return render(request, 'users/index.html', {
        "booked_buses": booked_buses
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        
        return render(request, 'users/login.html', {
            "message": "Invalid credentials"
        })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        "message": "Logged out"
    })        
    
def add_bus(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    passenger = Passenger.objects.filter(booked_under=request.user).first()
    booked_buses = passenger.booked_buses.all() if passenger else []
    buses = Bus.objects.exclude(id__in=booked_buses.values_list('id', flat=True))
    
    return render(request, 'users/add_bus.html', {
        "available_buses": buses
    })