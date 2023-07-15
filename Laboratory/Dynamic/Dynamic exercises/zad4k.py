from zad4ktesty import runtests
from math import inf


def f(T, F, i, j):
    if F[i][j] != inf:
        return F[i][j]
    # if i < 0 or j < 0:
    #     return inf
    F[i][j] = min(f(T, F, i - 1, j), f(T, F, i, j - 1)) + T[i][j]
    return F[i][j]


def falisz(T):
    n = len(T)
    F = [[inf] * n for _ in range(n)]
    F[0][0] = T[0][0]
    for i in range(1, n):
        F[i][0] = F[i - 1][0] + T[i][0]
        F[0][i] = F[0][i - 1] + T[0][i]

    return f(T, F, n - 1, n - 1)

runtests(falisz)
