import sys

sys.path.append('../..')
from graph.graph import graph
import graph.graph_utils as graph_utils


def main():
    graph1 = graph.create_from_file("graph_hamilton.txt")
    # print(graph_utils.get_vertices_number(graph1))
    n = graph_utils.get_vertices_number(graph1)
    tab = [-1 for i in range(n)]
    tab[0] = 0
    graph.hamilton_cycle(graph1.get_adjacency_matrix(), 1, n, tab)
    graph1.draw()


main()
