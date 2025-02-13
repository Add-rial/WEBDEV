from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path('bus_details/<int:bus_id>/', views.bus_details, name = "bus_details")
]
