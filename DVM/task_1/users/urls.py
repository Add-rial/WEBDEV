from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('available_buses/', views.available_buses, name = "available_buses"),
    path('book_bus/<int:bus_id>/<str:name>', views.book_bus, name = "book_bus"),
    path('book_bus_redirect/<int:bus_id>/', views.book_bus_redirect, name = "book_bus_redirect")
]
