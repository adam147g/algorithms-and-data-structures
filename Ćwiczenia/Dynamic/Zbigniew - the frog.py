# Pewna żaba skacze po osi liczbowej. Ma się dostać z 0 do n-1., skacząc wyłącznie
# w kierunku większych liczb. Skok z liczby i do j (j>i) kosztuje ją j-i jednostek
# energii, a jej energia nigdy nie może spaść poniżej 0. Na początku żaba ma 0
# jednostek energi, ale na szczęście na niektórych liczbach - także na 0 - leżą
# przekąski o określonej wartości energetycznej (wartości przekąski dodaje się do
# aktualnej energii żaby). Proszę zaproponować algorytm, który oblicza minimalną
# liczbę skoków potrzebną na dotarcie z 0 do n-1 mając daną tablicę A z wartościami
# energetycznymi przekąsek na każdej z liczb.

from math import inf
# Złożoność: O(s*n^2), gdzie n to rozmiar tablicy, a s to suma jej elementów


def SUM(A):
    s = 0
    for i in range(len(A)):
        s += A[i]
    return s


def zbigniew(A):
    n = len(A)
    maxE = SUM(A)
    D = [[inf for _ in range(maxE + 1)] for __ in range(n)]
    D[0][A[0]] = 0  # Warunek początkowy

    for j in range(1, n):
        for e in range(maxE + 1):
            for i in range(0, j):
                dk = inf
                de = e - (A[j] - (j - i))
                if 0 <= de <= maxE and (j - i) <= de:
                    dk = D[i][de] + 1
                D[j][e] = min(D[j][e], dk)

    minJumps = inf
    for e in range(maxE + 1):
        minJumps = min(minJumps, D[n - 1][e])

    if minJumps == inf:
        return -1
    return minJumps


A = [5, 0, 0, 3, 2, 0, 7, 1, 5, 1]
print(zbigniew(A))
