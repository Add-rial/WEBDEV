from django.urls import path
from . import views

app_name = "bus"

urlpatterns = [
    path("", views.index, name = "index"),
    path('bus_details/<int:bus_id>/<str:from_where>/', views.bus_details, name = "bus_details")
]
