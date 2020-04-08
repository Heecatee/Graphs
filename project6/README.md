## Projekt 6

(1) Zaimplementować algorytm PageRank dla digrafu. Zastosować dwie
poniższe metody i porównać wyniki.
(a) Metoda polegającą na przechodzeniu od wierzchołka do sąsiedniego
wierzchołka za pomocą błądzenia przypadkowego z prawdopodobieństwem 1−d i teleportacji z prawdopodobieństwem d. Przyjąć d = 0.15.
PageRank wyliczyć jako częstość odwiedzin danego wierzchołka.
(b) Metoda iteracji wektora obsadzeń ~pt
. Dla t = 0 przyjąć ~p0 =
(1/n, . . . , 1/n), a następnie powtarzać iteracyjnie obliczenie ~pt+1 = ~ptP,
dla t = 1, 2, . . ., gdzie P jest macierza stochastyczną postaci Pij =
(1 − d)Aij/di + d/n, a dj
jest stopniem wyjściowym wierzchołka j, a
Aij macierzą sąsiedztwa. PageRank wylicza się jako wartości elementów
wektora obsadzeń po wielu interacjach. Jeżeli te wartości się zmieniają
w czasie, to PageRank wylicza się jako średnie tych elementów.

```bash
python test_page_rank.py
```

(2)   Zaimplementować algorytm do wyszukiwania możliwie najkrótszej zamkniętej drogi przechodzącej przez wszystkie zadane wierzchołki rozrzucone na planszy kwadratowej. Zastosować metodę symulowanego
wyżarzania opartą o łańcuch Markowa, którego pojedyncze kroki są
wykonywane jako operacje 2-opt zgodnie z algorytmem MetropolisaHastingsa

```bash
python ...
```
