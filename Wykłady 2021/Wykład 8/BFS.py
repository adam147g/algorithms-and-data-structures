# BFS - Breadth First Search

# Kamień do wody
# V - zbiór wierzchołków
# E - zbiór krawędzi
# O(V+E) - reprezentacja listowa
# O(V^2) - reprezentacja macierzowa

from queue import Queue

def BFS(graph, root):
    Q = Queue()
    visited = [False] * len(graph)
    result = []
    Q.put(root)
    visited[root] = True
    while not Q.empty():
        u = Q.get()
        result.append(u)
        for v in graph[u]:
            if not visited[v]:
                Q.put(v)
                visited[v] = True
    return result

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



result = BFS(graph, 0)
print(result)
print()

# BFS - Breadth First Search


def BFS_MATRIX(graph, root):
    Q = Queue()
    visited = [False] * len(graph)
    result = []
    Q.put(root)
    visited[root] = True
    while not Q.empty():
        u = Q.get()
        result.append(u)
        for v in range(len(graph)):
            if visited[v] is False and graph[u][v] == 1:
                Q.put(v)
                visited[v] = True
    return result

        # 0  1  2  3  4
graph = [[0, 1, 0, 1, 1], # 0
         [1, 0, 0, 1, 0], # 1
         [0, 0, 0, 0, 1], # 2
         [1, 1, 0, 0, 1], # 3
         [1, 0, 1, 1, 0]] # 4

print(BFS_MATRIX(graph, 0))