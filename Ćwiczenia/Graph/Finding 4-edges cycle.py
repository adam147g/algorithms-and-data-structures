# Proszę podać jak najszybszy algorytm, który znajduje w grafie cykl długości dokładnie 4
# (trywialny algorytm ma złożoność O(n^4), gdzie n to liczba wierzchołków, chodzi
# o rozwiązanie szybsze).


def four_length_cycle(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if i != j:
                count = 0
                result = []
                for k in range(n):
                    if graph[i][k] == 1 and graph[j][k] == 1:
                        count += 1
                        result.append(k)
                    if count == 2:
                        result.append(i)
                        result.append(j)
                        return True, result
    return None


graph = [[0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [1, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 1, 1],
         [0, 0, 0, 0, 1, 0]]

graph_1 = [[0, 1, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [0, 1, 0, 1, 1, 0],
           [0, 0, 1, 0, 0, 1],
           [0, 0, 1, 0, 0, 1],
           [0, 0, 0, 1, 1, 0]]

decision, result = four_length_cycle(graph_1)
print(decision)
print(result)