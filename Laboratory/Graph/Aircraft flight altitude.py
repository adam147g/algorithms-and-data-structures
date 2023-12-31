# Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty nawigacyjne nad Bajtocją,
# a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy korytarz powietrzny
# e[i] ∈ E powiązany jest z optymalnym pułapem przelotu p[i] ∈ N (wyrażonym w metrach). Przepisy
# dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej
# o t metrów. Napisz algorytm, który sprawdza czy istnieje możliwość przelotu z zadanego punktu
# x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.


def dfs(edges, source, finish, visited, t, optimal):
    if source[1] == finish:
        return True
    for i in range(len(edges)):
        if edges[i][0] == source[1] and not visited[i]:
            if abs(edges[i][2] - optimal) <= t:
                idx = edges.index(source)
                visited[idx] = True
                if dfs(edges, edges[i], finish, visited, t, optimal):
                    return True
    return False


def safe_flight(graph, t, optimal):
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j][0] > i:
                edges.append((i, graph[i][j][0], graph[i][j][1]))
    source = (0, graph[0][0][0])
    finish = graph.index(graph[-1])
    visited = [False] * len(edges)
    possible_edges = []
    for i in range(len(edges)):
        if edges[i][0] == source[0]:
            if abs(edges[i][2] - optimal) < t:
                possible_edges.append(edges[i])
            # if edges[i][2] > optimal:
            #     if optimal + t >= edges[i][2]:
            #         possible_edges.append(edges[i])
            # elif edges[i][2] < optimal:
            #     if optimal - t <= edges[i][2]:
            #         possible_edges.append(edges[i])
        else:
            break

    for i in range(len(possible_edges)):
        if dfs(edges, possible_edges[i], finish, visited, t, optimal):
            return True
        visited = [False] * len(edges)
    return False


graph = [[(1, 10), (2, 7), (3, 3)],
         [(0, 10), (3, 5), (4, 20)],
         [(0, 7), (4, 11), (7, 8)],
         [(0, 3), (1, 5), (4, 14), (5, 5)], [(1, 20), (2, 11), (3, 14), (6, 8)],
         [(3, 5), (6, 9)],
         [(4, 8), (5, 9), (7, 13)],
         [(2, 8), (6, 13), (8, 10)],
         [(7, 10)]]
t = 2
optimal = 8
print(safe_flight(graph, t, optimal))
