import sys
from graph.graph import graph
from graph.graph import graph_utils
import operations.random_gen as random_gen
import operations.conversions as conversions
import numpy as np


def min_distance(size, dist, visited):
    min_dist = sys.maxsize
    min_index = -1

    for vertex in range(size):
        if dist[vertex] < min_dist and visited[vertex] is False:
            min_dist = dist[vertex]
            min_index = vertex

    return min_index


class WeightedGraph(graph):
    def __init__(self):
        super().__init__()
        self.graph_arr = []

    def random_connected_weighted_graph(self, vertices_number=7, max_edges=2, min_edges=1):
        random_g = None
        try_count = 0

        while random_g is None or (not random_g.is_connected()):
            if try_count % 5 == 0 and try_count > 0:
                max_edges += 1
            try:
                random_g, random_c = graph().create_random_euler(vertices_number, max_edges, min_edges)
            except:
                print("")

            try_count += 1

        weighted_g = random_gen.generate_random_weights(random_g.get_adjacency_matrix(), 1, 10)

        self.graph_arr = conversions.adjacency_matrix_to_base_format_with_weights(weighted_g)

        return weighted_g

    def dijkstra_algorithm(self, start_vertex):
        adjacency_matrix = self.get_adjacency_matrix()
        size = graph_utils.get_vertices_number(self)

        visited_vertices = []

        distances = [sys.maxsize] * size
        distances[start_vertex] = 0
        visited_vertices = [False] * size
        last_vertex = [-1] * size

        for i in range(size):

            # pick vertex with shortest distance
            u = min_distance(size, distances, visited_vertices)

            # put the minimum distance vertex in the shortest path tree
            visited_vertices[u] = True

            for v in range(size):
                if adjacency_matrix[u][v] > 0 and distances[v] > distances[u] + adjacency_matrix[u][v]:
                    distances[v] = distances[u] + adjacency_matrix[u][v]
                    last_vertex[v] = u

        ordered_vertices = []
        for i in range(size):
            v = last_vertex[i]
            ordered_vertices.append(str(i))
            if v != -1:
                ordered_vertices[i] += "-" + str(v)
            while v != start_vertex and v != -1:
                ordered_vertices[i] += "-" + str(last_vertex[v])
                v = last_vertex[last_vertex[v]]

        result = []
        vertex = 0
        for dist in distances:
            result.append(["d(" + str(vertex) + ") =", dist, "==>", ordered_vertices[vertex]])
            vertex += 1

        distances[distances.index(min(distances))] = sys.maxsize
        minimum = distances.index(min(distances))
        result.append(["---- minimum distance =", "d(" + str(minimum) + ")"])
        return result, distances

    def get_distances_matrix(self):
        distances_matrix = []
        size = graph_utils.get_vertices_number(self)

        for i in range(0, size):
            ignore, distances = self.dijkstra_algorithm(i)
            distances[distances.index(max(distances))] = 0
            distances_matrix.append(distances)

        return distances_matrix
