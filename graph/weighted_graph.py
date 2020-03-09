from graph.graph import graph
import operations.conversions as conversions
import random


def generate_random_weights(adjacency_matrix, min_r, max_r):
    random_weighted_graph = [[0] * len(adjacency_matrix) for i in range(len(adjacency_matrix))]

    for i in range(0, len(adjacency_matrix)):
        for j in range(0, i + 1):
            if adjacency_matrix[i][j] == 1:
                random_weighted_graph[i][j] = random.randrange(min_r, max_r)

    for i in range(0, len(adjacency_matrix)):
        for j in range(0, i + 1):
            random_weighted_graph[j][i] = random_weighted_graph[i][j]

    return random_weighted_graph


class WeightedGraph(graph):
    def __init__(self):
        super().__init__()
        self.graph_arr = []

    def generate_randomly_weighted_connected_graph(self):
        connected_adjacency_matrix = self.graph_arr
        return generate_random_weights(connected_adjacency_matrix, 1, 11)
