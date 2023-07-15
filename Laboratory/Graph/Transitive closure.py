# Proszę zaproponować algorytm obliczający domknięcie przechodnie grafu reprezentowanego w postaci
# macierzowej (domknięcie przechodnie grafu G to taki graf H, że w H mamy krawędź z u do v wtedy
# i tylko wtedy gdy w G jest ścieżka skierowana z u do v).


def transitive_closure(graph):
    n = len(graph)
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or graph[i][j] == 1:
                reach[i][j] = True
    for k in range(1, n):
        for u in range(n):
            for v in range(n):
                if reach[u][v] or (reach[u][k] and reach[k][v]):
                    reach[u][v] = True
    return reach


graph = [[0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0]]

reach = transitive_closure(graph)

for i in range(len(reach)):
    for j in range(len(reach)):
        print(reach[i][j], end='\t')
    print()
