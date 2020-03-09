#!/usr/bin/env python
import os.path
import sys
import math
from matplotlib import pyplot as plt
import graph.graph_utils as graph_utils
import random
import operations.conversions as conversions


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

    def create_from_sequence(seq):
        if sum(seq) % 2:
            print("Suma jest nieparzysta!")
            return
        seq.sort(reverse=True)
        verts = [[i, seq[i]] for i in range(len(seq))]
        out = []
        for i in range(len(seq)):
            for j in range(1, 1 + verts[0][1]):
                out.append([verts[0][0], verts[j][0]])
                verts[j][1] -= 1
            verts[0][1] = 0
            verts.sort(key=lambda x: x[1], reverse=True)
        verts.sort(key=lambda x: x[1])
        if verts[0][1] < 0:
            print("Pojawiła się wartość ujemna!")
            return
        out_graph = graph()
        out_graph.graph_arr = out
        return out_graph

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
        max_vertex = max(max(x) for x in self.graph_arr) + 1
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
            self.graph_arr[a][1] = self.graph_arr[b][0]
            self.graph_arr[b][1] = self.graph_arr[a][0]
            break

    def largest_component(self):

        graph_list = self.get_adjacency_list()
        print(graph_list)
        size = get_vertices_number(self)
        visited = [0]*size

        i = 0
        component_number = 0

        def depth_search(vertex):
            if visited[vertex] == 0:
                visited[vertex] = component_number

                for n in get_vertex_neighbours(self, vertex):
                    depth_search(n)

        while i<size:
            if visited[i] == 0:
                component_number += 1
                depth_search(i)
            i+=1

        #checking which component is the biggest:
        maxsize = 0
        maxcomponent = 0
        for c in range(1,component_number):
            size = 0
            for i in visited:
                if i == c:
                    size +=1
            if size>maxsize:
                maxsize = size
                maxcomponent = c

        #construction of a resulting graph:
        new_list = []
        for v in graph_list:
            if visited[int(v[0][:-1])]==maxcomponent:
                new_list.append(v)

        return new_list

    def euler_cycle(self):

        graph_list = self.get_adjacency_list()

        #checking if possible:
        for v in graph_list:
            if get_vertex_degree(self, int(v[0][:-1])) % 2 == 1:
                return [-1]

        edge_list = []

        done = False

        #actually walking the graph:
        vertex = 0  #this is the one we are at currently
        while done!=True:
            #getting neighboors:
            i = 1
            neighboor_list = []
            while i<len(graph_list[i]):
                neighboor_list.append(graph_list[vertex][i])
                i+=1

            if len(neighboor_list) == 0:
                #we have came to an end...
                done = True
                continue

            neighboor_list.sort()

            #walk, append path and remove edge:
            vertex_to_go = neighboor_list[0]

            edge_list.append(vertex)

            graph_list[vertex].remove(vertex_to_go)
            graph_list[vertex_to_go].remove(vertex)
            vertex = vertex_to_go

        return edge_list
