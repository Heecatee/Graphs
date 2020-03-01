import random as r;
import utils;





def generate_random_matrix_with_edges(n,l):
    Matrix = [[0 for x in range(n)] for y in range(n)];
    l = int(l);
    n = int(n);
    while l>0:
        rand_i = r.randint(0,n-1);
        rand_j = r.randint(rand_i,n-1);
        if rand_j!=rand_i:
            if Matrix[rand_i][rand_j]==0:
                Matrix[rand_i][rand_j]=1;
                l-=1;

    for i in range(n):
        for j in range(n-i):
                Matrix[j+i][i]=Matrix[i][j+i];

    
    return Matrix;


def generate_random_matrix_with_probability(n,p):
    n = int(n);
    Matrix = [[0 for x in range(n)] for y in range(n)];
    for i in range(n):
        for j in range(n-i):
            if r.random()<=float(p):
                Matrix[i][j+i]=1;
        Matrix[i][i]=0;

    for i in range(n):
        for j in range(n-i):
                Matrix[j+i][i]=Matrix[i][j+i];
     
    return Matrix;



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
        Matrix = generate_random_matrix_with_edges(n,l);
    else:
        p = float(input("Podaj prawdopodobieństwo wystąpienia krawędzi: "));
        Matrix = generate_random_matrix_with_probability(n,p);

    utils.print_2D_array("",Matrix);
   

main();