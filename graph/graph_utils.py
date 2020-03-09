def has_digits(graph):
    for row in graph:
        if not any(i.isdigit() for i in row):
            return False
    return True


def get_max_vertex(graph_arr):
    return max(max(x) for x in graph_arr) + 1


def get_amount_of_empty_vertex(graph_arr):
    return sum(x.count(-1) for x in graph_arr)


def get_vertices_number(graph):
    return len(graph.get_adjacency_list())


def get_vertex_degree(graph, vertex_id):
    graph_list = graph.get_adjacency_list()
    return len(graph_list[vertex_id]) - 1


def get_vertex_neighbours(graph, vertex_id):
    graph_list = graph.get_adjacency_list()
    neighbor_list = []
    i = 1
    while i < len(graph_list[vertex_id]):
        neighbor_list.append(graph_list[vertex_id][i])
        i += 1
    return neighbor_list


def print_2d_array(title, arr):
    print(title + ":")
    for row in arr:
        for col in row:
            print(col, end=" ")
        print("")
    print("")
