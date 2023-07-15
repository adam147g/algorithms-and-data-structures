from zad10ktesty import runtests
from math import inf


def dywany(N):
    print(N)
    F = [inf] * (N + 1)
    F[0] = 0
    F[1] = 1
    p = [None] * (N + 1)
    p[1] = 1
    for i in range(2, N + 1):
        j = int(i ** (1 / 2))
        if j * j == i:
            F[i] = 1
            p[i] = int(i ** (1 / 2))
        while j > 0:
            if F[i - j * j] + 1 < F[i]:
                F[i] = F[i - j * j] + 1
                p[i] = j
            j -= 1
    x = N
    res = []
    while p[x] is not None:
        res.append(p[x])
        x = x - p[x] ** 2
    return res


runtests(dywany)
