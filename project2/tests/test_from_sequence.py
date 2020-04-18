#!/bin/env python3.7

import sys
sys.path.append('../..')
from graph.graph import graph
import graph.graph_utils as graph_utils

graph1 = graph.create_from_sequence([4,2,2,3,2,1,4,2,2,2,2])
graph_utils.print_2d_array("Ciag graficzny", graph1.get_adjacency_matrix())
graph1.draw()

print("Ciag niegraficzny:")
graph_wrong = graph.create_from_sequence([4,2,2,3,2,1,4,2,2,2,1])

print("Ciag niegraficzny:")
graph_wrong2 = graph.create_from_sequence([4,-2,1,4,2,2,2,1])