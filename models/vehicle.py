from location import Location
class Vehicle(object):
    def __init__(self, lat, lng, name = None, start = None, end = None, duration = None, load = None, type = None):
        self.location = Location(lat, lng, name)
        self.start = start
        self.end = end
        self.duration = duration
        self.load = load
        self.type = type
