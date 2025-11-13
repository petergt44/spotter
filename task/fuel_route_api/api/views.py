import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FuelPrice
from .serializers import FuelPriceSerializer

google_maps_url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
api_key = 'YOUR_API_KEY'  # Replace with your actual Google Maps API key

@api_view(['POST'])
def get_route(request):
    """
    Calculates the optimal route between two locations, including fuel ups and total cost.

    Args:
        request (HttpRequest): The HTTP request containing the start and end locations.

    Returns:
        Response: A JSON response containing the route, fuel ups, and total cost.
    """
    # Validate form data
    serializer = RouteSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    start = serializer.validated_data['start']
    end = serializer.validated_data['end']

    # Get fuel prices for the route
    fuel_prices = FuelPrice.objects.all()
    serialized_fuel_prices = FuelPriceSerializer(fuel_prices, many=True)

    # Call Google Maps API for route and distance
    params = {
        'origin': start,
        'destination': end,
        'drivingMode': 'driving',  # Adjust mode if needed
        'key': api_key,
    }
    response = requests.get(google_maps_url, params=params)
    route_data = response.json()

    # Error handling for Google Maps API response
    if route_data['status'] != 'OK':
        return Response({'error': route_data['error']['message']}, status=status.HTTP_400_BAD_REQUEST)

    # Extract distance
    distance = route_data['routes'][0]['legs'][0]['distance']['value'] / 1000  # Convert to kilometers

    # Calculate fuel consumption and cost (assuming 10 mpg)
    fuel_consumption = distance / 10
    total_cost = fuel_consumption * min([price for city, price in serialized_fuel_prices.data])

    # Implement fuel up calculation
    fuel_ups = calculate_fuel_ups(distance)

    # Prepare response data
    response_data = {
        'route': route_data['routes'][0]['overview_polyline']['points'],
        'fuel_ups': fuel_ups,
        'total_cost': total_cost,
    }

    return Response(response_data, status=status.HTTP_200_OK)

