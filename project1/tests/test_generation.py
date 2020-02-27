from array import *
import sys
sys.path.append('..')
from generation import generation
from conversions import conversions
import utils

def main():
    graph_arr = utils.load_graph_from_file()

    utils.print_2D_array("Initial data", graph_arr)

    utils.print_2D_array("Adjacency matrix", generation.save_to_adjacency_matrix(graph_arr))
    utils.print_2D_array("Adjacency list", generation.save_to_adjacency_list(graph_arr))
    utils.print_2D_array("Incidence matrix", generation.save_to_incidence_matrix(graph_arr))

main()
