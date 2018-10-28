from collections import defaultdict
from collections import namedtuple
 
Edge = namedtuple('Edge', ('source', 'target', 'weight'))
 
class Graph:
    def __init__(self, vertices, edges=tuple()):
        self.vertices = vertices
        self.incident_edges = defaultdict(list)
 
        for edge in edges:
            self.add_edge(edge[0], edge[1], 1 if len(edge) == 2 else edge[2])
 
    def add_edge(self, u, v, weight=1):
        self.incident_edges[u].append(Edge(u, v, weight))
        self.incident_edges[v].append(Edge(v, u, weight))
 
    def edge(self, u, v):
        return [e for e in self.incident_edges[u] if e.target == v][0]

'''
Graph 
 
    a       k
     b     j
      cfghi
     d     l
    e       m
'''
G = Graph(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm'],
          [
               ('a', 'b'),
               ('b', 'c'),
               ('c', 'd'),
               ('d', 'e'),
               ('c', 'f'),
               ('f', 'g'),
               ('g', 'h'),
               ('h', 'i'),
               ('i', 'j'),
               ('j', 'k'),
               ('i', 'l'),
               ('l', 'm'),
          ])
print("Vertices of graph:")
print(G.vertices)

print("Incident Edges:")
print(G.incident_edges)

print("Edge b -> c")
print(G.edge('b','c'))