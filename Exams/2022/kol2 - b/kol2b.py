'''
Adam Górka
Algorytm prezentuie funkcię f(i,i), która mówi iaki minimalny koszt potrzebuiemy by dostać się na i-te z kolei
miasto pod warunkiem i
i=0 - nie użyliśmy ieszcze bonusowego warunku
i=1 - użyliśmy iuż warunek
f(i,0) = min{f(i-k, 0)+ C[i]} dla O[i]-O[i-k}<=T
f(i,1) = min{f(i-k, 1)+ C[i] dla O[i]-O[i-k}<=T, f(i-k, 0)+ C[i] dla O[i]-O[i-k}<=2*T
rozwiązanie zostaje odczytywane jako minimum z
f(i, 0) dla O[i]+2*T>=L
f(i, 1) dla O[i]+T>=L
'''
from kol2btesty import runtests
from math import inf

'''
def min_cost(O, C, T, L):
    if 2 * T >= L:
        return 0
    n = len(O)
    for i in range(n):
        O[i] = (O[i], i)
    O.sort(key=lambda x: x[0])
    F = [[inf, inf] for _ in range(n)]
    F[0][0] = C[O[0][1]]
    i = 1
    while i < n:
        k = 1
        while i - k > -1 and O[i][0] - O[i - k][0] <= T:
            F[i][0] = min(F[i][0], F[i - k][0] + C[O[i][1]])
            k += 1
        i += 1
    i = 0
    while i < n and O[i][0] <= 2 * T:
        F[i][1] = C[O[i][1]]
        i += 1
    i = 1
    while i < n:
        k = 1
        while i - k > -1 and O[i][0] - O[i - k][0] <= T:
            F[i][1] = min(F[i][1], F[i - k][1] + C[O[i][1]], F[i - k][0] + C[O[i][1]])
            k += 1
        while i - k > -1 and O[i][0] - O[i - k][0] <= 2 * T:
            F[i][1] = min(F[i][1], F[i - k][0] + C[O[i][1]])
            k += 1
        i += 1
    res = inf
    i = n - 1
    while O[i][0] + T >= L:
        res = min(res, F[i][0], F[i][1])
        i -= 1
    while O[i][0] + 2 * T >= L:
        res = min(res, F[i][0])
        i -= 1
    return res
'''


def min_cost(O, C, T, L):
    oc = [(o, c) for o, c in zip(O, C)]
    oc.append((0, 0))
    oc.append((L, 0))
    oc.sort(key=lambda x: x[0])
    n = len(oc)
    F0 = [inf for _ in range(n)]
    F1 = [inf for _ in range(n)]

    F0[0], F1[0] = 0, 0
    for i in range(1, n):
        m0, m1 = inf, inf
        for j in range(i - 1, -1, -1):
            if oc[i][0] - oc[j][0] > 2 * T:
                break
            if oc[i][0] - oc[j][0] <= T:
                m0 = min(m0, F0[j])
                m1 = min(m1, F1[j])
            else:
                m1 = min(m1, F0[j])

        F0[i] = m0 + oc[i][1]
        F1[i] = m1 + oc[i][1]

    return min(F0[-1], F1[-1])


runtests(min_cost, all_tests=True)
