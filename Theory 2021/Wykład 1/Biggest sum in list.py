# Znajdź największą sumę kolejnych elementów tablicy

from time import time
from random import seed, randint

seed(42)


def getdata(n):
    return [randint(-100, 100) for _ in range(n)]


# Szukanie każdy z każdym - O(n^3)

def ssp3(T):
    result = 0
    for i in range(n):
        for j in range(i, n):
            partial = 0
            for k in range(i, j + 1):
                partial += T[k]
            result = max(partial, result)
    return result


# Ustawianie początki na każdy po kolei, ale sumowanie po kolei już - O(n^2)

def ssp2(T):
    result = 0
    for i in range(n):
        partial = 0
        for j in range(i, n):
            partial += T[j]
            result = max(partial, result)
    return result


# Dziel i zwyciężaj - podział na mniejsze połówki i tam rozwiązywanie problemu - O(n logn)

def ssprec(T, b, e):
    n = e - b + 1
    m = b + (e - b) // 2
    if n == 0: return 0
    if n == 1: return max(0, T[b])

    res_l = ssprec(T, b, m)
    res_r = ssprec(T, m + 1, e)

    span_l = span_r = 0
    partial = 0
    for i in range(m, b - 1, -1):
        partial += T[i]
        span_l = max(partial, span_l)
    partial = 0
    for i in range(m + 1, e + 1):
        partial += T[i]
        span_r = max(partial, span_r)

    return max(res_l, res_r, span_l + span_r)


def sspdc(T):
    return ssprec(T, 0, len(T) - 1)


# Sumowanie i zatrzymywanie, gdy wynik będzie ujemny - O(n)

def ssp1(T):
    result = 0
    partial = 0
    for i in range(n):
        partial += T[i]
        partial = max(0, partial)
        result = max(partial, result)
    return result


n = int(input("n= "))
T = getdata(n)
start = time()

result = ssp1(T)
czas1 = time()
print("Wynik= ", result)
print("Czas działania ssp1: %f sek." % (czas1 - start))
print()

result = sspdc(T)
czas2 = time()
print("Wynik= ", result)
print("Czas działania sspdc: %f sek." % (czas2 - czas1))
print()

result = ssp2(T)
czas3 = time()
print("Wynik= ", result)
print("Czas działania ssp2: %f sek." % (czas3 - czas2))
print()

result = ssp3(T)
czas4 = time()
print("Wynik= ", result)
print("Czas działania ssp3: %f sek." % (czas4 - czas3))
print()

end = time()
print("Czas działania całego programu: %f sek." % (end - start))