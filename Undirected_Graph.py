class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = dict()

	def addNeighbor(self, v, w):
		if v not in self.neighbors:
			self.neighbors[v] = w
			# self.neighbors.sort()

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def addEdge(self, u, v, w):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].addNeighbor(v, w)
            self.vertices[v].addNeighbor(u, w)
            return True
        else:
            return False

    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))