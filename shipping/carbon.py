
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

### emissions 
# factor from Green Freight Handbook
#  https://storage.googleapis.com/scsc/Green%20Freight/EDF-Green-Freight-Handbook.pdf

emissions_factor = 161.8 #grams CO2 per short-ton mile
# page 11, average emission for combined types of trucks

### weight of package 
# arbitrary for now, source from vendor later
weight_lbs = 50
weight_short_ton = weight_lbs / 2000

# estimate carbon involved: W * D * Fe (weight * distance * emissionsFactor) 


# Weight * Distance
ton_miles = weight_short_ton * miles

# emissions factor
emissions_factor = 161.8 #grams CO2 per ton mile

# W * D * Emissions Factor

grams_co2 = weight_short_ton * miles * emissions_factor