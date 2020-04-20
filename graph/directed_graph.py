from graph.weighted_graph import WeightedGraph
from graph.graph import get_max_vertex
from graph.graph import get_amount_of_empty_vertex
import operations.random_gen as random_gen
import operations.conversions as conversions
import random
from graph import graph_utils


# ------------------ Functions for Kosaraju Algorithm ---------------------#
def DFS_visit(v, g_matrix, d, f, t):
    t += 1
    d[v] = t
    for u in range(len(g_matrix)):
        if g_matrix[v][u] == 1 and d[u] == -1:
            DFS_visit(u, g_matrix, d, f, t)
    t += 1
    f[v] = t


def components_r(nr, v, g_matrix_transposed, comp):
    for u in range(len(g_matrix_transposed)):
        if g_matrix_transposed[v][u] == 1 and comp[u] == -1:
            comp[u] = nr
            components_r(nr, u, g_matrix_transposed, comp)


# ------------------------------------------------------------------------#


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
            if self.graph_arr[i][0] == self.graph_arr[i][1] and self.graph_arr[i][1] >= 0:
                incidence_matrix[self.graph_arr[i][0]][i] = 1
                incidence_matrix[self.graph_arr[i][1]][i] = 1
            elif self.graph_arr[i][0] >= 0 and self.graph_arr[i][1] >= 0:
                incidence_matrix[self.graph_arr[i][0]][i] = 1
                incidence_matrix[self.graph_arr[i][1]][i] = -1


        return incidence_matrix

    def get_adjacency_list(self):
        max_vertex = max(max(x) for x in self.graph_arr) + 1
        tmp_list = {}
        adjacency_list = []

        # for i in range(0, len(self.graph_arr)):

        for row in self.graph_arr:
            weight = ''
            if len(row) > 2:
                weight = '(' + str(row[2]) + ')'

            if row[0] in tmp_list.keys():
                if row[1] >= 0:
                    tmp_list[row[0]].append(str(row[1]) + weight)
            else:
                tmp_list[row[0]] = []
                if row[1] >= 0:
                    tmp_list[row[0]].append(str(row[1]) + weight)

        for index, key in enumerate(tmp_list):
            adjacency_list.append([str(key) + ":"])
            for vertex in tmp_list[key]:
                adjacency_list[index].append(vertex)

        return adjacency_list

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

        return self.get_adjacency_matrix()
    
    def kosaraju(self):
        g_matrix = self.get_adjacency_matrix()
        n = len(g_matrix)
        d = [-1 for i in range(n)]
        f = [-1 for i in range(n)]
        t = 0
        for v in range(n):
            if d[v] == -1:
                DFS_visit(v, g_matrix, d, f, t)
        g_matrix_transposed = graph_utils.transpose_matrix(g_matrix)
        nr = 0
        comp = [-1 for i in range(n)]
        for v in range(n):
            if comp[v] == -1:
                nr += 1
                comp[v] = nr
                components_r(nr, v, g_matrix_transposed, comp)
        return comp

    def kosaraju_with_adj_matrix(g_matrix):
        n = len(g_matrix)
        d = [-1 for i in range(n)]
        f = [-1 for i in range(n)]
        t = 0
        for v in range(n):
            if d[v] == -1:
                DFS_visit(v, g_matrix, d, f, t)
        g_matrix_transposed = graph_utils.transpose_matrix(g_matrix)
        nr = 0
        comp = [-1 for i in range(n)]
        for v in range(n):
            if comp[v] == -1:
                nr += 1
                comp[v] = nr
                components_r(nr, v, g_matrix_transposed, comp)
        return comp
