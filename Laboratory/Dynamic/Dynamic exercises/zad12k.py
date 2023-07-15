from zad12ktesty import runtests
from math import inf


def sum(arr, p, r):
    total = 0
    for i in range(p, r + 1):
        total += arr[i]
    return total


def autostrada(arr, k):
    n = len(arr)
    F = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        F[1][i] = F[1][i - 1] + arr[i - 1]
    for i in range(1, k + 1):
        F[i][1] = arr[0]

    for i in range(2, k + 1):
        for j in range(2, n + 1):
            best = inf
            for p in range(1, j + 1):
                best = min(best, max(F[i - 1][p], sum(arr, p, j - 1)))
            F[i][j] = best

    return F[k][n]


runtests(autostrada, all_tests=True)
