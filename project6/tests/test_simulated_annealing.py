import sys

sys.path.append('..')
sys.path.append('../..')

import math
import random
from graph.directed_graph import DirectedGraph
from matplotlib import pyplot as plt

MAX_ITER = 100


def cycle_length(arr):
    cycle_len = 0
    for i in range(len(arr)):
        cycle_len += math.sqrt(math.pow(arr[i][1][0] - arr[i][0][0], 2) + math.pow(arr[i][1][1] - arr[i][0][1], 2))
    return cycle_len


def draw_paths(arr, ax):
    for i in range(len(arr)):
        ax.plot([arr[i][0][0], arr[i][1][0]], [arr[i][0][1], arr[i][1][1]], 'go-')
    ax.set_xlabel('Cycle length = ' + str(cycle_length(arr)))


def get_random_edges(arr):
    different_edges = False

    while not different_edges:
        edge1 = random.choice(arr)
        edge2 = random.choice(arr)
        if edge1 != edge2 and edge1[0] != edge2[0] and edge1[0] != edge2[1] and edge2[1] != edge1[1]:
            different_edges = True
            return arr.index(edge1), arr.index(edge2)


def simulated_annealing(cycle):
    # wyznacz dowolny cykl
    for i in range(100, 0, -1):
        T = 0.001 * math.pow(i, 2)

        for it in range(1, 10000):
            new_cycle = cycle.copy()
            e1, e2 = get_random_edges(cycle)
            new_cycle[e1][1], new_cycle[e2][0] = new_cycle[e2][0], new_cycle[e1][1]
            if cycle_length(new_cycle) < cycle_length(cycle):
                cycle = new_cycle
            else:
                r = random.uniform(0, 1)
                if r < math.exp(-1 * (cycle_length(new_cycle) - cycle_length(cycle))/T):
                    cycle = new_cycle
                pass

    return cycle


def generate_cycle(arr):
    cycle = []
    for i in range(len(arr)):
        if i != len(arr) - 1:
            cycle.append([[arr[i][0], arr[i][1]], [arr[i + 1][0], arr[i + 1][1]]])
    cycle.append([[arr[0][0], arr[0][1]], [arr[len(arr) - 1][0], arr[len(arr) - 1][1]]])
    return cycle


def main():
    graph = DirectedGraph()
    graph.create_from_file_with_instance("simulated_annealing_input.txt", False)

    plt.rcParams["figure.figsize"] = (5, 10)
    cycle = generate_cycle(graph.graph_arr)
    fig, axs = plt.subplots(2, 1)

    axs[0].set_title("Initial data")
    draw_paths(cycle, axs[0])

    cycle = simulated_annealing(cycle)

    axs[1].set_title("End data")
    draw_paths(cycle, axs[1])

    plt.show()


main()
