import math
import heapq


'''
Dijkstra's algorithm with associated metadata to compute
all shortest paths
'''
class DijkstraOutput:
    def __init__(self, graph, start):
        self.start = start
        self.graph = graph
        
        # the smallest distance from the start to the destination v
        self.distance_from_start = {v: math.inf for v in graph.vertices}
        self.distance_from_start[start] = 0

        # a list of predecessor edges for each destination
        # to track a list of possibly many shortest paths
        self.predecessor_edges = {v: [] for v in graph.vertices}

    def found_shorter_path(self, vertex, edge, new_distance):
        # update the solution with a newly found shorter path
        self.distance_from_start[vertex] = new_distance

        if new_distance < self.distance_from_start[vertex]:
            self.predecessor_edges[vertex] = [edge]
        else:  # tie for multiple shortest paths
            self.predecessor_edges[vertex].append(edge)

    def path_to_destination_contains_edge(self, destination, edge):
        predecessors = self.predecessor_edges[destination]
        if edge in predecessors:
            return True
        return any(self.path_to_destination_contains_edge(e.source, edge)
                   for e in predecessors)

    def sum_of_distances(self, subset=None):
        subset = subset or self.graph.vertices
        return sum(self.distance_from_start[x] for x in subset)   
