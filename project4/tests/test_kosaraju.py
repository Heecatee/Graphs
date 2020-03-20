import sys

sys.path.append('..')
sys.path.append('../..')

from graph.directed_graph import DirectedGraph
from graph import directed_graph
import graph.graph_utils as graph_utils


def main():
    n = 7
    test_adj_matrix = [[0 for x in range(n)] for y in range(n)]
    test_adj_matrix[0][1] = 1
    test_adj_matrix[0][2] = 1
    test_adj_matrix[0][4] = 1
    test_adj_matrix[1][0] = 1
    test_adj_matrix[1][2] = 1
    test_adj_matrix[1][4] = 1
    test_adj_matrix[1][3] = 1
    test_adj_matrix[1][6] = 1
    test_adj_matrix[2][5] = 1
    test_adj_matrix[4][6] = 1
    test_adj_matrix[3][6] = 1
    test_adj_matrix[3][1] = 1
    test_adj_matrix[5][1] = 1
    test_adj_matrix[6][5] = 1
    graph_utils.print_2d_array("Example digraph 1", test_adj_matrix)
    c = DirectedGraph.kosaraju_with_adj_matrix(test_adj_matrix)
    print(c)
    test_adj_matrix1 = [[0 for x in range(n)] for y in range(n)]
    test_adj_matrix1[0][1] = 1
    test_adj_matrix1[0][6] = 1
    test_adj_matrix1[6][0] = 1
    test_adj_matrix1[6][1] = 1
    test_adj_matrix1[1][2] = 1
    test_adj_matrix1[2][1] = 1
    test_adj_matrix1[2][3] = 1
    test_adj_matrix1[2][4] = 1
    test_adj_matrix1[4][3] = 1
    test_adj_matrix1[4][5] = 1
    test_adj_matrix1[5][1] = 1
    test_adj_matrix1[5][2] = 1
    graph_utils.print_2d_array("Example digraph 2", test_adj_matrix1)
    c = DirectedGraph.kosaraju_with_adj_matrix(test_adj_matrix1)
    print(c)
    for i in range(len(c)):
        print("Wierzchołek ", i, " należy do składowej nr: ", c[i])

    graph = DirectedGraph()
    graph_utils.print_2d_array("Random digraph", graph.random(7, 0.3))
    c = graph.kosaraju()
    print(c)
    for i in range(len(c)):
        print("Wierzchołek ", i, " należy do składowej nr: ", c[i])


main()
