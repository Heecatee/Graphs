#!/bin/env python3.7
import math
from matplotlib import pyplot as plt


################################################################################
####    Draw arguments:  adjecency matrix, radius of the drawing circle     ####
################################################################################

def gen_coords(amount, r):
    step = 2 * math.pi / amount
    coords = [(r * math.cos(math.pi / 2 - step * (0.5 + a)),
               r * math.sin(math.pi / 2 - step * (0.5 + a)),
               r * 1.1 * math.cos(math.pi / 2 - step * (0.5 + a)),
               r * 1.1 * math.sin(math.pi / 2 - step * (0.5 + a)))
              for a in range(amount)]
    return coords


def draw(adj_mat, r):
    coords = gen_coords(len(adj_mat), r)
    for id in range(len(adj_mat)):
        for id2 in range(id + 1, len(adj_mat)):
            if adj_mat[id][id2]:
                plt.plot([coords[id][0], coords[id2][0]], [coords[id][1], coords[id2][1]])
        plt.plot(coords[id][0], coords[id][1], 'o')
        plt.annotate(id, xy=(coords[id][0], coords[id][1]), xytext=(coords[id][2], coords[id][3]))
    plt.axis([-r - 1, r + 1, -r - 1, r + 1])
    plt.show()
