# KAROLINA KUCIA

"""
ALgorytm opiera się o rozwiązanie problemu maksymalnego przepływu dla jednego źródła i dwóch ujść.
Wierzchołki to miasta, źródło ma nieskończoność paliwa, dwie fabryki będą umieszczone w dwóch wierzchołkach.
Zaczyna od przekonwertowania grafu na macierz połączeń między wierzchołkami, następnie  dla
każdego wierzchołka szuka maksymalny przepływ(licząc od źródła). Gdy już mamy maksymalny przepływ
jednego wierzchołka, to na podstawie zapisanej sieci przepływów szukamy maksymalnego przepływu
dla kolejnego wierzchołka(poza źródłem i pierwszym wybranym wierzchołkiem). Zapisujemy sume maksymalnych
przepływów do pierwszego i drugiego miasta, a następnie zaczynamy szukanie dla kolejnej pary miast.
Algorytm zwraca najwiekszą z sum maksymalnych przepływów wszystkich par miast.
"""
from zad9testy import runtests
from collections import deque
from math import inf

def BFS(G, parent, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    Q = deque()
    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in range(n):
            if not visited[v] and G[u][v] != 0:
                visited[v] = True
                parent[v] = u
                if visited[t]: return True
                Q.append(v)
    return visited[t]


def find_flow(G, s, t):
    n = len(G)
    parent = [None for _ in range(n)]
    max_flow = 0
    while BFS(G, parent, s, t):
        curr_flow = inf
        curr_top = t
        while curr_top != s:
            curr_flow = min(G[parent[curr_top]][curr_top], curr_flow)
            curr_top = parent[curr_top]
        max_flow += curr_flow
        v = t
        while v != s:
            u = parent[v]
            G[v][u] += curr_flow
            G[u][v] -= curr_flow
            v = parent[v]
    return max_flow


def maxflow(G, s):
    n = len(G)
    num_of_verticles = -inf
    for i in range(n):
        num_of_verticles = max(num_of_verticles, G[i][0], G[i][1])
    num_of_verticles += 1
    result = 0

    prev_G = [[0] * num_of_verticles for _ in range(num_of_verticles)]
    for i in range(n):
        prev_G[G[i][0]][G[i][1]] = G[i][2]

    for u in range(num_of_verticles):
        if u != s:
            G = [row[:] for row in prev_G]
            curr_flow = find_flow(G, s, u)
            flow = 0
            for v in range(u + 1, num_of_verticles):
                if v != s and v != u:
                    res_G = [row[:] for row in G]
                    local_flow = find_flow(res_G, s, v)
                    flow = max(flow, local_flow)
            result = max(result, flow + curr_flow)
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
