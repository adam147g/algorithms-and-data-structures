# Adam Górka
# Algorytm znajduje najkrótszą ścieżkę od s do t, po czym zapisuje ją w T[0],
# a jej długość w dist[0]
#
# Następnie z ścieżki, którą otrzymaliśmy usuwamy jedną krawędź i szukamy
# najkrótszej ścieżki dla takiego przypadku.
# Tak robimy do momentu, kiedy usuniemy po każdej krawędzi z pierwotnie znalezionej ścieżki
# i obliczymy dane wyniki.
# Jeśli po usunięciu dystans będzie większy od dist[0], to nie bierzemy tej ścieżki pod uwagę
# w result zapisujemy krawędzie, które dotychczas się pojawiły. Jeśli analizowana krawędź
# nie występuje w result, to dopisujemy ją

# Złożoność obliczeniowa wynosi O(V*E*log(V))
# Złożoność pamięciowa to O(V+E)

from zad3testy import runtests
from queue import PriorityQueue
from math import inf


def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def minimum_product(graph, u, v, x):
    queue = PriorityQueue()
    queue.put((0, u))
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    visited = [False] * len(graph)
    distance[u] = 0
    while not queue.empty():
        dist, vertex = queue.get()
        for adj in graph[vertex]:
            if not visited[adj[0]] and relax(vertex, adj, distance, parent):
                queue.put((distance[adj[0]], adj[0]))
        visited[vertex] = True
    path = []
    while v != parent[u]:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path, distance[x]


def paths(G, s, t):
    graph_copy = G
    T = [[] for _ in range(len(G))]
    dist = [inf] * len(G)
    T[0], dist[0] = minimum_product(graph_copy, s, t, t)
    n = len(T[0]) - 1
    x = 1

    while n > 0:
        idx = T[0][n]
        idx_prev = T[0][n - 1]
        e = 0
        for i in range(len(G[idx])):
            if G[idx][i][0] == idx_prev:
                e = G[idx][i][1]
                graph_copy[idx][i] = (idx_prev, inf)
        for i in range(len(G[idx_prev])):
            if G[idx_prev][i][0] == idx:
                graph_copy[idx_prev][i] = (idx, inf)
        T[x], dist[x] = minimum_product(graph_copy, s, t, t)
        x += 1

        for i in range(len(G[idx])):
            if G[idx][i][0] == idx_prev:
                graph_copy[idx][i] = (idx_prev, e)
        for i in range(len(G[idx_prev])):
            if G[idx_prev][i][0] == idx:
                graph_copy[idx_prev][i] = (idx, e)
        n -= 1

    check = dist[0]
    licz = len(dist)
    for i in range(len(dist)):
        if dist[i] > check:
            T[i] = []
            licz -= 1

    result = []
    for i in range(len(T[0]) - 1):
        result.append((T[0][i], T[0][i + 1]))
    for i in range(1, licz):
        for j in range(len(T[i]) - 1):
            if (T[i][j], T[i][j + 1]) not in result:
                if (T[i][j + 1], T[i][j]) not in result:
                    result.append((T[i][j], T[i][j + 1]))

    return len(result)


runtests(paths)
