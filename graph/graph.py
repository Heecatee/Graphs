import os.path
import sys
import math
from matplotlib import pyplot as plt
import random

def has_digits(s):
    return any(i.isdigit() for i in s)

def get_max_vertex(graph_arr):
    return max(max(x) for x in graph_arr) + 1

def get_amount_of_empty_vertex(graph_arr):
    return sum(x.count(-1) for x in graph_arr)

def gen_coords(amount, r):
    step = 2 * math.pi / amount
    coords = [(r * math.cos(math.pi / 2 - step * (0.5 + a)),
               r * math.sin(math.pi / 2 - step * (0.5 + a)),
               r * 1.1 * math.cos(math.pi / 2 - step * (0.5 + a)),
               r * 1.1 * math.sin(math.pi / 2 - step * (0.5 + a)))
              for a in range(amount)]
    return coords

class graph():
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
        out_graph = graph()
        if os.path.isfile(file if (len(sys.argv) <= 1) else sys.argv[0]):
            f = open(file, "r")
            for line in f:
                if (len(line.split(" ")) > 1 and has_digits(line.split(" ")[0]) and has_digits(line.split(" ")[1])):
                    out_graph.graph_arr.append([int(line.split(" ")[0]), int(line.split(" ")[1])])
                elif (len(line.split(" ")) > 0 and has_digits(line.split(" ")[0])):
                    out_graph.graph_arr.append([int(line.split(" ")[0]), -1])
        else:
            print("There is no file with graph data!\n")

        out_graph.graph_arr.sort(key=lambda x: x[0])
        return out_graph


    def get_adjecency_matrix(self):
        adjacency_matrix = [[0] * get_max_vertex(self.graph_arr) for i in range(get_max_vertex(self.graph_arr))]

        for row in self.graph_arr:
            # row[0] - first vertex, row[1] - second vertex
            if (row[0] >= 0 and row[1] >= 0):
                adjacency_matrix[row[0]][row[1]] = 1
                adjacency_matrix[row[1]][row[0]] = 1

        return adjacency_matrix


    def get_adjecency_list(self):
        max_vertex = max(max(x) for x in self.graph_arr) + 1
        tmp_list = {}
        adjacency_list = []

        # for i in range(0, len(self.graph_arr)):

        for row in self.graph_arr:
            if row[0] in tmp_list.keys():
                if row[1] >= 0:
                    tmp_list[row[0]].append(row[1])
                    if row[1] not in tmp_list.keys():
                        tmp_list[row[1]] = []
                        tmp_list[row[1]].append(row[0])
                    else:
                        tmp_list[row[1]].append(row[0])
            else:
                tmp_list[row[0]] = []
                if row[1] >= 0:
                    tmp_list[row[0]].append(row[1])
                    if row[1] not in tmp_list.keys():
                        tmp_list[row[1]] = []
                        tmp_list[row[1]].append(row[0])
                    else:
                        tmp_list[row[1]].append(row[0])

        for index, key in enumerate(tmp_list):
            adjacency_list.append([str(key) + ":"])
            for vertex in tmp_list[key]:
                adjacency_list[index].append(vertex)

        return adjacency_list


    def get_incidence_matrix(self):
        incidence_matrix = [[0] * (len(self.graph_arr) - get_amount_of_empty_vertex(self.graph_arr)) for i in
                            range(get_max_vertex(self.graph_arr))]

        for i in range(0, len(self.graph_arr) - get_amount_of_empty_vertex(self.graph_arr)):
            # row[0] - first vertex, row[1] - second vertex
            if (self.graph_arr[i][0] >= 0 and self.graph_arr[i][1] >= 0):
                incidence_matrix[self.graph_arr[i][0]][i] = 1
                incidence_matrix[self.graph_arr[i][1]][i] = 1

        return incidence_matrix


    def draw(self):
        r=5
        adj_mat = self.get_adjecency_matrix()
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