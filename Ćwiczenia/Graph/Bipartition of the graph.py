# Proszę zaimplementować algorytm sprawdzający czy graf jest dwudzielny.
from queue import Queue


def bipartite_graph(graph, root):
    queue = Queue()
    colors = [-1] * len(graph)
    queue.put(root)
    colors[root] = 1
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if colors[v] == -1:
                if colors[u] == 1:
                    colors[v] = 0
                elif colors[u] == 0:
                    colors[v] = 1
                queue.put(v)
            elif colors[u] == colors[v]:
                return False
    return True


graph = [[2, 3, 4, 5],  # 0
         [2, 3, 4],  # 1
         [0, 1, 6],  # 2
         [0, 1],  # 3
         [0, 1, 6],  # 4
         [0, 6],  # 5
         [2, 4, 5]]  # 6

print(bipartite_graph(graph, 0))
