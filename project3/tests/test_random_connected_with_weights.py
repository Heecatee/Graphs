import sys

sys.path.append('..')
sys.path.append('../..')

import graph.graph_utils as graph_utils
from graph.weighted_graph import WeightedGraph


def main():
    graph = WeightedGraph().create_from_file_with_instance()
    graph_utils.print_2d_array("Weighted connected graph from file", graph.get_adjacency_matrix())

    graph.random_connected_weighted_graph()
    graph.draw()
    graph_utils.print_2d_array("Randomly weighted connected graph", graph.get_adjacency_matrix())


main()
