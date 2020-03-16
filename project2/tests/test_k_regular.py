import sys

sys.path.append('../..')
from graph.graph import graph
from graph.graph import graph_utils


def main():
    n = int(input("Podaj liczbe wierzchołków: "))
    print(n);
    while 1 > 0:
        l = int(input("Podaj liczbe k: "))
        if l <= n - 1:
            break;

    list = [l for x in range(n)]

    graph1 = graph.create_from_sequence(list)

    graph1.draw();


main();
