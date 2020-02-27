from array import *
import os.path
import sys


def load_graph_from_file():
    graph_arr = []

    if os.path.isfile("graph.txt" if (len(sys.argv) <= 1) else sys.argv[0]):
        f = open("graph.txt", "r")
        for line in f:
            if (len(line.split(" ")) > 1):
                graph_arr.append([int(line.split(" ")[0]), int(line.split(" ")[1])])
            elif (len(line.split(" ")) > 0):
                graph_arr.append([int(line.split(" ")[0]), ""])
            else:
                graph_arr.append(["", ""])
    else:
        print("There is no file with graph data!\n")

    graph_arr.sort(key=lambda x:x[0])

    return graph_arr

def print_2D_array(title, arr):
    print(title + ":")
    for row in arr:
        for col in row:
            print(col, end = " ")
        print("")
    print("")
