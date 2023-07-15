'''
Adam Górka
Algorytm tworzy listę pojemności poj o długości n, ponieważ dłuższa nie może być, o wartościach T
przechodzi po kolei dla każdej wartości z listy A i sprawdza jaki jest pierwszy magazyn w którym pomieści się
analizowany transport i odejmuje od listy poj pod danym indeksem
Po każdym takim zapisaniu uaktualniamu wartość "ostatni" i zwracamy ją jako miejsce ostatniego transportu
'''
from egz2atesty import runtests


def coal(A, T):
    n = len(A)
    print(T, n)
    poj = [T] * n
    k = 1
    ostatni = None
    poj[0] -= A[0]
    for i in range(1, n):
        for j in range(i + 1):
            if poj[j] >= A[k]:
                poj[j] -= A[k]
                k += 1
                ostatni = j
                break
    return ostatni


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=True)
