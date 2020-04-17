import sys

sys.path.append('..')
sys.path.append('../..')

from graph.weighted_graph import WeightedGraph
import operations.conversions as conversions
import graph.graph_utils as graph_utils


def main():
    g = WeightedGraph()

    graph_utils.print_2d_array("Initial data", g.random_connected_weighted_graph(6, 2, 1))
    g.draw()

    graph_utils.print_2d_array("\nDistances matrix", g.get_distances_matrix())


main()
