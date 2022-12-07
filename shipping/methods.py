
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
def shipping_co2(origin, destination, weight_lbs):
    """
    params:
    origin: origin address of shipment
    destination: destination of shipment
    weight_lbs: float weight in lbs
    """
    # inputs
    origin = str(input("Package origin address?"))
    destination = str(input("Package destination address?"))
    weight = float(input("Package weight in pounds?  "))
    
    #api call
    meters = gmaps.distance_matrix(
        origins = origins_input,
        destinations = destinations_input,
        mode = str("driving")
    )["rows"][0]["elements"][0]["distance"]["value"]

    #conversions
    miles = meters * 0.000621371
    shortTon = pounds/2000
    emissions_factor = 161.8
    grams_co2 = shortTon * miles * emissions_factor
    lbs_co2 = grams_co2 * 0.0022046226

    #outputs
    return print("Package will travel {} miles and generate {} pounds of CO2" 
        .format(round(miles, 2), round(lbs_co2, 2))
        )

shipping_co2(
    "2220 S Oak St, Port Angeles, WA, 98362"
    , "2000 Pennsylvania Ave, Washington, D.C. 11100"
    , 123.45
)