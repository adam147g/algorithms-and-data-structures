from zad3ktesty import runtests
from math import inf


def ksuma(T, k):
    # print(T, k)
    if k == 1:
        return sum(T)
    n = len(T)
    if k >= n:
        return min(T)
    F = [inf] * n
    for i in range(k):
        F[i] = T[i]
    for i in range(k, n):
        j = i - 1
        while j >= i - k:
            F[i] = min(F[j] + T[i], F[i])
            j -= 1

    i = n - 2
    res = F[n - 1]
    while i >= n - k:
        res = min(res, F[i])
        i -= 1
    return res


runtests(ksuma)
