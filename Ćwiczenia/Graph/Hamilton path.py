# Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie
# raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm,
# który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym.

# 1

def DFS(G):
    n = len(G)
    path = []
    visited = [False] * n
    stack = []
    # for u, neigh in enumerate(G):   # u to indeks, neigh to G[u]
    for u in range(n):
        if not visited[u]:
            stack.append(u)
            while len(stack) > 0:
                v = stack.pop()
                visited[v] = True
                for w in G[v]:
                    if not visited[w]:
                        stack.append(w)
                path.append(v)
    path.reverse()
    return path

def CHECK(G, path):
    for i in range(1, len(path)):
        if path[i] not in G[path[i-1]]:
            return False
    return True


# 2


def dfs(graph, source, visited, result):
    visited[source] = True
    for v in range(len(graph)):
        if not visited[v] and graph[source][v] == 1:
            dfs(graph, v, visited, result)
    result.insert(0, source)


def topological_sort(graph):
    visited = [False] * len(graph)
    result = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, result)
    return result


def hamiltonian_path(graph):
    result = topological_sort(graph)
    result.append(result[0])
    for i in range(1, len(result)):
        if graph[result[i - 1]][result[i]] == 0:
            return False
    return True


graph = [[0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0],
         [1, 0, 0, 1, 0, 0, 0]]
print(hamiltonian_path(graph))
