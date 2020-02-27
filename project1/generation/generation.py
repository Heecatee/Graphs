from array import *
import os.path
import sys


def save_to_adjacency_matrix(graph_arr):
    max_vertex = max(max(x) for x in graph_arr)
    adjacency_matrix = [[0] * max_vertex for i in range(max_vertex)]

    for row in graph_arr:
        # row[0] - first vertex, row[1] - second vertex
        adjacency_matrix[row[0] - 1][row[1] - 1] = 1
        adjacency_matrix[row[1] - 1][row[0] - 1] = 1

    print_2D_array("Adjacency matrix", adjacency_matrix)
    return adjacency_matrix


def save_to_adjacency_list(graph_arr):
    max_vertex = max(max(x) for x in graph_arr)
    adjacency_list = []

    index = 0;
    adjacency_list.append([str(graph_arr[0][0]) + ":"])
    for i in range(0, len(graph_arr)):
        if i > 0 and graph_arr[i - 1][0] != graph_arr[i][0]:
            index += 1
            adjacency_list.append([str(graph_arr[i][0]) + ":"])
        adjacency_list[index].append(graph_arr[i][1])

    print_2D_array("Adjacency list", adjacency_list)
    return adjacency_list


def save_to_incidence_matrix(graph_arr):
    max_vertex = max(max(x) for x in graph_arr)
    incidence_matrix = [[0] * len(graph_arr) for i in range(max_vertex)]

    for i in range(0, len(graph_arr)):
        # row[0] - first vertex, row[1] - second vertex
        incidence_matrix[graph_arr[i][0] - 1][i] = 1
        incidence_matrix[graph_arr[i][1] - 1][i] = 1

    print_2D_array("Incidence matrix", incidence_matrix)
    return incidence_matrix


def print_2D_array(title, arr):
    print(title + ":")
    for row in arr:
        for col in row:
            print(col, end = " ")
        print("")
    print("")
