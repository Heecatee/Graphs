import sys

sys.path.append('..')
sys.path.append('../..')

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
    graph_utils.print_2d_array("", random_gen.generate_random_connected_weighted_graph(g, 1, 10))


main()
