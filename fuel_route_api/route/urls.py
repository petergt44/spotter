from django.urls import path
from .views import get_fuel_route, fuel_route_form

urlpatterns = [
    path('fuel-route/', get_fuel_route, name='get_fuel_route'),
    path('fuel-route-form/', fuel_route_form, name='fuel_route_form'),
]
