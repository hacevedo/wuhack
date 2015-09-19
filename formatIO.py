import collections

class Destination(collections.namedtuple('Destination', ['lat', 'long'])):
	def __new__(cls, lat, long, id):
		numLat = float(lat)
		numLong = float(long)
        	self = super(Destination, cls).__new__(cls, numLat, numLong)
		self.id = id
		return self


