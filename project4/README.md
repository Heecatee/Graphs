## Projekt 4

(1) Napisać program do kodowania grafów skierowanych (digrafów) i do
generowania losowych digrafów z zespołu G(n, p).

```bash
python test_digraph_encoding.py
python test_random_digraph.py
```
Macierz incydencji:

![alt text](https://static.javatpoint.com/tutorial/graph-theory/images/graph-representations4.png)

Macierz sąsiedztwa:

![alt text](https://ycpcs.github.io/cs360-spring2019/lectures/images/lecture15/adjmatexample.png)


(2) Zaimplementować algorytm Kosaraju do szukania silnie spójnych składowych na digrafie i zastosować go do digrafu losowego.

```bash
python test_kosaraju.py
```

(3) Wykorzystując algorytmy z powyższych punktów wygenerować losowy
silnie spójny digraf. Łukom tego digrafu przypisać losowe wagi będące
liczbami całkowitymi z zakresu [−5, 10]. Zaimplementować algorytm
Bellmana-Forda do znajdowania najkrótszych ścieżek od danego wierzchołka.

```bash
python test_bellmann_ford.py
```

(4) Zaimplementować algorytm Johnsona do szukania odegłości pomiędzy
wszystkimi parami wierzchołków na ważonym grafie skierowanym.


```bash
python test_johnson.py
```
