# Floyd-Warshall algorithm for finding the shortest paths between every pair of vertices in a given
# directed weighted graph.

# O(V^3)

from math import inf


def Floyd_Warshall_algorithm(graph):
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    # k=0
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    '''
    Ekonomiczniej ^^, ale z kopiowaniem
    
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 0:
                if i!=j:
                    graph[i][j] = inf
    '''

    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance


def print_solution(distance):
    for i in range(len(distance)):
        for j in range(len(distance)):
            print(distance[i][j], end="\t")
        print()


graph = [[0, 0, 0, 0, -1, 0],
         [1, 0, 0, 2, 0, 0],
         [0, 2, 0, 0, 0, 10],
         [-4, 0, 0, 0, 3, 0],
         [0, 7, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0]]
distance = Floyd_Warshall_algorithm(graph)
print_solution(distance)
