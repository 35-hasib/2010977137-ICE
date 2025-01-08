
import geocoder

def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng
    else:
        raise Exception('Error !!')

print(get_current_location)