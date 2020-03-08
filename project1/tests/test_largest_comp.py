import sys

sys.path.append('../..')
from graph.graph import graph
import utils

def main():
    g = graph()
    component = g.largest_component()
    utils.print_2D_array("largest component:",component)

main()