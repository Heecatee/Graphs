import sys

sys.path.append('..')
sys.path.append('../..')

import graph.graph_utils as graph_utils
from graph.weighted_graph import WeightedGraph


def main():
    graph = WeightedGraph().create_from_file_with_instance()

    graph.random_connected_weighted_graph(9)
    graph_utils.print_2d_array("Randomly weighted connected graph", graph.get_adjacency_matrix())
    graph.draw()

main()
