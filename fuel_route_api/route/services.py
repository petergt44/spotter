# fuel_route_api/route/services.py
from .utils import get_route


def calculate_fuel_stops(start, end):
    """
    Calculate fuel stops along the route based on starting and ending locations.

    Parameters:
    - start (str): Starting location in latitude,longitude format.
    - end (str): Ending location in latitude,longitude format.

    Returns:
    - fuel_prices (list): List of fuel prices at optimal stops.
    - total_cost (float): Total cost of fuel for the trip.
    - route_map (dict): Map data for the route.

    Raises:
    - ValueError: If no routes are found in the response.
    """
    route_data = get_route(start, end)

    # Check for errors in the response
    if route_data.get('status') != 'OK':
        raise ValueError(f"Error from Google Maps API: {route_data.get('error_message', 'Unknown error')}")

    # Process the route data
    if not route_data.get('routes'):
        raise ValueError("No routes found in the response.")

    # Extract route information and fuel cost calculations here...
    # This would include calculating fuel prices and determining stops based on the route

    # Example return statement, update according to your logic
    return [], 0, route_data  # Adjust this to return actual fuel prices and total cost
