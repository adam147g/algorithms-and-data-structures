from queue import PriorityQueue


# from math import inf


def dijkstra_algorithm(graph, source, finish):
    n = len(graph)
    queue = PriorityQueue()
    queue.put((0, source, None))
    # visited = [False] * n
    # distance = [inf] * n
    # distance[source] = 0
    while not queue.empty():
        dist, u, earlier = queue.get()
        if u == finish:
            return dist
        for v in range(n):
            a=[0, earlier]
            # if graph[u][v] not in [0, earlier] and not visited[v]:
                # if distance[v] > dist + graph[u][v]:
                #     distance[v] = dist + graph[u][v]
                #     queue.put((dist + graph[u][v], v, graph[u][v]))
            if graph[u][v] not in [0, earlier]:
                queue.put((dist + graph[u][v], v, graph[u][v]))
        # visited[u] = True

    # return distance[finish]
    return None


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 9, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]

print(dijkstra_algorithm(G1, 5, 2))

G2 = [[0, 300, 50, 0],
      [300, 0, 100, 100],
      [50, 100, 0, 50],
      [0, 100, 50, 0]]
print(dijkstra_algorithm(G2, 0, 3))

G3 = [[0, 1, 0],
      [1, 0, 1],
      [0, 1, 0]]
print(dijkstra_algorithm(G3, 0, 2))
