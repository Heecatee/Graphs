#!/bin/env python3.7

import sys
sys.path.append('../..')
from graph.graph import graph

graph1 = graph.create_from_sequence([4,2,2,3,2,1,4,2,2,2,2])
print(graph1.graph_arr)
graph1.draw()

for i in range(10):
    graph1.randomize()

graph1.draw()

graph2 = graph.create_from_sequence([1,1,0])

graph2.draw()
graph2.randomize()

graph3 = graph.create_from_sequence([1,1,1,1])
graph3.draw()
graph3.randomize()
graph3.draw()