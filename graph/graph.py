import os.path
import sys
import math
from matplotlib import pyplot as plt

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
    def __init__(self, file="graph.txt"):
        self.graph_arr = []

        if os.path.isfile(file if (len(sys.argv) <= 1) else sys.argv[0]):
            f = open(file, "r")
            for line in f:
                if (len(line.split(" ")) > 1 and has_digits(line.split(" ")[0]) and has_digits(line.split(" ")[1])):
                    self.graph_arr.append([int(line.split(" ")[0]), int(line.split(" ")[1])])
                elif (len(line.split(" ")) > 0 and has_digits(line.split(" ")[0])):
                    self.graph_arr.append([int(line.split(" ")[0]), -1])
        else:
            print("There is no file with graph data!\n")

        self.graph_arr.sort(key=lambda x: x[0])


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

    def get_vertices_number(self):
        return len(self.get_adjecency_list())

    def get_vertex_degree(self, vertex_id):
        graph_list = self.get_adjecency_list()
        return len(graph_list[vertex_id])-1

    def get_vertex_neighbours(self,vertex_id):
        graph_list = self.get_adjecency_list()
        neighboor_list = []
        i = 1
        while i<len(graph_list[vertex_id]):
            neighboor_list.append(graph_list[vertex_id][i])
            i+=1
        return neighboor_list
    
    def largest_component(self):

        graph_list = self.get_adjecency_list()
        size = self.get_vertices_number()
        visited = [0]*size
        
        i = 0
        component_number = 0

        def depth_search(vertex):
            if visited[vertex] == 0:
                visited[vertex] = component_number

                for n in self.get_vertex_neighbours(vertex):
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
