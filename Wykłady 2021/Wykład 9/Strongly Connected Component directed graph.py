# Niech G = (V, E) będzie grafem skierowanym. Mówimy, że u,v należą do tej samej
# Silnie Spójnej Składowej, jeśli istnieją ścieżki skierowane z u do v oraz z v do u


' DFS_Util zapisuje czasy przetworzenia!!! '

def DFS_Util(graph, source, visited, times):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DFS_Util(graph, v, visited, times)
    times.append(source)



def reverse_graph(graph):
    new_graph = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            new_graph[graph[i][j]].append(i)
    return new_graph



def dfs(graph, u, visited, result, index):
    visited[u] = True
    result[index].append(u)
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited, result, index)


def SCC(graph):
    visited = [False] * len(graph)
    times = []
    for i in range(len(graph)):
        if not visited[i]:
            DFS_Util(graph, i, visited, times)  # zapisujemy w times czas przetworzenia wierzchołków
    print(times)

    print(graph)
    graph = reverse_graph(graph)                # graf ze zmienionymi stronami
    print(graph)

    for i in range(len(visited)):
        visited[i] = False
    result = [[] for _ in range(len(graph))]
    index = 0
    while len(times):
        u = times.pop()
        if not visited[u]:
            dfs(graph, u, visited, result, index)
            index += 1

    return result

#           0       1       2     3    4      5     6    7    8     9     10
graph = [[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [8], [9], [10], [6, 7]]
print(SCC(graph))