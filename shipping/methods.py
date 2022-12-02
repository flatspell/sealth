
# need weight, distance, emissions_factor
# co2 = shortTon * miles * emissions_factor

# origin/destination api pull
import googlemaps
import os
from dotenv import load_dotenv
load_dotenv()

#define api key
API_KEY = os.getenv('API_KEY')

# set up google distance matrix API key
gmaps = googlemaps.Client(key = API_KEY)

#origin input
def locations(origins, destinations, mode):
    origins = origins
    destinations = destinations
    mode = mode
origins = str(input("Package origin address?"))
destinations = str(input("Package destination address?"))
mode = str("driving")

def distance(meters):
    meters = meters
meters = gmaps.distance_matrix(
              origins = origins, 
              destinations = destinations, 
              mode = mode)["rows"][0]["elements"][0]["distance"]["value"]



# weight conversion
def pounds_to_tons(pounds):
    shortTon = pounds/2000
    return float(shortTon)
pounds = float(input("Package weight in pounds?  "))
shortTon = pounds_to_tons(pounds)
print("Package weighs {} pounds or {} short tons" .format(pounds, shortTon))


# distance conversion
def meters_to_miles(meters):
    miles = meters *0.000621371
    return float(miles)
miles = meters_to_miles(meters)
print("Package will travel {} miles" .format(round(miles, 2)))

# emissions factor
emissions_factor = 161.8


# model:
# co2 = shortTon * miles * emissions_factor
grams_co2 = shortTon * miles * emissions_factor
lbs_co2 = grams_co2 * 0.0022046226

# final output
print("Shipping this package will generate {} pounds of CO2 emissions." .format(round(lbs_co2, 2)))







### JUNKYARD ###

# class Carbon:
#     def __init__(self, origin, destination, miles, weight, eFactor):
#         self.origin = origin
#         self.destination = destination
#         self.miles = miles
#         self.weight = weight
#         self.eFactor = eFactor

# def distance():
#     gmaps = googlemaps.Client(key = API_KEY)
#     API_KEY = os.getenv('API_KEY')
#     origin = origin
#     destination = destination
#     meters = gmaps.distance_matrix(
#               origins = origin, 
#               destinations = destination, 
#               mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
#     miles = meters * 0.000621371
#     print("Your package will travel an estimated" + {miles} + "miles")



# import googlemaps
# import os
# from dotenv import load_dotenv
# load_dotenv()

# origin = input("warehouse location?")
# destination = input("shipping address?")


# def distance(miles):
    # distance_matrix_arg = distance_matrix_arg
    # meters_to_miles = meters * 0.000621371
    # miles = miles
    # transport_method = {'walking', 'biking', 'driving'}


# class emissions:
#     def __init__(self, co2):
#         self.co2 = co2
#         co2 = d1.miles * w1.shortTon * e1.E
# c1 = emissions(co2)
        
        