from location import Location
import json

class Vehicle(object):
    def __init__(self, startId, startLat, startLng, endId, endLat, endLng, startName = None, endName = None, shiftStart = None, shiftEnd = None, capacity = None, speed = None, type = None, strictStart = None, minVisits = None, breakStart = None, breakEnd = None, breakDuration = None):
        self.startLocation = Location(startLat, startLng, startId, startName)
        if !endId and !endLat and !endLng:
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

    '''
    Serialize object to dictionary
    '''
    def toDict(self):
      vehicle = {}

      if self.startLocation:  vehicle["start_location"] = self.startLocation.toDict()
      if self.endLocation:    vehicle["end_location"] = self.endLocation.toDict()
      if self.shiftStart:     vehicle["shift_start"] = self.shiftStart
      if self.shiftEnd:       vehicle["shift_end"] = self.shiftEnd
      if self.capacity:       vehicle["capacity"] = self.capacity
      if self.speed:          vehicle["speed"] = self.speed
      if self.type:           vehicle["type"] = self.type
      if self.strictStart:    vehicle["strict_start"] = self.strictStart
      if self.minVisits:      vehicle["min_visits"] = self.minVisits
      if self.breakStart:     vehicle["break_start"] = self.breakStart
      if self.breakEnd:       vehicle["break_end"] = self.breakEnd
      if self.breakDuration:  vehicle["break_duration"] = self.breakDuration

      return vehicle

    def toJson(self):
      return json.dumps(self.toDict())