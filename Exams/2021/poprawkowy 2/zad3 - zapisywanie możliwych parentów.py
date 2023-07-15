# Paweł Konop

# Przechodzę przez cały graf zmodyfikowaną dijkstrą. Dodatkowo zamiast jednej tablicy parent dodaję tablicę parents która
# zapamiętuje wszystkie poprzednie wierzchołki z których można się dostać na aktualny, jeżeli waga była taka sama to
# wierzchołek zostaje dodany do listy a jeżeli mniejsz to czyszczę listę i zostawiam tylko ten wierzchołek.
# Następnie tworzę tablicę o wielkości V^2 i przechodzę po niej dodając jej wartości do wyniku. Otrzymany wynik to ilość
# wymagana ilość krawędzi. Zlozonosc obliczneiowa: ElogV, pamieciowa V^2

from zad3testy import runtests

G = [[(1, 2), (2, 4)],
     [(0, 2), (3, 11), (4, 3)],
     [(0, 4), (3, 13)],
     [(1, 11), (2, 13), (5, 17), (6, 1)],
     [(1, 3), (5, 5)],
     [(3, 17), (4, 5), (7, 7)],
     [(3, 1), (7, 3)],
     [(5, 7), (6, 3)]]

s = 0
t = 7

from queue import *

def paths(G, s, t):
    n = len(G)
    inf = float('inf')
    weights = [inf] * n
    parents = [[] for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, 0))

    while not pq.empty():

        min_w, u, parent = pq.get()

        if min_w <= weights[u]:
            weights[u] = min_w
            parents[u].append(parent)

            if u == t: continue

            for v, weight in G[u]:
                if weights[v] == inf or v == t:
                    pq.put((weights[u] + weight, v, u))

    res_arr = [[0] * n for _ in range(n)]
    q = Queue()
    print(parents)
    for parent in parents[t]:
        res_arr[t][parent] = 1
        q.put(parent)

    while q.qsize() > 0:
        u = q.get()
        if u == s: continue
        for x in parents[u]:
            res_arr[u][x] = 1
            q.put(x)

    res = 0
    for i in range(n):
        for j in range(n):
            res += res_arr[i][j]
    # print(res_arr)
    return res



runtests(paths)
