import sys

sys.path.append('..')
sys.path.append('../..')

from graph.directed_graph import DirectedGraph
import graph.graph_utils as graph_utils
import random


def PageRank_random(graph, N, d, vertex):
    n = graph_utils.get_vertices_number(graph)
    pagerank_vector = [0 for x in range(n)]
    pagerank_vector[vertex] += 1
    matrix = graph.get_adjacency_matrix()
    for i in range(N):
        if random.random() > d:
            while 1:
                next_vertex = random.randrange(n)
                if matrix[vertex][next_vertex] != 0:
                    vertex = next_vertex
                    pagerank_vector[next_vertex] += 1
                    break
        else:
            vertex = random.randrange(n)
            pagerank_vector[vertex] += 1
    for i in range(n):
        pagerank_vector[i] = pagerank_vector[i] / N
    return pagerank_vector


def PageRank_iteration(graph, N, d):
    n = graph_utils.get_vertices_number(graph)
    matrix_A = graph.get_adjacency_matrix()
    d_i = [0 for x in range(n)]
    p = [1 / n for x in range(n)]
    matrix_P = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix_A[i][j] != 0:
                d_i[i] += 1
    for i in range(n):
        for j in range(n):
            matrix_P[i][j] = (1 - d) * matrix_A[i][j] / d_i[i] + d / n
    # ------------Dodać zbieżność!---------------#
    for i in range(N):
        p = graph_utils.multiply_vector_matrix(p, matrix_P)
    # -------------------------------------------#
    return p


def main():
    alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    graph = DirectedGraph()
    graph.create_from_file_with_instance()
    graph_utils.print_2d_array("Adjacency matrix", graph.get_adjacency_matrix())

    print("Błądzenie przypadkowe:")
    print("#########################")
    vec_rand = PageRank_random(graph, 100000, 0.15, 1)
    for i in range(graph_utils.get_vertices_number(graph)):
        print(alfabet[i], "==> PageRank = ", vec_rand[i])
    print("#########################")
    print("\n\nWektor obsadzeń")
    print("#########################")
    vec_it = PageRank_iteration(graph, 54, 0.15)

    for i in range(graph_utils.get_vertices_number(graph)):
        print(alfabet[i], "==> PageRank = ", vec_it[i])
    print("#########################")

    graph1 = DirectedGraph()
    graph1.create_from_file_with_instance('graph1.txt')
    graph_utils.print_2d_array("Adjacency matrix", graph1.get_adjacency_matrix())
    print("Błądzenie przypadkowe:")
    print("#########################")
    vec_rand = PageRank_random(graph1, 1000000, 0.15, 1)
    for i in range(graph_utils.get_vertices_number(graph1)):
        print(alfabet[i], "==> PageRank = ", vec_rand[i])
    print("#########################")
    print("\n\nWektor obsadzeń")
    print("#########################")
    vec_it = PageRank_iteration(graph1, 31, 0.15)

    for i in range(graph_utils.get_vertices_number(graph1)):
        print(alfabet[i], "==> PageRank = ", vec_it[i])
    print("#########################")


main()
