from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Bus, Bus_Stop

def index(request):
    return render(request, 'bus/index.html', {
        "buses": Bus.objects.all()
    })