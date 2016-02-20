from visit import Visit
from vehicle import Vehicle
from urllib2 import Urllib2

ROUTIFIC_URL = "https://api.routific.com/v1/vrp"

class Routific(object):
    def __init__(self, token):
        self.token = token
        self.visits = []
        self.fleet = []

    def addVisit(self, lat,lng,name=None,start=None,end=None,duration=None,load=None,type=None):
        self.visit.append(Visit(lat,lng,name,start,end,duration,load,type))

    def addVehicle(self, startId, startLat, startLng, startName = None, endId = None, endLat = None, endLng = None, endName = None, shiftStart = None, shiftEnd = None, capacity = None, speed = None, type = None, strictStart = None, minVisits = None, breakStart = None, breakEnd = None, breakDuration = None):
        self.fleet.append(Vehicle(startId, startLat, startLng, startName, endId, endLat, endLng, endName, shiftStart, shiftEnd, capacity, speed, type, strictStart, minVisits, breakStart, breakEnd, breakDuration))

    def fetchRoute(self):
        req = Urllib2.Request(ROUTIFIC_URL)
        req.add_header('Content-Type', 'application/JSON')
        req.add_header('Authorization', self.token)
        # TODO: Add request data here
        return Urllib2.urlopen(req).read()
