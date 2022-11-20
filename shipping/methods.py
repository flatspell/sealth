
# need weight, distance, emissions_factor
# co2 = shortTon * miles * emissions_factor

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
meters = float(input("Shipping distance in meters?  "))
miles = meters_to_miles(meters)
print("Package will travel {} meters or {} miles" .format(meters, miles))

# emissions factor
emissions_factor = 161.8
print(emissions_factor)

# model:
# co2 = shortTon * miles * emissions_factor
grams_co2 = shortTon * miles * emissions_factor
lbs_co2 = grams_co2 * 0.0022046226

# final output
print("Shipping this package will generate {} grams or {} pounds of co2 emissions." .format(grams_co2, lbs_co2))







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
        
        