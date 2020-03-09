import sys

sys.path.append('..')
sys.path.append('../..')

from graph.graph import graph
from generation import generation
import graph.graph_utils as graph_utils
import operations.conversions as conversions

def main():
    graph_arr = graph.create_from_file().graph_arr

    adj_matrix = generation.save_to_adjacency_matrix(graph_arr)
    adj_list = generation.save_to_adjacency_list(graph_arr)
    inc_matrix = generation.save_to_incidence_matrix(graph_arr)

    graph_utils.print_2d_array("Adjacency matrix", generation.save_to_adjacency_matrix(graph_arr))
    graph_utils.print_2d_array("Adjacency list", generation.save_to_adjacency_list(graph_arr))
    graph_utils.print_2d_array("Incidence matrix", generation.save_to_incidence_matrix(graph_arr))

    print("----------")
    print("")

    # from adjacency matrix:
    adj_list1 = conversions.adjacency_matrix_to_adjacency_list(adj_matrix)
    inc_matrix1 = conversions.adjacency_matrix_to_incident_matrix(adj_matrix)

    graph_utils.print_2d_array("adj matrix to list", adj_list1)
    graph_utils.print_2d_array("adj matrix to inc matrix", inc_matrix1)

    # from adjacency list:
    adj_matrix1 = conversions.adjacency_list_to_adjacency_matrix(adj_list)
    inc_matrix1 = conversions.adjacency_list_to_incident_matrix(adj_list)

    graph_utils.print_2d_array("list to adj matrix", adj_matrix1)
    graph_utils.print_2d_array("list to inc matrix", inc_matrix1)

    # from incidence matrix:
    adj_matrix1 = conversions.incident_matrix_to_adjacency_matrix(inc_matrix)
    adj_list1 = conversions.incident_matrix_to_adjacency_list(inc_matrix)

    graph_utils.print_2d_array("inc matrix to adj matrix", adj_matrix1)
    graph_utils.print_2d_array("inc matrix to list", adj_list1)


main()
