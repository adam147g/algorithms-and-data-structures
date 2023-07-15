# DFS - Depth First Search

# V - zbiór wierzchołków
# E - zbiór krawędzi

# 1st solution

def DFS(graph, root):
    visited = [False] * len(graph)
    result = [root]

    def dfs_visit(u, graph, visited, result):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                result.append(v)
                dfs_visit(v, graph, visited, result)

    dfs_visit(root, graph, visited, result)
    return result


# 2nd solution

def dfs(graph, u, visited):
    if u not in visited:
        visited.append(u)
        for n in graph[u]:
            dfs(graph, n, visited)
    return visited


graph = [[1, 8],        # 0
         [0],           # 1
         [3, 4, 5, 8],  # 2
         [2],           # 3
         [2, 7],        # 4
         [2, 6],        # 5
         [5, 7, 8],     # 6
         [4, 6],        # 7
         [0, 2, 6]]     # 8

#     3 --- 2 --- 8 --- 0 ---1
#          / \     \
#         /   \     \
#        4 --- 5 --- 6
#         \         /
#          \-- 7 --/

result1 = DFS(graph, 0)
print(result1)
print()
result2 = dfs(graph, 0, [])
print(result2)
print()


# DFS - Depth First Search

def DFS_MATRIX(graph, root):
    visited = [False] * len(graph)
    result = []
    dfs_visit(root, graph, visited, result)
    return result


def dfs_visit(u, graph, visited, result):
    visited[u] = True
    result.append(u)
    for i in range(len(graph)):
        if visited[i] is False and graph[u][i] == 1:
            dfs_visit(i, graph, visited, result)

        # 0  1  2  3  4
graph = [[0, 1, 0, 1, 1], # 0
         [1, 0, 0, 1, 0], # 1
         [0, 0, 0, 0, 1], # 2
         [1, 1, 0, 0, 1], # 3
         [1, 0, 1, 1, 0]] # 4

print(DFS_MATRIX(graph, 2))