
import requests

def get_current_location(api_key):
    # Geolocation API endpoint
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + api_key

    # Send a POST request to the Geolocation API (no parameters required)
    try:
        response = requests.post(url)

        # Raise an exception for unsuccessful requests
        response.raise_for_status()

        # Parse the response JSON
        location_data = response.json()

        # Extract latitude and longitude
        latitude = location_data['location']['lat']
        longitude = location_data['location']['lng']

        return latitude, longitude

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None

# Replace with your Google API key
api_key = 'AlzaSyZsqrOsRl6X1QPe_QGzhOWJg92Ds1R9G4K'
latitude, longitude = get_current_location(api_key)

if latitude and longitude:
    print(f"Current Location: Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Unable to fetch location.")
