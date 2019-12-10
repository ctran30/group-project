from application import app, db
from application.models import User, Post





#pip install googlemaps
#pip install prettyprint


#define our API key
#API_KEY = key()

#define our client
#gmaps = googlemaps.Client(key= API_KEY)

#define our search
#places_result = gmaps.place_nearby(location='-33.8670522, 151.1957362', radius = 4000, open_now = False, type= 'restaurant')

#pprint.pprint(places_result)

#place_result = gmaps.places_nearby(page_token = places_result['next_page_token'])
#for place in place_result['results']:
    #define my place id
    #my_place_id = place['place_id']
    #define the field we want sent back to us
    #my_fields = ['name', 'formatted_phone_number', 'type']
    #make a request for detail
    #place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
    #print the result
    #print(place_details)



#app = Flask(__name__)

#search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
#details_url = "https://maps.googleapis.com/maps/api/place/details/json"


if __name__ == "__main__":
    app.run()