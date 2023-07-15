# DAG - directed acyclic graph
# Topological sorting of DAG consists in arranging the vertices in order that the edges point
# only from left to right.


# Sortowanie topologiczne dag'u polega na ułożeniu wierzchołków w takiej kolejności,
# że krawędzie wskazują tylko "z lewej na prawą"


def dfs(graph, v, visited, result):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(graph, u, visited, result)
    # (1):
    result.insert(0, v)                # tab.insert(n,k) - wstaw do tablicy tab pod indeksem n wartość k
    # (2):
    # result.append(v)

def topological_sort(graph):
    visited = [False] * len(graph)
    result = []
    for v in range(len(graph)):
        if not visited[v]:
            print(v)    # pokazuje nam jak się "cofamy"
            dfs(graph, v, visited, result)
    # (2):
    # result.reverse()
    return result


graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]
print(topological_sort(graph))