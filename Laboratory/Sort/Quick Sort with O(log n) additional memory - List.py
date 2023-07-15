# Proszę zaimplementować Quick Sort tak, by zawsze używał najwyżej O(logn) dodatkowej pamięci.

from random import randint


def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q - p < r - q:
            quicksort(T, p, q - 1)
            p = q + 1
        else:
            quicksort(T, q + 1, r)
            r = q - 1


'''
Użycie pamięci:
S(n) = S(n/2) + c
     = S(n/4) + 2c
     = S(n/8) + 3c ...
     = c*log(n)
'''

n = 11
T = [randint(0, 20) for _ in range(n)]
print(T)
quicksort(T, 0, len(T) - 1)
print(T)
