import sys

sys.path.append('..')
sys.path.append('../..')

from graph.graph import graph
import graph.graph_utils as graph_utils


def main():
    graph_arr = graph.create_from_file().graph_arr

    graph_utils.print_2d_array("Initial data", graph_arr)

    graph_utils.print_2d_array("Adjacency matrix", graph.create_from_file().get_adjacency_matrix())
    graph_utils.print_2d_array("Adjacency list", graph.create_from_file().get_adjacency_list())
    graph_utils.print_2d_array("Incidence matrix", graph.create_from_file().get_incidence_matrix())


main()