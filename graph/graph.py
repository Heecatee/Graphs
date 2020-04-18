#!/usr/bin/env python
import os.path
import sys
import math
from matplotlib import pyplot as plt
import graph.graph_utils as graph_utils
import random
import numpy as np
import operations.conversions as conversions


def get_max_vertex(graph_arr):
    max_vertex = -1
    for row in graph_arr:
        for i in range(0, len(row)):
            if row[i] > max_vertex and i < 2:
                max_vertex = row[i]

    return max_vertex + 1


def get_amount_of_empty_vertex(graph_arr):
    return sum(x.count(-1) for x in graph_arr)


def get_vertex_degree(graph, vertex_id):
    graph_list = graph.get_adjacency_list()
    return len(graph_list[vertex_id]) - 1


def get_vertex_neighbours(graph, vertex_id):
    graph_list = graph_utils.list_to_int_array(graph.get_adjacency_list())
    neighbor_list = []
    i = 1
    while i < len(graph_list[vertex_id]):
        neighbor_list.append(graph_list[vertex_id][i])
        i += 1
    return neighbor_list


def gen_coords(amount, r):
    step = 2 * math.pi / amount
    coords = [(r * math.cos(math.pi / 2 - step * (0.5 + a)),
               r * math.sin(math.pi / 2 - step * (0.5 + a)),
               r * 1.1 * math.cos(math.pi / 2 - step * (0.5 + a)),
               r * 1.1 * math.sin(math.pi / 2 - step * (0.5 + a)))
              for a in range(amount)]
    return coords


