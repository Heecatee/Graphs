import sys

sys.path.append('../..')

from graph.graph import graph
import graph.graph_utils as graph_utils


def main():
    g = graph.create_from_file()
    g.draw()
    component = g.largest_component()
    graph_utils.print_2d_array("largest component", component)


main()
