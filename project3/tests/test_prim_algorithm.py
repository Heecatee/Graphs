import sys

sys.path.append('..')
sys.path.append('../..')

import graph.graph_utils as graph_utils
from graph.weighted_graph import WeightedGraph


def main():
    g = WeightedGraph()
    gr = WeightedGraph.create_from_file("example_graph.txt")
    g.graph_arr = gr.graph_arr
    g.prim_algorithm()
    g.draw()
    graph_utils.print_2d_array("Adjacency Matrix For Tree", g.get_adjacency_matrix())


main()
