from kol2atesty import runtests
from math import inf


# f(i,d) - min liczba pkt. kontrolnych, przez które prowadzi Marian, gdy dojeżdamy
#         do i-tego pkt, a za kierownicą siedzi d
# f(i,J) - min{ f(i-1, M), f(i-2, M), f(i-3, M) }
# f(i,M) - min{ f(i-1, J) + cost(i-1, i),
#               f(i-2, J) + cost(i-2, i),
#               f(i-3, J) + cost(i-3, i) }

# f(0,J) = inf
# f(0,M) = 0

def f(DP, i, d, t):
    if i < 0:
        return 0
    if DP[i][d] != inf or (i==0 and d==0):
        return DP[i][d]
    if d == 1:  # Jacek
        DP[i][d] = min(f(DP, i - 1, 0, t), f(DP, i - 2, 0, t), f(DP, i - 3, 0, t))
    elif d == 0:  # Marian
        DP[i][d] = min(f(DP, i - 1, 1, t) + t[i - 1][1], f(DP, i - 2, 1, t) + t[i - 2][1],
                       f(DP, i - 3, 1, t) + t[i - 3][1])
    return DP[i][d]


def drivers(P, B):
    n = len(P)
    P.sort(key=lambda x: x[0])  # mozliwe e niepotrzebne
    print(P)
    t = [(0, 0)]
    i, j = 0, 1
    while j < n:
        if P[j][1]:
            t.append((P[j][0], P[j][0] - t[i][0] - 1))
            i += 1
        j += 1
    t.append((B, B - t[i][0] - 1))
    print(t)
    DP = [[inf, inf] for _ in range(len(t))]
    DP[0][1] = 0

    return min(f(DP, len(t) - 1, 1, t), f(DP, len(t) - 1, 0, t))


runtests(drivers, all_tests=False)
