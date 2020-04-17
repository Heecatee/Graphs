import sys

sys.path.append('../..')

from graph.graph import graph
import graph.graph_utils as graph_utils


def main():
    g = graph.create_from_file()

    random_g, random_c = graph().create_random_euler(8, 3, 1)
    random_g.draw()
    print("Euler cycle", random_c)


main()
