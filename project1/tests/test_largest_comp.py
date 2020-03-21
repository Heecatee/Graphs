import sys

sys.path.append('../..')
from graph.graph import graph

def main():
    g = graph.create_from_sequence([1,2,1,2,2,2,2,2])
    component = g.largest_component()
    print(len(component))
    print(component)
    g.draw()

main()