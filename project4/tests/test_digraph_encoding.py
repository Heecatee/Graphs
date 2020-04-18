import sys

sys.path.append('..')
sys.path.append('../..')

from graph.directed_graph import DirectedGraph
import graph.graph_utils as graph_utils


def main():
    graph = DirectedGraph()
    graph.create_from_file_with_instance()

    graph_utils.print_2d_array("Initial data", graph.graph_arr)
    graph_utils.print_2d_array("Adjacency matrix", graph.get_adjacency_matrix())
    graph_utils.print_2d_array("Incidence matrix", graph.get_incidence_matrix())
    graph_utils.print_2d_array("Adjacency list", graph.get_adjacency_list())


main()
