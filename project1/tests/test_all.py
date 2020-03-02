import sys

sys.path.append('..')
from drawing import drawing
from generation import generation
from randomGen import random_gen
from conversions import conversions
import utils


def main():
    graph = random_gen.generate_random_matrix_with_edges(5,5)
    drawing.draw(graph,5)

main()