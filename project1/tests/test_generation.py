from array import *
import sys
sys.path.append('..')
sys.path.append('../..')
from graph.graph import graph
from generation import generation
from tests import utils

def main():
    graph_arr = graph.create_from_file().graph_arr

    utils.print_2D_array("Initial data", graph_arr)

    utils.print_2D_array("Adjacency matrix", generation.save_to_adjacency_matrix(graph_arr))
    utils.print_2D_array("Adjacency list", generation.save_to_adjacency_list(graph_arr))
    utils.print_2D_array("Incidence matrix", generation.save_to_incidence_matrix(graph_arr))

main()
