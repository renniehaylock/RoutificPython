from location import Location
class Vehicle(object):
    def __init__(self, startId, startLat, startLng, startName = None, endId, endLat, endLng, endName = None, shiftStart = None, shiftEnd = None, capacity = None, speed = None, type = None, strictStart = None, minVisits = None, breakStart = None, breakEnd = None, breakDuration = None):
        self.startLocation = Location(startLat, startLng, startId, startName)
        self.endLocation = Location(endLat, endLng, endId, endName)
        self.shiftStart = shiftStart
        self.shiftEnd = shiftEnd
        self.capacity = capacity
        self.speed = speed
        self.type = type
        self.strictStart = strictStart
        self.minVisits = minVisits
        self.breakStart = breakStart
        self.breakEnd = breakEnd
        self.breakDuration = breakDuration
