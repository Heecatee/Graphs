from array import *
import os.path
import sys
sys.path.append('..')
from generation import generation
from conversions import conversions

def main():

    graph_arr = []
    print("")

    if os.path.isfile("graph.txt" if (len(sys.argv) <= 1) else sys.argv[0]):
        f = open("graph.txt", "r")
        for line in f:
            graph_arr.append([int(line.split(" ")[0]), int(line.split(" ")[1])])
    else:
        print("There is no file with graph data!\n")

    graph_arr.sort(key=lambda x:x[0])

    adj_matrix = generation.save_to_adjacency_matrix(graph_arr)
    adj_list = generation.save_to_adjacency_list(graph_arr)
    inc_matrix = generation.save_to_incidence_matrix(graph_arr)

    print("----------")
    print("")

    #from adjacency matrix:
    adj_list1 = conversions.adjacency_matrix_to_adjacency_list(adj_matrix)
    inc_matrix1 = conversions.adjacency_matrix_to_incident_matrix(adj_matrix)

    generation.print_2D_array("adj matrix to list",adj_list1)
    generation.print_2D_array("adj matrix to inc matrix",inc_matrix1)

    #from adjacency list:
    adj_matrix1 = conversions.adjacency_list_to_adjacency_matrix(adj_list)
    inc_matrix1 = conversions.adjacency_list_to_incident_matrix(adj_list)

    generation.print_2D_array("list to adj matrix",adj_matrix1)
    generation.print_2D_array("list to inc matrix",inc_matrix1)

    #from incidence matrix:

    adj_matrix1 = conversions.incident_matrix_to_adjacency_matrix(inc_matrix)
    adj_list1 = conversions.incident_matrix_to_adjacency_list(inc_matrix)

    generation.print_2D_array("inc matrix to adj matrix",adj_matrix1)
    generation.print_2D_array("inc matrix to list",adj_list1)

main()