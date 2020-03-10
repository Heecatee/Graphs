from graph.graph import graph
import operations.random_gen as random_gen


class WeightedGraph(graph):
    def __init__(self):
        super().__init__()
        self.graph_arr = []

    def dijkstra_algorithm(self):
        print("")

