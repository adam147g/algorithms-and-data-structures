from egzP8btesty import runtests
from math import inf


def robot(G, P):
    n = len(G)
    G2 = [[inf for _ in range(n)] for _ in range(n)]
    for u in range(n):
        G2[u][u] = 0
        for v in G[u]:
            G2[u][v[0]] = v[1]
            G2[v[0]][u] = v[1]

    for k in range(n):
        for u in range(n):
            for v in range(n):
                G2[u][v] = min(G2[u][v], G2[u][k] + G2[k][v])

    result = 0
    for i in range(1, len(P)):
        result += G2[P[i - 1]][P[i]]
    return result


runtests(robot, all_tests=True)
