### distance
import pandas as pd
import googlemaps
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

# set up google distance matrix API key
gmaps = googlemaps.Client(key = API_KEY)

#addresses
#arbitrary now, source from vendor later
address_vendor = '8000 24th Ave NW, Seattle, WA 98117'
address_client = '1118 S 13th St, Tacoma, WA 98405'

#street address conversion to lat long, maybe don't need to do?  
          # geo_vendor = gmaps.geocode(address_vendor)
          # geo_client = gmaps.geocode(address_client)

#api call, returns in xml? json?, [ ] extracts distance value in meters             
meters = gmaps.distance_matrix(
              origins = address_vendor, 
              destinations = address_client, 
              mode='driving')["rows"][0]["elements"][0]["distance"]["value"]

#convert meters to miles
miles = meters * 0.000621371
