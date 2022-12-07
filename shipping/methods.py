
# modules
import googlemaps
import os
from dotenv import load_dotenv
load_dotenv()

# define api key
API_KEY = os.getenv('API_KEY')

# set up google distance matrix API key
gmaps = googlemaps.Client(key = API_KEY)

# co2 function bundled with api call, works well
def shipping_co2(origins, destinations, weight_kg):
    """
    params:
    origin: origin address of shipment
    destination: destination of shipment
    weight_kg: float weight in kg
    """
    
    # api call
    meters = gmaps.distance_matrix(
        origins = origins,
        destinations = destinations,
        mode = str("driving")
    )["rows"][0]["elements"][0]["distance"]["value"]

    # conversions
    miles = meters * 0.000621371
    kilometers = meters / 1000
    shortTon = weight_kg * 0.001102311

    # factors
    emissions_factor = 161.8 #grams/mile, need miles

    # model
    grams_co2 = shortTon * miles * emissions_factor

    kg_co2 = grams_co2/1000


    #outputs
    return print("Package will travel {} kilometers and generate {} kilograms of CO2" 
        .format(round(kilometers, 2), round(kg_co2, 2))
        )


shipping_co2(
    "2220 S Oak St, Port Angeles, WA, 98362"
    , "918 Windsor St, Santa Cruz CA 95062"
    , 10
)
