'''
Adam Górka
Algorytm polega na sprawdzaniu każdej możliwej ścieżki wchodząc jedną bramą do miasta,
a wychodząc z niego drugą.
Jeśli danej ścieżki nie ma, to się cofamy i próbujemy dalej, do skutku.
W celu optymalizacji w pierwszym kroku znajdujemy miasto z najmniejszą liczbą miast
do których można dotrzeć z jednej z bram i z niej rozpoczynamy wyszukiwanie ścieżki.
'''
from zad7testy import runtests
from math import inf


def dfs(G, visited, res, v, finish, left, stp):
    visited[v] = True
    if left == 1:
        if finish in G[v][stp]:
            res.append(v)
            return True
        visited[v] = False
        return False

    for u in G[v][stp]:
        if not visited[u]:
            res.append(v)
            if v in G[u][0]:
                if dfs(G, visited, res, u, finish, left - 1, 1):
                    return True
            if v in G[u][1]:
                if dfs(G, visited, res, u, finish, left - 1, 0):
                    return True

            res.remove(v)
    visited[v] = False
    return False


def droga(G):
    n = len(G)
    visited = [False] * n
    res = []
    vertex = None
    ct = inf
    for i in range(n):
        tmp = len(G[i][0])
        if tmp < ct:
            ct = tmp
            vertex = i, 0
        tmp = len(G[i][1])
        if tmp < ct:
            ct = tmp
            vertex = i, 1
        if ct == 1:   break
    if dfs(G, visited, res, vertex[0], vertex[0], n, vertex[1]):
        return res
    return None


runtests(droga, all_tests=True)
