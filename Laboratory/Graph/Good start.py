# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można
# osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy dany graf
# zawiera dobry początek.

from math import inf


def dfs(graph, visited, time_visit, source, time):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, visited, time_visit, v, time)
    time[0] += 1
    time_visit[source] = time[0]


def dfs_check(graph, visited, source):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs_check(graph, visited, v)


def good_start(graph):
    visited = [False] * len(graph)
    time_visit = [inf] * len(graph)
    time = [0]
    time_visit[0] = 0
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, visited, time_visit, i, time)
    for i in range(len(graph)):
        visited[i] = False
    for i in range(len(time_visit)):
        if time_visit[i] == len(time_visit):
            dfs_check(graph, visited, i)
            for j in range(len(time_visit)):
                if not visited[j]:
                    return False
            return True


graph = [[1],
         [2],
         [0, 3],
         [4],
         []]
print(good_start(graph))






'''

def SilnieSpojneSkladowe(G):
    pass


def REVERSE(G):
    n = len(F)
    g_copy = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                g_copy[j][i] = G[i][j]
    return g_copy


def DFS(G):
    def DFSv(G, V, i, T=None):
        nonlocal t
        for j in range(len(G)):
            if not V[j] and G[i][j]:
                t += 1
                DFSv(G, V, j, T)
        if T != None:
            T[i] = t

    n = len(G)
    T = [0 for _ in range(n)]
    V = [False for _ in range(n)]
    t = 0
    for i in range(n):
        if not V[i]:
            DFSv(G, V, i, T)
    return T


def SP_SKTED(G):
    def DFSv(G, V, i, T=None):
        nonlocal t
        for j in range(len(G)):
            if not V[j] and G[i][j]:
                t += 1
                DFSv(G, V, j, T)
        if T != None:
            T[i] = t
    t = 0   # ??
    n = len(G)
    T = sorted(enumerate(DFS(G)), key=lambda x: x[1], reverse=True)
    V = [False for _ in range(n)]
    reverse_graph = REVERSE(G)
    k = 0
    for i, x in T:
        if V[i]:
            DFSv(reverse_graph, V, i)
            k += 1
    return k


'''