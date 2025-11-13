import requests
from geopy.geocoders import Nominatim
from .simulation import simulate_trip
import polyline

def calculate_trip(current_location, pickup_location, dropoff_location, current_cycle_used):
    geolocator = Nominatim(user_agent="eld_app")
    
    # Geocode locations
    current = geolocator.geocode(current_location)
    pickup = geolocator.geocode(pickup_location)
    dropoff = geolocator.geocode(dropoff_location)
    
    if not all([current, pickup, dropoff]):
        raise ValueError("Unable to geocode one or more locations")

    coords = [
        (current.longitude, current.latitude),
        (pickup.longitude, pickup.latitude),
        (dropoff.longitude, dropoff.latitude)
    ]
    
    # Get route from OSRM
    coord_str = ';'.join(f"{lon},{lat}" for lon, lat in coords)
    route_url = f"http://router.project-osrm.org/route/v1/driving/{coord_str}?overview=full&geometries=polyline"
    response = requests.get(route_url)
    route_data = response.json()
    
    if route_data.get('code') != 'Ok':
        raise ValueError("Failed to retrieve route from OSRM")

    route = route_data['routes'][0]
    distance_miles = route['distance'] / 1609.34  # Convert meters to miles
    duration_hours = route['duration'] / 3600    # Convert seconds to hours
    
    # Simulate trip
    duty_status_log, log_sheets = simulate_trip(route, distance_miles, current_cycle_used)
    
    # Prepare map data
    geometry = polyline.decode(route['geometry'])
    stops = [
        {"type": "start", "location": [coords[0][1], coords[0][0]], "distance": 0},
        {"type": "pickup", "location": [coords[1][1], coords[1][0]], "distance": route['legs'][0]['distance'] / 1609.34}
    ]
    
    cumulative_distance = 0
    for leg in route['legs']:
        cumulative_distance += leg['distance'] / 1609.34
        if cumulative_distance >= 1000:
            stops.append({"type": "fueling", "location": geometry[len(geometry)//2], "distance": 1000})
            cumulative_distance -= 1000

    stops.append({"type": "dropoff", "location": [coords[2][1], coords[2][0]], "distance": distance_miles})
    
    return {
        "route": {
            "geometry": route['geometry'],
            "distance": distance_miles,
            "duration": duration_hours,
            "stops": stops
        },
        "duty_status_log": duty_status_log,
        "log_sheets": log_sheets,
        "map_data": {
            "route_path": route['geometry'],
            "markers": stops + [{"type": "rest", "location": event["location"], "duration": event["duration"]}
                               for event in duty_status_log if event["status"] == "off_duty" and "location" in event]
        }
    }