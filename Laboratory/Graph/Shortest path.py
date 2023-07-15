# Proszę zaimplementować algorytm który dla danego wierzchołka efektywnie znajdzie najkrótszą
# ścieżkę do dowolnego innego wierzchołka za pomocą BFS.

from queue import Queue
from math import inf


def find_shortest_paths(graph, source=0):
    queue = Queue()
    queue.put(source)
    visited = [False] * len(graph)
    visited[source] = True
    distance = [inf] * len(graph)
    distance[source] = 0

    while not queue.empty():
        u = queue.get()
        min_distance = inf
        for v in graph[u]:
            if not visited[v]:
                for g in graph[v]:
                    min_distance = min(min_distance, distance[g])
                distance[v] = min_distance + 1
                queue.put(v)
                visited[v] = True
    return distance


graph = [[1, 2],  # 0
         [0, 3, 4],  # 1
         [0],  # 2
         [1, 5],  # 3
         [1, 6],  # 4
         [3, 7, 8],  # 5
         [4, 11],  # 6
         [5],  # 7
         [5, 9],  # 8
         [8, 10, 11],  # 9
         [9],  # 10
         [6, 9]]  # 11

print(find_shortest_paths(graph))
