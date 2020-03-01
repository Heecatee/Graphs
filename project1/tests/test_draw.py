#!/bin/env python3
import sys
sys.path.append('..')
form drawing import drawing
from generation import generation
import utils

graph_arr = utils.load_graph_from_file()
drawing.draw(generation.save_to_adjacency_matrix(graph_arr)