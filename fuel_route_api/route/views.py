import requests
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import calculate_fuel_stops

@swagger_auto_schema(
    method='post',
    manual_parameters=[
        openapi.Parameter('body', openapi.IN_BODY, description="Origin and destination for the route", type=openapi.TYPE_OBJECT),
    ],
    responses={200: 'Route, fuel stops, and total cost returned', 400: 'Invalid input'}
)


@api_view(['POST'])
def get_fuel_route(request):
    """
    API endpoint to get fuel route information.

    Parameters:
    - request (Request): The HTTP request containing the start and end locations.

    Returns:
    - Response: The HTTP response containing the fuel route information.
    """
    # Extract data from the request body
    try:
        origin = request.data['origin']['location']['latLng']
        destination = request.data['destination']['location']['latLng']
    except KeyError:
        return Response({"error": "Origin and destination locations are required"}, status=400)

    # Construct the request payload for Google Maps API
    google_maps_url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
    api_key = 'YOUR_API_KEY'  # Replace with your actual Google Maps API key
    
    payload = {
        "origin": {
            "location": {
                "latLng": {
                    "latitude": origin['latitude'],
                    "longitude": origin['longitude']
                }
            }
        },
        "destination": {
            "location": {
                "latLng": {
                    "latitude": destination['latitude'],
                    "longitude": destination['longitude']
                }
            }
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
        "computeAlternativeRoutes": False,
        "routeModifiers": {
            "avoidTolls": False,
            "avoidHighways": False,
            "avoidFerries": False
        },
        "languageCode": "en-US",
        "units": "IMPERIAL"
    }

    # Make a request to the Google Maps API
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': api_key,
        'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'
    }

    response = requests.post(google_maps_url, json=payload, headers=headers)

    if response.status_code != 200:
        return Response({"error": "Failed to retrieve route information"}, status=response.status_code)

    # Process the response from Google Maps API
    data = response.json()
    if 'routes' not in data or not data['routes']:
        return Response({"error": "No routes found"}, status=400)

    # Extract relevant route information
    route_info = data['routes'][0]
    distance_meters = route_info['distanceMeters']
    polyline = route_info['polyline']['encodedPolyline']
    
    # Calculate fuel stops and total cost
    try:
        fuel_prices, total_cost, optimal_stops = calculate_fuel_stops(origin, destination)
        return Response({
            "distance_meters": distance_meters,
            "route_polyline": polyline,
            "fuel_prices": fuel_prices,
            "total_cost": total_cost,
            "optimal_stops": optimal_stops
        })
    except ValueError as e:
        return Response({"error": str(e)}, status=400)
    except Exception as e:
        return Response({"error": "An unexpected error occurred."}, status=500)


def fuel_route_form(request):
    """
    Renders the HTML form for testing the Fuel Route API.
    """
    return render(request, 'fuel_form.html')
