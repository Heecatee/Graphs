#!/bin/env python3.7
import sys

sys.path.append('..')
from drawing import drawing
from generation import generation
import utils

graph_arr = utils.load_graph_from_file()
drawing.draw(generation.save_to_adjacency_matrix(graph_arr), 5)
