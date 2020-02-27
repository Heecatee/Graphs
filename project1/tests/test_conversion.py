import generation.generation
import conversions.conversions
from array import *
import os.path
import sys

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



    