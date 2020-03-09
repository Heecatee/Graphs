import sys

sys.path.append('..')
sys.path.append('../..')

from graph.graph import graph
from graph.weighted_graph import WeightedGraph
import graph.graph_utils as graph_utils
import operations.random_gen as random_gen
import numpy as np


def main():
    n = int(input("Podaj liczbe wierzchołków: "))
    while 1 > 0:
        l = int(input("Podaj liczbe krawędzi: "))
        if l <= (n * n - n) / 2:
            break

    g = np.squeeze(np.asarray(random_gen.generate_random_matrix_with_edges(n, l)))
    weighted_graph = WeightedGraph()
    weighted_graph.graph_arr = g
    print(g)

    randomly_weighted_graph = weighted_graph.generate_randomly_weighted_connected_graph()
    graph_utils.print_2d_array("", randomly_weighted_graph)


main()
