#pip install googlemaps
#pip install prettyprint

import googlemaps
import pprint
import time
from GoogleMapsAPIKey import get_my_key

#define our API key
API_KEY = get_my_key()
#define our client
gmaps = googlemaps.Client(key= API_KEY)

#define our search
places_result = gmaps.place_nearby(location='-33.8670522, 151.1957362', radius = 4000, open_now = False, type= 'restaurant')

print.pprint(places_result)