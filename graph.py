class Vector(object):

	"""A vector for the Timbot's graph-map, consisting of degrees and magnitude."""

	def __init__(self, deg, mag):
		self.degrees = deg
		self.magnitude = mag
	
	def __str__(self):
		return 'Degrees: ' + str(self.degrees) + '\nMagnitude: ' + str(self.magnitude)		

class Edge(object):

	"""An edge for the Timbot's graph-map, containing a vector object and a reference to the vertex they represent."""

	def __init__(self, vect,vert):
		self.vector = vect
		self.vertex = vert

	def __str__(self):
		return 'Vector: \n' + str(self.vector) + '\nVertex Coordinates: (' + str(self.vertex.x) + ',' + str(self.vertex.y) + ',' + str(self.vertex.z) + ')'

class Vertex(object):

	"""A Vertex for the Timbot's graph-map, containing (x,y,z) coordinates, a confidence percentage, a room check and an edge list."""

	def __init__(self, x, y, z, conf):
		self.isRoom = False
		self.x = x
		self.y = y
		self.z = z
		self.confidence = conf
		self.edge_list = []

	def set_as_room(self):
		self.isRoom = True

	def add_edge(self, edge):
		self.edge_list.append(edge)

	def __str__(self):
		coord = 'Coordinates: (' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) +')'
		conf = 'Confidence: ' + str(self.confidence)
		rm = 'Room? ' + str(self.isRoom)
		el = ''
		for e in self.edge_list:
			el += '\nEdge{\n'
			el += str(e) + '\n}'
		return coord + '\n' + conf + '\n' + rm + el


class Graph(object):
	
	"""The graph-map for the Timbot."""

	def __init__(self):
		self.vertex_list = []

	def add_vertex(self, vertex):
		self.vertex_list.append(vertex)

	def form_edge(self,vertex_one,vertex_two,vector):
		vertex_one.add_edge(Edge(vector,vertex_two))
		vertex_two.add_edge(Edge(vector,vertex_one))

print Vector.__doc__
print Edge.__doc__
print Vertex.__doc__
print Graph.__doc__
