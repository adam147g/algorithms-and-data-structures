'''
Adam Górka
Algorytm spełnia funkcję f, gdzie
f(i,j) - oznacza maksymalną ilość studentów, jaką mogą pomieścić budynki nie nachodzące się na siebie
         w kolejności od lewej strony do i-tego indeksu o maksymalnej łącznej cenie budowy <= j.

f(0,j) =  0,                        dla j  < T[0][3]
         (T[0][2]-T[0][1])*T[0][0], dla j >= T[0][3]

f(i,j) = max{ f(i-1,j), (T[i][2]-T[i][1])*T[i][0],  f(parent[i], j - T[i][3]) + (T[i][2]-T[i][1])*T[i][0]}
                                                ,gdzie parent[i] - pierwszy
                                                nienachodzący na i-ty budynek
Lista parent jest wypełniana w linijkach 40-44.
Po wypełnieniu macierzy F, znajdujemy listę budynków, zapomocą funkcji get_res,
rekurencyjnie przechodząc po tablicy i sprawdzając, które budynki wybieraliśmy by uzyskać optymalne rozwiązanie.
'''
# Poprawione na n(logn)

from zad4testy import runtests


def binary_search(T, x, p, r):
    if r < p:
        return None
    if p == r and p == 0:
        if T[0][2] < x:
            return 0
        return None
    k = (p + r) // 2
    if T[k + 1][2] >= x > T[k][2]:
        return k
    elif T[k][2] >= x:
        return binary_search(T, x, p, k - 1)
    return binary_search(T, x, k + 1, r)


def get_res(T, F, parent, idx, val, res):
    if idx is None:
        return res
    if idx == 0:
        if val >= T[0][3]:
            res.append(T[0][4])
        return res
    if F[idx - 1][val] == F[idx][val]:
        return get_res(T, F, parent, idx - 1, val, res)
    res.append(T[idx][4])
    return get_res(T, F, parent, parent[idx], val - T[idx][3], res)


def select_buildings(T, p):
    n = len(T)
    # print(T)
    for i in range(n):
        T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    T.sort(key=lambda x: x[2])
    parent = [None] * n
    F = [[0 for _ in range(p + 1)] for _ in range(n)]
    for i in range(1, n):
        parent[i] = binary_search(T, T[i][1], 0, i - 1)
    for val in range(T[0][3], p + 1):
        F[0][val] = (T[0][2] - T[0][1]) * T[0][0]
    for idx in range(1, n):
        for val in range(p + 1):
            F[idx][val] = F[idx - 1][val]
            if parent[idx] is not None and val >= T[idx][3] and \
                    F[parent[idx]][val - T[idx][3]] + (T[idx][2] - T[idx][1]) * T[idx][0] > F[idx][val]:
                F[idx][val] = F[parent[idx]][val - T[idx][3]] + (T[idx][2] - T[idx][1]) * T[idx][0]
            elif parent[idx] is None and val >= T[idx][3] and (T[idx][2] - T[idx][1]) * T[idx][0] > F[idx][val]:
                F[idx][val] = (T[idx][2] - T[idx][1]) * T[idx][0]

    result = []
    result = get_res(T, F, parent, n - 1, p, result)
    return result


runtests(select_buildings)
