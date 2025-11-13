# fuel_route_api/route/utils.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables


def get_route(start, end):
    """
    Get the route from the starting location to the ending location using Google Maps Directions API.
    
    Parameters:
    - start (str): Starting location in latitude,longitude format.
    - end (str): Ending location in latitude,longitude format.
    
    Returns:
    - route_data (dict): Data containing route information.
    
    Raises:
    - Exception: If the API request fails.
    """
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")  # Get the API key from environment variable
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={end}&key={api_key}"

    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()