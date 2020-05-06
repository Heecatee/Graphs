import sys

sys.path.append('..')
sys.path.append('../..')

from graph.directed_graph import DirectedGraph
from graph.flow_web import FlowWeb

graph2 = FlowWeb(3)
print(graph2)
graph2.draw()