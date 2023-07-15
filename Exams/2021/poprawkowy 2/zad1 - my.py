# Adam Górka
# Algorytm sprawdza które prostokąty i oraz j się przecinają i wpisuje do tablicy
# T ich wspólne pole w miejscu T[i][j]

from zad1testy import runtests
from math import inf


def rect(D):
    T = [[0] * len(D) for _ in range(len(D))]

    for i in range(len(D)):
        for j in range(len(D)):
            if i != j and T[i][j] == 0:
                if D[i][0] <= D[j][0] and D[i][2] >= D[j][2]:
                    x = D[j][2] - D[j][0]
                elif D[i][0] <= D[j][0] and D[i][2] <= D[j][2]:
                    x = D[i][2] - D[j][0]
                elif D[j][0] <= D[i][0] and D[j][2] >= D[i][2]:
                    x = D[i][2] - D[i][0]
                elif D[i][0] >= D[j][0] and D[i][2] >= D[j][2]:
                    x = D[j][2] - D[i][0]
                else:
                    x = 0
                if D[i][2] <= D[j][0]:
                    x = 0

                if D[i][1] <= D[j][1] and D[i][3] >= D[j][3]:
                    y = D[j][3] - D[j][1]
                elif D[i][1] <= D[j][1] and D[i][3] <= D[j][3]:
                    y = D[i][3] - D[j][1]
                elif D[j][1] <= D[i][1] and D[j][3] >= D[i][3]:
                    y = D[i][3] - D[i][1]
                elif D[i][1] >= D[j][1] and D[i][3] >= D[j][3]:
                    y = D[j][3] - D[i][1]
                else:
                    y = 0
                if D[i][3] <= D[j][1]:
                    y = 0
                T[i][j] = x * y

    min = inf
    idx = inf
    for i in range(len(T)):  # algorytm podsumowuje pole, które łącznie przecina prostokąt i
        for j in range(1, len(T)):
            T[i][0] += T[i][j]  # i zapisuje je w T[i][0]
    for i in range(len(T)):
        if T[i][0] < min:
            min = T[i][0]
            idx = i  # szukamy indeksu o najmniejszej sumie przecinanych pól
    return idx


# z uwagi na zapisywanie w tablicy T, algorytm ma złożoność O(N^2)
# złożoność pamięciowa również O(N^2)
runtests(rect)
