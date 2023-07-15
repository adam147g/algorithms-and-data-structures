'''
Adam Górka
Algorytm polega na znalezieniu za pomocą funkcji bfs najkrótszej ścieżki
z wierzchołka s do wierzchołka t. Funkcja ta zwraca jak ona przebiega do listy parent
oraz jej długość do min_dist.
W tym momencie jest sprawdzany warunek czy istnieje taka ścieżka, jeśli nie zwracamy None
w przeciwnym przypadku po kolei sprawdzamy czy dla usunięcia kolejnych krawędzi
od t do s zmieni nam się wynik najmniejszej śceżki. Jeśli tak, zwracamy usuniętą krawędź.
Gdy przejdziemy przez całą ścieżkę i nie znajdziemy wyniku, zwracamy None.
'''
from zad6testy import runtests
from queue import Queue


def default_lists(s, n):
    visited = [False] * n
    visited[s] = True
    distances = [n + 1] * n
    distances[s] = 0
    parent = [None] * n
    return visited, distances, parent


def bfs(G, start, finish, lists):
    queue = Queue()
    queue.put(start)
    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not lists[0][v]:
                lists[0][v] = True
                lists[2][v] = u
                queue.put(v)
                if lists[1][u] + 1 < lists[1][v]:
                    lists[1][v] = lists[1][u] + 1
    return lists[2], lists[1][finish]


def longer(G, s, t):
    n = len(G)
    parent, min_dist = bfs(G, s, t, default_lists(s, n))
    if min_dist == n + 1:
        return None
    i = t
    while parent[i] is not None:
        v = i, parent[i]
        G[v[0]].remove(v[1]), G[v[1]].remove(v[0])
        _, curr = bfs(G, s, t, default_lists(s, n))
        if curr > min_dist:
            return v[0], v[1]
        G[v[0]].append(v[1]), G[v[1]].append(v[0])
        i = parent[i]
    return None


runtests(longer, all_tests=True)
