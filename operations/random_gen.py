import random as r;

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