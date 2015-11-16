import pprint

class Cube(object):
	"""docstring for Cube"""
	def __init__(self, size=3, num_faces=6):
		super(Cube, self).__init__()
		self.size = size
		self.num_faces = num_faces
		self.faces = [Face() for i in xrange(self.num_faces)]

	def __str__(self):
		pprint.pprint(self.faces)

class Face(object):
	"""docstring for Face"""
	def __init__(self, size=3, color=None):
		super(Face, self).__init__()
		self.size = size
		self.color = color
		self.num_pieces = self.size**2
		self.pieces = [Piece() for i in xrange(self.num_pieces)]

	def __str__(self):
		pprint.pprint(self.pieces)
		
class Piece(object):
	"""docstring for Piece"""
	def __init__(self, connections={}):
		super(Piece, self).__init__()
		self.connections = connections

	def __str__(self):
		for k,v in self.connections.items():
			print "%s \t %s" % (k,v)
		