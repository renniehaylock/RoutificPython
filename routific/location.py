class Location(object):
  '''
  (String)      name
  (Latitude)    lat
  (Longitude)   lng
  '''
  def __init__(self,lat,lng,id=None,name=None):
    # TODO: Type Checking for lat and lon
    self.id = id
    self.name   = name
    self.lat    = lat
    self.lng    = lng

  '''
  Serialize object to dictionary
  '''
  def toDict(self):
    location = {}

    if self.id:   location["id"] = self.id
    if self.name: location["name"] = self.name
    if self.lat:  location["lat"] = self.lat
    if self.lng:  location["lng"] = self.lng

    return location