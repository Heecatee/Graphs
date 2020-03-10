import sys

sys.path.append('..')
sys.path.append('../..')

import graph.graph_utils as graph_utils
from graph.weighted_graph import WeightedGraph


def main():
    graph_utils.print_2d_array("Randomly weighted connected graph", WeightedGraph().random_connected_weighted_graph(1, 10))


main()
