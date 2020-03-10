import sys

sys.path.append('..')

import graph.graph_utils as graph_utils
import operations.random_gen as random_gen

def main():

    print("Wybierz tryb generowania Losowego : G(n,l) [0]       G(n,p) [1]");
    way = int(input());

    n = int(input("Podaj liczbe wierzchołków: "));
    print(n);
    if way == 0 :
        while 1>0:
            l = int(input("Podaj liczbe krawędzi: "));
            if l<= (n*n-n)/2:
                break;
        Matrix = random_gen.generate_random_matrix_with_edges(n,l);
    else:
        p = float(input("Podaj prawdopodobieństwo wystąpienia krawędzi: "));
        Matrix = random_gen.generate_random_matrix_with_probability(n,p);

    graph_utils.print_2d_array("Graf losowy",Matrix);


main();
