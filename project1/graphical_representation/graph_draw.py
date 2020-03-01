#!/bin/env python3
import sys
import math
sys.path.append('..')
from matplotlib import pyplot as plt

r=6

matrox = [[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0]]

def gen_coords(amount):
    step = 2*math.pi/amount
    coords = [(r*math.cos(math.pi/2 - step*(0.5 + a)), r*math.sin(math.pi/2 - step*(0.5 + a))) for a in range(amount)]
    return coords

def draw(adj_mat):
    verts = gen_coords(6)
    for vert in verts:
        plt.plot(vert[0], vert[1], 'bo')
        plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.axis([-r-1, r+1, -r-1, r+1])
    plt.Circle((0,0), r)
    plt.show()

draw(matrox)