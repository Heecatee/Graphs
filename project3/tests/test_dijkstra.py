import sys

sys.path.append('..')
sys.path.append('../..')

from graph.weighted_graph import WeightedGraph
import operations.conversions as conversions
import graph.graph_utils as graph_utils


def main():
    g = WeightedGraph()

    graph_utils.print_2d_array("Initial data", g.random_connected_weighted_graph())
    g.draw()

    length = len(g.get_adjacency_matrix())
    start_vertex = int(input("Starting vertex (0-" + str(length - 1) + "): "))
    dijkstra_result, distances = g.dijkstra_algorithm(start_vertex)
    graph_utils.print_2d_array("\nDijkstra algorithm output", dijkstra_result)


main()
