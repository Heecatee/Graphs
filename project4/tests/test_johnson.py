import sys

sys.path.append('..')
sys.path.append('../..')

from graph.directed_graph import DirectedGraph
from graph import weighted_graph as WeightedGraph
import graph.graph_utils as graph_utils
import random


def main():
    graph = DirectedGraph()
    n = 5
    graph.correct_random(n, 0.8)
    c = graph.kosaraju()
    while sum(c) / n != 1:
        graph.random(n, 1)
        c = graph.kosaraju()
    print(c)

    matrix = graph.get_adjacency_matrix()
    weights = graph.get_adjacency_matrix()
    for x in range(n):
        for y in range(n):
            if weights[x][y] != 0:
                weights[x][y] = random.randint(-5, 10)

    graph_utils.print_2d_array("Random digraph", matrix)
    graph_utils.print_2d_array("Weights on digraph", weights)
    graph_utils.print_2d_array("Johnson's Matrix", WeightedGraph.johnson(matrix, weights))
    print("\nTest z zajęć \n")
    test_matrix = [[0, 1, 1], [1, 0, 0], [0, 1, 0]]
    test_weights = [[0, -1, -4], [4, 0, 0], [0, 2, 0]]
    graph_utils.print_2d_array("Johnson's Matrix", WeightedGraph.johnson(test_matrix, test_weights))


main()
