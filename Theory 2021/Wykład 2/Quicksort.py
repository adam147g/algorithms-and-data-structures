'''
Sortowanie
Zadanie to znalezc ciag a1', ..., an' będący pewrutacją ciągu taki, że a1'<= a2'<= a3'... <= an'
Warianty:
-tablica
-lista (1 lub 2 -kierunkowa)
-plik
'''

from random import randint


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  # swap(A[i],A[j[)
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# QuickSort#
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)  # podzial tablicy na el <= x i > x, x jest o indeksie q
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    return A


def QuickSort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        QuickSort(A, p, q - 1)
        p = q + 1
    return A


tab = [randint(0, 100) for i in range(10)]
print(tab)
print("QuckSorty")
print(quicksort(tab, 0, len(tab) - 1))
tab = [randint(0, 100) for _ in range(10)]
print(QuickSort(tab, 0, len(tab) - 1))

