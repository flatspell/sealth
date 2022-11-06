# estimate carbon involved: W * D * Fe (weight * distance * emissionsFactor) 


# Weight * Distance
ton_miles = weight_short_ton * miles

# emissions factor
emissions_factor = 161.8 #grams CO2 per ton mile

# W * D * Emissions Factor

grams_co2 = weight_short_ton * miles * emissions_factor
