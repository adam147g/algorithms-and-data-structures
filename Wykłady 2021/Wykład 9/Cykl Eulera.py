# The eulerian path is one that passes through each edge exactly ones.


def dfs(graph, v, result):
    for i in range(len(graph)):
        if graph[v][i] == 1:
            graph[v][i], graph[i][v] = 0, 0
            print(i, end=' ')
            dfs(graph, i, result)
    result.append(v)            # tworzę ścieżkę Eulera od tyłu... później ją odwrócę


def eulerian_path(graph):
    for i in range(len(graph)):  # sprawdzanie parzystości stopnia każdego z wierzchołków
        edges = 0
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                edges += 1
        if edges % 2 == 1:
            return False

    result = []
    dfs(graph, 0, result)

    return result


graph = [[0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 1],
         [1, 1, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 1, 1, 1, 1, 0]]

print(eulerian_path(graph))
print("-------------------")
graph_1 = [[0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 1, 0],
           [0, 1, 0, 1, 1, 1],
           [0, 1, 1, 0, 1, 1],
           [1, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 0]]
print(eulerian_path(graph_1))
