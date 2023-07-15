# Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, żeby wjechać
# na prom. Prom ma dwa pasy (lewy i prawy) oba długości L. Proszę napisać program,
# który wyznacza, które samochody powinny pojechać na który pas, żeby na promie
# zmieściło się jak najwięcej aut. Auta muszą wjeżdżać w takiej kolejności, w jakiej
# są podane w tablicy A.

from math import inf


def cars_on_ferry(A, L):
    n = len(A)
    DP = [[[-inf] * (L + 1) for _ in range(L + 1)] for _ in range(n)]
    for i in range(L):
        for j in range(L):
            DP[0][i][j] = 0
    return solution(0, L, L, A, DP)


def solution(i, g, d, A, DP):
    if DP[i][g][d] != -inf:
        return DP[i][g][d]
    a = b = 0
    if A[i] <= g:
        a = solution(i + 1, g - A[i], d, A, DP) + 1
    if A[i] <= d:
        b = solution(i + 1, g, d - A[i], A, DP) + 1
    DP[i][g][d] = max(a, b)
    return DP[i][g][d]


A = [1, 1, 2, 3, 5, 8, 13]
L = 8
print(cars_on_ferry(A, L))
