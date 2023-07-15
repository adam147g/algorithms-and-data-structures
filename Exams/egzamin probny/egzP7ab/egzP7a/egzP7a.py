from egzP7atesty import runtests
from math import inf

'''
from collections import deque
from queue import Queue
from math import inf


def bfs(graph, s, t, parent):
    # queue = Queue()
    Q = deque()
    visited = [False] * len(graph)
    visited[s] = True
    # queue.put(s)
    Q.append(s)

    # while not queue.empty():
    while Q:
        u = Q.popleft()
        # u = queue.get()

        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                if visited[t]: return True
                # queue.put(v)
                Q.append(v)
    return visited[t]


def edmonds_karp_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
        current_flow = inf
        v = t
        while v != s:
            current_flow = min(current_flow, graph[parent[v]][v])
            v = parent[v]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


'''


def dfs_visit(G, V, P, i, t):
    V[i] = True
    if i == t:
        return True
    for nb in range(len(G)):
        if not V[nb] and G[i][nb]:
            P[nb] = i
            dfs_visit(G, V, P, nb, t)


def dfs(G, s, t, P):
    V = [False for _ in range(len(G))]
    dfs_visit(G, V, P, s, t)
    return V[t]


def ford_fulkerson_algorithm(graph, s, t):
    P = [None] * len(graph)
    max_flow = 0
    while dfs(graph, s, t, P):
        current_flow = inf
        v = t
        while v != s:
            current_flow = min(current_flow, graph[P[v]][v])
            v = P[v]
        max_flow += current_flow
        v = t
        while v != s:
            u = P[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = P[v]
    return max_flow


def akademik(T):
    n = len(T)
    G = [[0 for _ in range(2 * n + 2)] for _ in range(2 * n + 2)]
    ct = 0
    for i in range(n):
        G[0][i + 1] = 1
        G[n + 1 + i][2 * n + 1] = 1
        cur = 0
        for j in T[i]:
            if j is not None:
                G[1 + i][n + 1 + j] = 1
            else:
                cur += 1
        if cur == 3:
            ct += 1

    return n - ford_fulkerson_algorithm(G, 0, (2 * n) + 1) - ct


#   return n - edmonds_karp_algorithm(G, 0, (2 * n) + 1) - ct


runtests(akademik)
