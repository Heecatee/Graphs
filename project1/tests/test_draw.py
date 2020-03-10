import sys
sys.path.append('../..')
from graph.graph import graph

graph.create_from_file().draw()
