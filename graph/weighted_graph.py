from graph.graph import graph


class WeightedGraph(graph):
    def __init__(self):
        super().__init__()
        self.graph_arr = []

    def generate_random_weights(self):
        graph_list = self.get_adjacency_list()
