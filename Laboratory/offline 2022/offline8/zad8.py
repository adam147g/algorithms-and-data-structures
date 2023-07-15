'''
Adam Górka
Funkcja highway w pierwszych linijkach konwertuje miasta zapisuje w liście edges
liczbę dni potrzebną na zbudowanie drogi między dwoma miastami i orez j
które są interpretowane jako krawędzie w grafie nieskierowanym.
Krawędzie te sortujemy od najmniejszej.
W kolejnej linijce szukamy ostatniego indeksu, od krórego jesteśmy w stanie znaleźć
drzewo rozpinające - last_idx.
Jako ostatni krok wykonujemy algorytm kruskala last_idx - razy, za każdym razem
usuwając najmniejszą krawędź i szukamy najmniejszą z największych różnic między dwoma
krawędziami jeśli znaleźliśmy drzewo rozpinające dla danego przykładu.
W celu optymalizacji algorytmu Kruskala - przekazuję aktualny minimalny result
i szukam MST tylko do (krawędź o najmniejszym koszcie + result)
'''

from zad8testy import runtests
from math import ceil, inf


class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find_last_idx(n, edges):
    V = [Node(i) for i in range(n)]
    ct = 1
    j = (n * (n - 1)) // 2 - 1
    while ct != n:
        x, y = V[edges[j][0]], V[edges[j][1]]
        while x != x.parent:
            x = x.parent
        while y != y.parent:
            y = y.parent

        if x != y:
            if x.rank > y.rank:
                y.parent = x
            else:
                x.parent = y
                if x.rank == y.rank:
                    y.rank += 1
            ct += 1
        j -= 1
    return j + 1


def kruskal_algorithm(n, edges, border, idx):
    V = [Node(i) for i in range(n)]
    max_ = -inf
    ct = 1
    while edges[idx][2] < border:
        x, y = V[edges[idx][0]], V[edges[idx][1]]
        while x != x.parent:
            x = x.parent
        while y != y.parent:
            y = y.parent

        if x != y:
            if x.rank > y.rank:
                y.parent = x
            else:
                x.parent = y
                if x.rank == y.rank:
                    y.rank += 1

            if edges[idx][2] > max_:
                max_ = edges[idx][2]
            ct += 1
        if ct == n:
            return max_
        idx += 1
    return None


def highway(A):
    n = len(A)
    edges = []
    for row in range(n):
        for col in range(row + 1, n):
            edges.append((row, col, ceil(((A[row][0] - A[col][0]) ** 2 + (A[row][1] - A[col][1]) ** 2) ** (1 / 2))))
    edges.sort(key=lambda x: x[2])
    last_idx = find_last_idx(n, edges)
    result = inf
    for i in range(last_idx + 1):
        max_ = kruskal_algorithm(n, edges, edges[i][2] + result, i)
        if max_ is not None and max_ - edges[i][2] < result:
            result = max_ - edges[i][2]
    return result

runtests(highway, all_tests=True)