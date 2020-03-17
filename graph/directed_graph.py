from graph.weighted_graph import WeightedGraph
from graph.graph import get_max_vertex
from graph.graph import get_amount_of_empty_vertex
import operations.random_gen as random_gen
import operations.conversions as conversions
import random


class DirectedGraph(WeightedGraph):

    # graph_arr for digraph: [start_vertex, end_vertex, weight]
    def __init__(self):
        super().__init__()
        self.graph_arr = []

    def get_adjacency_matrix(self):
        adjacency_matrix = [[0] * get_max_vertex(self.graph_arr) for i in range(get_max_vertex(self.graph_arr))]

        for row in self.graph_arr:
            weight = 1
            if len(row) > 2:
                weight = row[2]

            if row[0] >= 0 and row[1] >= 0:
                adjacency_matrix[row[0]][row[1]] = weight

        return adjacency_matrix

    def get_incidence_matrix(self):
        incidence_matrix = [[0] * (len(self.graph_arr) - get_amount_of_empty_vertex(self.graph_arr)) for i
                            in
                            range(get_max_vertex(self.graph_arr))]

        for i in range(0, len(self.graph_arr) - get_amount_of_empty_vertex(self.graph_arr)):
            # row[0] - first vertex, row[1] - second vertex
            if self.graph_arr[i][0] >= 0 and self.graph_arr[i][1] >= 0:
                incidence_matrix[self.graph_arr[i][0]][i] = 1
                incidence_matrix[self.graph_arr[i][1]][i] = -1

        return incidence_matrix

    def random(self, vertex_number, edge_probability):
        self.graph_arr = conversions.adjacency_matrix_to_base_format_with_weights(
            random_gen.generate_random_matrix_with_probability(vertex_number, edge_probability)
        )

        new_graph = []
        for row in self.graph_arr:
            tmp = row[:2]
            row[:2] = random.sample(tmp, len(tmp))
            new_graph.append(row)

        self.graph_arr = new_graph
        print(new_graph)

        return self.get_adjacency_matrix()
