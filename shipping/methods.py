#
# origin, destination, miles, weight, emissions factor


class Carbon:
    def __init__(self, origin, destination, miles, weight, eFactor):
        self.origin = origin
        self.destination = destination
        self.miles = miles
        self.weight = weight
        self.eFactor = eFactor
