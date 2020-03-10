from array import *
import sys
sys.path.append('..')
sys.path.append('../..')
from graph.graph import graph
from generation import generation
import graph.graph_utils as graph_utils

def main():
    graph_arr = graph.create_from_file().graph_arr

    graph_utils.print_2d_array("Initial data", graph_arr)

    graph_utils.print_2d_array("Adjacency matrix", generation.save_to_adjacency_matrix(graph_arr))
    graph_utils.print_2d_array("Adjacency list", generation.save_to_adjacency_list(graph_arr))
    graph_utils.print_2d_array("Incidence matrix", generation.save_to_incidence_matrix(graph_arr))

main()
