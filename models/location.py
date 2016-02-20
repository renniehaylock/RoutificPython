class Location(object):
  def __init__(self,lat,lng,id=None,name=None):
    self.id = id
    self.name   = name
    self.lat    = lat
    self.lng    = lng
