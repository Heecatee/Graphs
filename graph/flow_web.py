from graph.directed_graph import DirectedGraph
from matplotlib import pyplot as plt
import random


class FlowWeb(DirectedGraph):
    def coords(self, width, height):
        out = []
        i = 0
        for row in self.structure:
            x = width/len(self.structure)/2 + i * width/len(self.structure) - width/2
            j = 0
            for el in row:
                try:
                    y = height/len(row)/2 + j * height/len(row) - height/2
                except:
                    y = 0
                out.append([x, y])
                j += 1
            i += 1
        return out


    def THE_CONDITION(self, i):
        for x in self.structure[i]:
            for edge in self.graph_arr:
                if edge[0] == x:
                    break
            else:
                return True
        for x in self.structure[i+1]:
            for edge in self.graph_arr:
                if edge[1] == x:
                    break
            else:
                return True
        return False
        

    def __init__(self, N):
        i = 1
        self.structure = [[0]]
        for _ in range(N):
            tab = []
            for _ in range(random.randint(2,N)):
                tab.append(i)
                i+=1
            self.structure.append(tab)
        self.structure.append([i])
        self.graph_arr = []
        for i in range(1, N):
            while self.THE_CONDITION(i):
                start = random.choice(self.structure[i])
                end = random.choice(self.structure[i+1])
                if [start, end] not in self.graph_arr:
                    self.graph_arr.append([start, end])
        for x in self.structure[1]:
            self.graph_arr.append([0, x])
        for x in self.structure[-2]:
            self.graph_arr.append([x, self.structure[-1][0]])
        for _ in range(2*N):
            start, end = -1, -1
            while start == end or [start, end] in self.graph_arr:
                start = random.randint(0,self.structure[-1][0] - 1)
                end  =  random.randint(1,self.structure[-1][0])
            self.graph_arr.append([start, end])
        self.graph_arr.sort(key = lambda x: x[0])
        
        for edge in self.graph_arr:
            edge.append(random.randint(1,10))
    
    def __str__(self):
        out = 'Warstwy:\n\n'
        for i in range(len(self.structure)):
            out += str(i) + ':  ' + str(self.structure[i]) + '\n'
        out += '\nKrawędzie [start, koniec, przepustowość]:\n'
        prev = -1
        for edge in self.graph_arr:
            out += '\n' if prev != edge[0] else '\t'
            prev = edge[0]
            out += str(edge)
        return out

    def draw(self):
        height = 12
        width = 20
        coords = self.coords(width, height)
        for id in range(len(coords)):
            plt.plot(coords[id][0], coords[id][1], 'o')
            plt.annotate(id, xy=(coords[id][0], coords[id][1]), xytext=(coords[id][0]-0.1, coords[id][1]+0.4), color='r')
        for edge in self.graph_arr:
            id = edge[0]
            id2 = edge[1]
            plt.arrow(coords[id][0], coords[id][1], coords[id2][0]-coords[id][0], coords[id2][1]-coords[id][1], head_width=0.3, length_includes_head=True, color='g')
            plt.annotate(edge[2], xy=(0,0), xytext=((coords[id][0] + coords[id2][0])/2, (coords[id][1] + coords[id2][1])/2))
        plt.axis([-width/2, width/2, -height/2, height/2])
        plt.show()


