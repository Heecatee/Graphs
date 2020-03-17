import sys

sys.path.append('..')
sys.path.append('../..')

from graph.directed_graph import DirectedGraph
import graph.graph_utils as graph_utils


def main():
    graph = DirectedGraph()
    graph.create_from_file_with_instance()

    graph_utils.print_2d_array("Random digraph", graph.random(5, 1))


main()
