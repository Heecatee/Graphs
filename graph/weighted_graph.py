import sys
from graph.graph import graph
from graph.graph import graph_utils
import operations.random_gen as random_gen
import operations.conversions as conversions
import numpy as np


def min_distance(self, dist, visited_vertices):
    min_dist = sys.maxsize

    min_index = -1
    for v in range(self.V):
        if dist[v] < min_dist and visited_vertices[v] is False:
            min_dist = dist[v]
            min_index = v

    return min_index


class WeightedGraph(graph):
    def __init__(self):
        super().__init__()
        self.graph_arr = []

    def random_connected_weighted_graph(self, min_r, max_r):
        n = int(input("Podaj liczbe wierzchołków: "))
        while 1 > 0:
            l = int(input("Podaj liczbe krawędzi: "))
            if l <= (n * n - n) / 2:
                break

        g = np.squeeze(np.asarray(random_gen.generate_random_matrix_with_edges(n, l)))
        # TODO: add largest comp
        weighted_g = random_gen.generate_random_weights(g, 1, 10)

        self.graph_arr = conversions.adjacency_matrix_to_base_format_with_weights(weighted_g)

        return weighted_g

    def dijkstra_algorithm(self, start_vertex):
        adjacency_matrix = self.get_adjacency_matrix()
        size = graph_utils.get_vertices_number(self.graph_arr)

        distances = [sys.maxsize] * size
        distances[start_vertex] = 0
        visited_vertices = [False] * size

        for i in range(size):

            # pick vertex with shortest distance
            u = min_distance(distances, visited_vertices)

            # put the minimum distance vertex in the shortest path tree
            visited_vertices[u] = True

            for v in range(size):
                if adjacency_matrix[u][v] > 0 and visited_vertices[v] is False and distances[v] > distances[u] + \
                        adjacency_matrix[u][v]:
                    distances[v] = distances[u] + adjacency_matrix[u][v]

        return distances
