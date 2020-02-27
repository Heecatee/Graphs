import os.path
import sys
sys.path.append('..')
from generation import generation

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

    generation.print_2D_array("Initial data", graph_arr)
    generation.save_to_adjacency_matrix(graph_arr)
    generation.save_to_adjacency_list(graph_arr)
    generation.save_to_incidence_matrix(graph_arr)
    