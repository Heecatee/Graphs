import sys

sys.path.append('../..')

from graph.graph import graph
import graph.graph_utils as graph_utils


def main():
    print("main")
    g = graph.create_from_file()
    euler_cycle = g.euler_cycle()
    print("Euler cycle", euler_cycle)

    random_g, random_c = graph.create_random_euler(8)
    random_g.draw()
    print(random_c)


main()
