from array import *
import sys
sys.path.append('..')
from generation import generation
from conversions import conversions
import utils

def main():

    graph_arr = utils.load_graph_from_file()

    adj_matrix = generation.save_to_adjacency_matrix(graph_arr)
    adj_list = generation.save_to_adjacency_list(graph_arr)
    inc_matrix = generation.save_to_incidence_matrix(graph_arr)

    
    utils.print_2D_array("Adjacency matrix", generation.save_to_adjacency_matrix(graph_arr))
    utils.print_2D_array("Adjacency list", generation.save_to_adjacency_list(graph_arr))
    utils.print_2D_array("Incidence matrix", generation.save_to_incidence_matrix(graph_arr))

    print("----------")
    print("")

    #from adjacency matrix:
    adj_list1 = conversions.adjacency_matrix_to_adjacency_list(adj_matrix)
    inc_matrix1 = conversions.adjacency_matrix_to_incident_matrix(adj_matrix)

    utils.print_2D_array("adj matrix to list", adj_list1)
    utils.print_2D_array("adj matrix to inc matrix", inc_matrix1)

    #from adjacency list:
    adj_matrix1 = conversions.adjacency_list_to_adjacency_matrix(adj_list)
    inc_matrix1 = conversions.adjacency_list_to_incident_matrix(adj_list)

    utils.print_2D_array("list to adj matrix", adj_matrix1)
    utils.print_2D_array("list to inc matrix", inc_matrix1)

    #from incidence matrix:
    adj_matrix1 = conversions.incident_matrix_to_adjacency_matrix(inc_matrix)
    adj_list1 = conversions.incident_matrix_to_adjacency_list(inc_matrix)

    utils.print_2D_array("inc matrix to adj matrix", adj_matrix1)
    utils.print_2D_array("inc matrix to list", adj_list1)

main()
