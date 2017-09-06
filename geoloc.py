from geolocation.main import GoogleMaps

key='AIzaSyB0dCe_e_aGb6S2ftcGQFdTR4yMe_1O3Ak'    #Google Maps Geocoding API key

def coordinates(address):
    coord=[]
    google_maps=GoogleMaps(api_key=key)
    location=google_maps.search(location=address)
    my_location=location.first()
    coord.append(my_location.lat)
    coord.append(my_location.lng)
    return coord
