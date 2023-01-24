shipping outline

post-purchase app
	just like ecocart
	plugin?
estimate carbon involved: W * D * Fe (weight * distance * factor of emissions) 
	Weight
		from product vendor
	Distance
		from api? google?
		Google Distance Matrix API
			doc page: https://developers.google.com/maps/documentation/javascript/distancematrix
		key = API_key in sealth.env
		need distance on road, not crow flight
		
	Factor of Emissions
		from mode of shipping
			air, train, truck
			start with trucks only
				many types of trucks!
		pull numbers from Green Freight Handbook
			https://storage.googleapis.com/scsc/Green%20Freight/EDF-Green-Freight-Handbook.pdf
			from GRH: 'All Trucks' by weight = 161.8 grams CO2 per short ton per mile
					     2000 lbs  = 161.8 grams CO2 per  mile travelled
					     1 lbs =  0.0809 grams CO2 per mile travelled
purchase carbon offset
	local options?
		Washington
	
starter model:
	weight:
		input weight from vendor
		use 1 lb package for starter
	distance:
		assume vendor of product located in metro Seattle
		input destination zipcode
		pull distance from origin to destination
	emissions factor