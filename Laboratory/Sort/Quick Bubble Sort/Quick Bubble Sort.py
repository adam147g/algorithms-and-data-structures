
from quick_bubble_sort_tests import runtests


def Q_Sort(I):
    def quicksort(I, start, stop):
        i = start
        j = stop
        pivot = (start + stop) // 2

        while i < j:
            while I[i] < I[pivot]:
                i += 1
            while I[j] > I[pivot]:
                j -= 1
            if i < j:
                I[i], I[j] = I[j], I[i]
                i += 1
                j -= 1

        if start < j:
            quicksort(I, start, pivot - 1)
        if i < stop:
            quicksort(I, pivot + 1, stop)

    quicksort(I, 0, len(I) - 1)
    return I, None


def bubblesort(lista):
    n = len(lista)
    liczba_porownan = 0
    while n > 1:
        for i in range(1, n):
            if lista[i - 1] > lista[i]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                liczba_porownan += 1
        n -= 1
    return lista, liczba_porownan


runtests(Q_Sort,bubblesort)