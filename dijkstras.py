# Dijkstra's algorithm re-implementation

import sys

class Vertex:
	def __init__(self, label, edges):
		self.label = label
		self.edges = edges
		self.sp = sys.maxsize

class Edge:
	def __init__(self, src, dst, weight):
		self.src = src
		self.dst = dst
		self.weight = weight
		

class Graph:
	def __init__(self, vertexes):
		self.graph = {}
		for i in vertexes:
			self.graph.update({i.label: i})

	def print_shortest_paths(self):
		for i in self.graph:
			print(i, self.graph[i].sp)
		return
	def dijkstras(self, start, end):
		if self.graph.get(start, -1) == -1 or self.graph.get(end, -1) == -1:
			return -1
		
		from queue import PriorityQueue
		q = PriorityQueue()

		self.graph[start].sp = 0
		q.put((self.graph[start].sp, self.graph[start]))
		visited = set()
		while q.qsize() != 0:
			print(q.qsize())	
			cur = q.get()[1]
			for edge in cur.edges:
				vert = self.graph[edge.dst]
				vert.sp = min(vert.sp, cur.sp + edge.weight)
				if vert not in visited:
					visited.add(vert)
					q.put((vert.sp, vert))
		self.print_shortest_paths()



# Playground
aedges = [	
			Edge("A", "D", 7), 
			Edge("A", "C", 4),
			Edge("A", "B", 3), 
		]
bedges = [
			Edge("B", "C", 1),
			Edge("B", "F", 5),
			Edge("B", "A", 3)
		]
cedges = [
			Edge("C", "D", 2),
			Edge("C", "F", 6),
			Edge("C", "B", 1),
			Edge("C", "A", 4)
		]
dedges = [
			Edge("D", "E", 3),
			Edge("D", "G", 6),
			Edge("D", "A", 7),
			Edge("D", "C", 2)
		]
eedges = [
			Edge("E", "G", 3),
			Edge("E", "H", 4),
			Edge("E", "F", 1),
			Edge("E", "D", 3)
		]
fedges = [
			Edge("F", "H", 8),
			Edge("F", "E", 1),
			Edge("F", "C", 6),	
			Edge("F", "B", 5)
		]
gedges = [
			Edge("G", "H", 2),
			Edge("G", "D", 6),
			Edge("G", "E", 3)
		]
hedges = [
			Edge("H", "G", 2),
			Edge("H", "E", 4),
			Edge("H", "F", 8)
		]
A = Vertex("A", aedges)
B = Vertex("B", bedges)
C = Vertex("C", cedges)
D = Vertex("D", dedges)
E = Vertex("E", eedges)
F = Vertex("F", fedges)
G = Vertex("G", gedges)
H = Vertex("H", hedges)
vertexes = [A, B, C, D, E, F, G, H]
g = Graph(vertexes)

g.dijkstras("A", "H")


