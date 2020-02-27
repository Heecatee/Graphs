from array import *
import os.path
import sys


def save_to_adjacency_matrix(graph_arr):
    adjacency_matrix = [[0] * get_max_vertex(graph_arr) for i in range(get_max_vertex(graph_arr))]

    for row in graph_arr:
        # row[0] - first vertex, row[1] - second vertex
        if (row[0] >= 0 and row[1] >= 0):
            adjacency_matrix[row[0]][row[1]] = 1
            adjacency_matrix[row[1]][row[0]] = 1

    return adjacency_matrix


def save_to_adjacency_list(graph_arr):
    max_vertex = max(max(x) for x in graph_arr) + 1
    adjacency_list = []

    # index = 0;
    # adjacency_list.append([str(graph_arr[0][0]) + ":"])
    # for i in range(0, len(graph_arr)):
    #     if i > 0 and graph_arr[i - 1][0] != graph_arr[i][0]:
    #         index += 1
    #         adjacency_list.append([str(graph_arr[i][0]) + ":"])
    #     else:
    #         found_before = -1
    #         for j in range(0, graph_arr[i][0]):
    #
    #     if (graph_arr[i][1] >= 0):
    #         adjacency_list[index].append(graph_arr[i][1])

    return adjacency_list


def save_to_incidence_matrix(graph_arr):
    incidence_matrix = [[0] * (len(graph_arr) - get_amount_of_empty_vertex(graph_arr)) for i in range(get_max_vertex(graph_arr))]

    for i in range(0, len(graph_arr) - get_amount_of_empty_vertex(graph_arr)):
        # row[0] - first vertex, row[1] - second vertex
        if (graph_arr[i][0] >= 0 and graph_arr[i][1] >= 0):
            incidence_matrix[graph_arr[i][0]][i] = 1
            incidence_matrix[graph_arr[i][1]][i] = 1

    return incidence_matrix

def get_amount_of_empty_vertex(graph_arr):
    return sum(x.count(-1) for x in graph_arr)

def get_max_vertex(graph_arr):
    return max(max(x) for x in graph_arr) + 1
