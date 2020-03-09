import sys

sys.path.append('..')
sys.path.append('../..')

from graph.graph import graph
import graph.graph_utils as graph_utils


def main():
    g = graph()
    component = g.largest_component()
    graph_utils.print_2d_array("largest component:", component)


main()
