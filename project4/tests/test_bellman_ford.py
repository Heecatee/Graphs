import sys

from Graphs.operations import conversions

sys.path.append('..')
sys.path.append('../..')

from graph.directed_graph import DirectedGraph
from graph.weighted_graph import WeightedGraph
import graph.graph_utils as graph_utils
import random


def init(graph, s, d, p):
    for v in range(len(graph)):
        d[v] = sys.maxsize
        p[v] = None
    d[s] = 0


def relax(u, v, w, d, p):
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        p[v] = u


def bellman_ford(graph, s, weights):
    n = len(graph)
    d = [0 for x in range(n)]
    p = [0 for x in range(n)]
    init(graph, s, d, p)
    for i in range(1, n - 1):
        for x in range(n):
            for y in range(n):
                if graph[x][y] != 0:
                    relax(x, y, weights, d, p)
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0:
                if d[y] > d[x] + weights[x][y]:
                    return False, d
    return True, d


def main():
    graph = DirectedGraph()

    graph.random(5, 1)
    c = graph.kosaraju()
    while sum(c) / 5 != 1:
        graph.random(5, 1)
        c = graph.kosaraju()
    matrix = graph.get_adjacency_matrix()
    weights = graph.get_adjacency_matrix()
    for x in range(5):
        for y in range(5):
            if weights[x][y] != 0:
                weights[x][y] = random.randint(-5, 10)
    graph_utils.print_2d_array("Random digraph", matrix)
    graph_utils.print_2d_array("Weights on digraph", weights)
    b, d = bellman_ford(matrix, 0, weights)
    print(b)
    print(d)


main()
