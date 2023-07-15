# The Ford-Fulkerson algorithm is a greedy algorithm that computes the maximum flow in a flow network (graph).
from math import inf


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
    parent = [None] * len(graph)
    max_flow = 0
    while dfs(graph, s, t, parent):
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


graph = [[0, 11, 12, 17, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 7, 0, 10, 0],
         [0, 0, 0, 0, 0, 0, 6, 9, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(ford_fulkerson_algorithm(graph, 0, 9))
