import sys

sys.path.append('..')
sys.path.append('../..')

from graph.directed_graph import DirectedGraph
from graph.flow_web import FlowWeb

# graph = DirectedGraph()
# graph.random(10, 0.5)
# print(graph.graph_arr)
# graph.draw()

graph2 = FlowWeb(3)
print(graph2.structure)