from graph.graph import graph
import operations.conversions as conversions
import random


def generate_random_weights(adjacency_matrix, min_r, max_r):
    random_weighted_graph = []
    for row in adjacency_matrix:
        row.append(random.randrange(min_r, max_r))
        random_weighted_graph.append(row)

    return random_weighted_graph


class WeightedGraph(graph):
    def __init__(self):
        super().__init__()
        self.graph_arr = []

    def generate_randomly_weighted_connected_graph(self):
        connected_adjacency_matrix = conversions.adjacency_list_to_adjacency_matrix(self.largest_component(True))
        return generate_random_weights(connected_adjacency_matrix, 1, 10)

