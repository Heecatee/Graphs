import sys

sys.path.append('..')
sys.path.append('../..')

import graph.graph_utils as graph_utils
from graph.weighted_graph import WeightedGraph


def main():
    graph = WeightedGraph()
    graph.random_connected_weighted_graph(8, 1, 10)
    graph.draw()
    graph_utils.print_2d_array("Randomly weighted connected graph", graph.get_adjacency_matrix())


main()
