#!/bin/env python3.7

import sys
sys.path.append('../..')
from graph.graph import graph

graph1 = graph.create_from_sequence([4,2,2,3,2,1,4,2,2,2,2])
graph1.draw()

for i in range(10):
    graph1.randomize()

graph1.draw()