from zad8ktesty import runtests
from math import inf


def f(s, t, F, a, b):
    if F[b][a] != inf:
        return F[b][a]
    if s[a] == t[b]:
        F[b][a] = f(s, t, F, a - 1, b - 1)
        return F[b][a]
    F[b][a] = min(f(s, t, F, a - 1, b - 1), f(s, t, F, a, b - 1), f(s, t, F, a - 1, b)) + 1
    return F[b][a]


def napraw(s, t):
    a = len(s)
    b = len(t)
    F = [[inf] * a for _ in range(b)]
    flag = False
    if s[0] != t[0]:
        F[0][0] = 1
    else:
        flag = True
        F[0][0] = 0
    for i in range(1, a):
        if flag or (s[i] != t[0] and not flag):
            F[0][i] = F[0][i - 1] + 1
        else:
            F[0][i] = F[0][i - 1]
            flag = True
    flag = False
    for i in range(1, b):
        if flag or (s[0] != t[i] and not flag):
            F[i][0] = F[i - 1][0] + 1
        else:
            F[i][0] = F[i - 1][0]
            flag = True

    return f(s, t, F, a - 1, b - 1)


runtests(napraw)
