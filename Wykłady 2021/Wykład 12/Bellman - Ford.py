# Bellman-Ford algorithm for finding the shortest paths from source vertex to all other vertices in
# a given graph in which edge weights may be negative.

# O(V*E)

from math import inf


def relax(edges, distance, parent, j):
    if distance[edges[j][1]] > distance[edges[j][0]] + edges[j][2]:
        distance[edges[j][1]] = distance[edges[j][0]] + edges[j][2]
        parent[edges[j][1]] = edges[j][0]


def bellman_ford_algorithm(edges, source):
    V = 0
    for i in range(len(edges)):
        V = max(V, edges[i][0], edges[i][1])
    E = len(edges)
    distance = [inf] * (V + 1)
    parent = [None] * (V + 1)
    distance[source] = 0
    for _ in range(V - 1):
        for j in range(E):
            relax(edges, distance, parent, j)

    # weryfikacja cykli ujemnych
    for i in range(E):
        if distance[edges[i][1]] > distance[edges[i][0]] + edges[i][2]:
            return False, None, None
    return True, distance, parent


edges = [(0, 1, 8), (5, 4, -2), (3, 5, -1), (0, 2, 10), (3, 2, -4), (1, 3, 1), (4, 2, 1), (2, 5, 2)]

result, distance, parent = bellman_ford_algorithm(edges, 0)

print(parent)
if result:
    i = len(parent) - 1
    while parent[i] is not None:
        print("dist {0} for vertex {1}".format(distance[i], i))
        i -= 1
else:
    print("Graph contains negative weight cycle.")
