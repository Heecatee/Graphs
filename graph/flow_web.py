

from graph.directed_graph import DirectedGraph
import random

def THE_CONDITION(array, next_length):
    check = list(range(next_length))
    for conn in array:
        if not conn:
            return True
        for node in conn:
            if check.index(node):
                 check.pop(check.index(node))
    if not check:
        return False
    else:
        return True


class FlowWeb(DirectedGraph):
    def __init__(self, N):
        i = 0
        self.structure = [[]]
        for _ in range(N):
            self.structure.append([[] for i in range(random.randint(2,N))])
        self.structure.append([])
        print(self.structure)
        for i in range(len(self.structure)):
            if i == N+1:
                break
            while THE_CONDITION(self.structure[i], len(self.structure[i+1])):
                start = random.randint(0,len(self.structure[i]))
                end = random.randint(0,len(self.structure[i+1]))
                if end not in self.structure[start]:
                    self.structure[start].append(end)
    
    def draw(self):
        pass