class graph:
    def __init__(self):
        self.graph_arr = []

    def __len__(self):
        return len(self.get_adjacency_list())

    def add_edge(self, u, v, w):
        if w is None:
            self.graph_arr.append([u, v])
        else:
            self.graph_arr.append([u, v, w])

    def create_from_sequence(seq):
        if sum(seq) % 2:
            print("Suma jest nieparzysta!")
            return False
        seq.sort()
        out = []
        index = len(seq) - 1
        for i in range(len(seq)):
            if seq[i] == 0:
                out.append([index, -1])
                index -= 1
                seq.pop(i)
            else:
                break
        seq.sort(reverse=True)
        verts = [[i, seq[i]] for i in range(len(seq))]
        for i in range(len(seq)):
            for j in range(1, 1 + verts[0][1]):
                out.append([verts[0][0], verts[j][0]])
                verts[j][1] -= 1
            verts[0][1] = 0
            verts.sort(key=lambda x: x[1], reverse=True)
        verts.sort(key=lambda x: x[1])
        if verts[0][1] < 0:
            print("Pojawiła się wartość ujemna!")
            return False
        out.sort()
        out_graph = graph()
        out_graph.graph_arr = out
        return out_graph

    # zrobilismy to totalnie nie po pythonowemu, przez co mamy problem, nie chce mi sie juz
    # tego naprawiac wiec zrobilam wrapper na metode create
    def create_from_file_with_instance(self, file="graph.txt"):
        self.graph_arr = graph.create_from_file(file).graph_arr
        return self

    def create_from_file(file="graph.txt"):
        # 0 - first vertex, 1 - second vertex, 2 - weight
        out_graph = graph()
        if os.path.isfile(file if (len(sys.argv) <= 1) else sys.argv[0]):
            f = open(file, "r")
            for line in f:
                if len(line.split(" ")) > 2 and graph_utils.has_digits(line.split(" ")):
                    out_graph.graph_arr.append([int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2])])
                elif len(line.split(" ")) > 1 and graph_utils.has_digits(line.split(" ")):
                    out_graph.graph_arr.append([int(line.split(" ")[0]), int(line.split(" ")[1])])
                elif len(line.split(" ")) > 0 and graph_utils.has_digits(line.split(" ")):
                    out_graph.graph_arr.append([int(line.split(" ")[0]), -1])
        else:
            print("There is no file with graph data!\n")

        out_graph.graph_arr.sort(key=lambda x: x[0])
        return out_graph

    def get_adjacency_matrix(self):
        adjacency_matrix = [[0] * get_max_vertex(self.graph_arr) for i in
                            range(get_max_vertex(self.graph_arr))]

        for row in self.graph_arr:
            weight = 1
            if len(row) > 2:
                weight = row[2]

            if row[0] >= 0 and row[1] >= 0:
                adjacency_matrix[row[0]][row[1]] = weight
                adjacency_matrix[row[1]][row[0]] = weight

        return adjacency_matrix

    def get_adjacency_list(self):
        max_vertex = get_max_vertex(self.graph_arr)
        tmp_list = {}
        adjacency_list = []

        # for i in range(0, len(self.graph_arr)):

        for row in self.graph_arr:
            weight = ''
            if len(row) > 2:
                weight = '(' + str(row[2]) + ')'

            if row[0] in tmp_list.keys():
                if row[1] >= 0:
                    tmp_list[row[0]].append(str(row[1]) + weight)
                    if row[1] not in tmp_list.keys():
                        tmp_list[row[1]] = []
                        tmp_list[row[1]].append(str(row[0]) + weight)
                    else:
                        tmp_list[row[1]].append(str(row[0]) + weight)
            else:
                tmp_list[row[0]] = []
                if row[1] >= 0:
                    tmp_list[row[0]].append(str(row[1]) + weight)
                    if row[1] not in tmp_list.keys():
                        tmp_list[row[1]] = []
                        tmp_list[row[1]].append(str(row[0]) + weight)
                    else:
                        tmp_list[row[1]].append(str(row[0]) + weight)

        for index, key in enumerate(tmp_list):
            adjacency_list.append([str(key) + ":"])
            for vertex in tmp_list[key]:
                adjacency_list[index].append(vertex)

        return adjacency_list

    def get_incidence_matrix(self):
        incidence_matrix = [[0] * (len(self.graph_arr) - get_amount_of_empty_vertex(self.graph_arr)) for i
                            in
                            range(get_max_vertex(self.graph_arr))]

        for i in range(0, len(self.graph_arr) - get_amount_of_empty_vertex(self.graph_arr)):
            # row[0] - first vertex, row[1] - second vertex
            if self.graph_arr[i][0] >= 0 and self.graph_arr[i][1] >= 0:
                incidence_matrix[self.graph_arr[i][0]][i] = 1
                incidence_matrix[self.graph_arr[i][1]][i] = 1

        return incidence_matrix

    def draw(self):
        r = 5
        adj_mat = self.get_adjacency_matrix()
        coords = gen_coords(len(adj_mat), r)
        for id in range(len(adj_mat)):
            for id2 in range(id + 1, len(adj_mat)):
                if adj_mat[id][id2]:
                    plt.plot([coords[id][0], coords[id2][0]], [coords[id][1], coords[id2][1]])
            plt.plot(coords[id][0], coords[id][1], 'o')
            plt.annotate(id, xy=(coords[id][0], coords[id][1]), xytext=(coords[id][2], coords[id][3]))
        plt.axis([-r - 1, r + 1, -r - 1, r + 1])
        plt.show()

    def randomize(self):
        if len(self) < 4:
            print("Too few lines")
            return False
        while True:
            a = random.randrange(len(self.graph_arr))
            b = random.randrange(len(self.graph_arr))
            if self.graph_arr[a][0] == self.graph_arr[b][0]:
                continue
            if self.graph_arr[a][0] == self.graph_arr[b][1]:
                continue
            if self.graph_arr[a][1] == self.graph_arr[b][0]:
                continue
            if self.graph_arr[a][1] == self.graph_arr[b][1]:
                continue
            if [self.graph_arr[a][0], self.graph_arr[b][1]] in self.graph_arr:
                continue
            if [self.graph_arr[b][0], self.graph_arr[a][1]] in self.graph_arr:
                continue
            tmp = self.graph_arr[a][1]
            self.graph_arr[a][1] = self.graph_arr[b][1]
            self.graph_arr[b][1] = tmp
            break

    def largest_component(self):

        graph_list = self.get_adjacency_list()
        size = len(self)
        visited = [0] * size

        i = 0
        component_number = 0

        def depth_search(vertex):
            if visited[vertex] == 0:
                visited[vertex] = component_number

                for n in get_vertex_neighbours(self, vertex):
                    depth_search(n)

        while i < size:
            if visited[i] == 0:
                component_number += 1
                depth_search(i)
            i += 1

        # checking which component is the biggest:
        maxsize = 0
        maxcomponent = 0
        for c in range(1, component_number+1):
            size = 0
            for i in visited:
                if i == c:
                    size += 1
            if size > maxsize:
                maxsize = size
                maxcomponent = c

        # construction of a resulting graph:
        new_list = []
        for v in graph_list:
            if visited[int(v[0][:-1])] == maxcomponent:
                new_list.append(v[0][:-1])

        return new_list

    def euler_cycle(self):

        graph_list = self.get_adjacency_list()

        # checking if possible:
        for v in graph_list:
            if get_vertex_degree(self, int(v[0][:-1])) % 2 == 1:
                return [-1]

        edge_list = []

        done = False

        # actually walking the graph:
        vertex = 0  # this is the one we are at currently
        while done != True:
            # getting neighboors:
            i = 1
            neighboor_list = []
            while i < len(graph_list[vertex]):
                neighboor_list.append(graph_list[vertex][i])
                i += 1

            if len(neighboor_list) == 0:
                # we have came to an end...
                done = True
                continue

            neighboor_list.sort()

            # walk, append path and remove edge:
            vertex_to_go = neighboor_list[0]

            edge_list.append(vertex)

            graph_list[vertex].remove(vertex_to_go)
            graph_list[int(vertex_to_go)].remove(str(vertex))
            vertex = int(vertex_to_go)
        
        #check if egde_list contains all the vertices:
        actual_edge_list = [False]*len(graph_list)
        for e in edge_list:
            actual_edge_list[e] = True
        
        for e in actual_edge_list:
            if not e:
                return [-1]

        return edge_list

    def create_random_euler(self, vertices_number, max_edges=3, min_edges=1):
        seq = []
        generated_graph = None
        while generated_graph is None or \
                generated_graph is False or \
                not generated_graph.is_connected():
            seq = []
            for i in range(0, vertices_number):
                seq.append(2 * random.randint(min_edges, max_edges))
                # print(seq[i])

            generated_graph = graph.create_from_sequence(seq)

            # if not generated_graph:
            #     return self.create_random_euler(vertices_number, max_edges, min_edges)

        return generated_graph, generated_graph.euler_cycle()

    def posible_move_hamilton(graph1, k, x, tab):
        if graph1[tab[x - 1]][k] == 0:
            return False
        for i in tab:
            if i == k:
                return False
        return True

    def next_vertex(graph1, x, n, tab):
        if x == n:
            if graph1[tab[x - 1]][tab[0]] == 1:
                return True
            else:
                return False
        for k in range(1, n):
            if graph.posible_move_hamilton(graph1, k, x, tab):
                tab[x] = k
                if graph.next_vertex(graph1, x + 1, n, tab):
                    return True
                tab[x] = -1
        return False

    def hamilton_cycle(graph1, x, n, tab):

        if not graph.next_vertex(graph1, 1, n, tab):
            print("Brak rozwiązania! \n")
            return False
        print(tab)
        return True
    
    def get_centers(self):
        Matrix = self.get_distances_matrix()
        n = graph_utils.get_vertices_number(self)
        center = 0
        center_minmax = 0
        sum = 0
        max = 0
        for i in range(n):
            sum += Matrix[0][i]
            if max < Matrix[0][i]:
                center_minmax = 0
                max = Matrix[0][i]

        for i in range(1, n):
            sum_tmp = 0
            max_tmp = 0
            for j in range(n):
                sum_tmp += Matrix[i][j]
                if max_tmp < Matrix[i][j]:
                    max_tmp = Matrix[i][j]
            if sum_tmp < sum:
                sum = sum_tmp
                center = i
            if max_tmp < max:
                center_minmax = i
                max = max_tmp

        print("Centrum grafu:", center, "(suma odległości: ", sum, ")")
        print("Centrum minmax grafu:", center_minmax, "(odleglosc od najdalszego: ", max, ")")
        return center, center_minmax

    def prim_algorithm(self):
        matrix = self.get_adjacency_matrix()
        n = graph_utils.get_vertices_number(self)
        tab_T = [-1 for x in range(n)]
        tab_W = [0 for x in range(n)]
        for i in range(n):
            tab_W[i] = i
        tab_T[0] = 0
        tab_W[0] = -1
        tmp_x = 0
        tmp_y = 0
        graph_arr_prim_tree = []
        for i in range(n - 1):
            min = sys.maxsize
            for x in range(n):
                if tab_T[x] != -1:
                    for y in range(n):
                        if tab_W[y] != -1:
                            if min > matrix[tab_T[x]][tab_W[y]] != 0:
                                min = matrix[tab_T[x]][tab_W[y]]
                                tmp_x = tab_T[x]
                                tmp_y = tab_W[y]
            tab_W[tmp_y] = -1
            tab_T[tmp_y] = tmp_y
            graph_arr_prim_tree.append([tmp_x, tmp_y, min])
        self.graph_arr = graph_arr_prim_tree
        return self

    def is_connected(self):
        matrix_len = graph_utils.get_vertices_number(self)
        adj_matrix = graph.get_adjacency_matrix(self)
        visited = [False] * graph_utils.get_vertices_number(self)

        for i in range(0, matrix_len):
            all_zeros = True

            for j in range(0, matrix_len):
                if 0 != adj_matrix[i][j]:
                    all_zeros = False

            if all_zeros:
                return False
            self.traverse(i, visited, adj_matrix, matrix_len)

            for j in range(0, matrix_len):
                if not visited[j]:
                    return False

        return True

    def traverse(self, i, visited, adj_matrix, matrix_len):
        visited[i] = True

        for j in range(0, matrix_len):
            if adj_matrix[i][j] != 0:
                if not visited[j]:
                    self.traverse(j, visited, adj_matrix, matrix_len)
