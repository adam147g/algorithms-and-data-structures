# The Edmonds-Karp algorithm is a greedy algorithm that computes the maximum flow in a flow network (graph).

from queue import Queue
from collections import deque
from math import inf

def bfs(G, s, t, parent):
    # queue = Queue()
    Q = deque()
    visited = [False] * len(G)
    visited[s] = True
    # queue.put(s)
    Q.append(s)

    # while not queue.empty():
    while Q:

        # u = queue.get()
        u = Q.popleft()
        for v in range(len(G)):
            if not visited[v] and G[u][v] != 0:
                visited[v] = True
                parent[v] = u
                if visited[t]: return True  # WAŻNE CZASOWO !!!
                # queue.put(v)
                Q.append(v)
    return visited[t]


def edmonds_karp_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
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


graph = [[0, 11, 12, 17, 0,  0, 0, 0,  0, 0],
         [0,  0,  0,  0, 0, 14, 0, 0,  0, 0],
         [0,  0,  0,  0, 8,  0, 0, 0,  0, 0],
         [0,  0,  0,  0, 9,  0, 0, 0,  0, 0],
         [0,  0,  0,  0, 0,  0, 7, 0, 10, 0],
         [0,  0,  0,  0, 0,  0, 6, 9,  0, 0],
         [0,  0,  0,  0, 0,  0, 0, 0,  0, 5],
         [0,  0,  0,  0, 0,  0, 0, 0,  0, 3],
         [0,  0,  0,  0, 0,  0, 0, 0,  0, 8],
         [0,  0,  0,  0, 0,  0, 0, 0,  0, 0]]
print(edmonds_karp_algorithm(graph, 0, 9))