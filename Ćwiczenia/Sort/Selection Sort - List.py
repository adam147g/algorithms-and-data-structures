# Proszę zaimplementować sortowanie tablicy w czasie O(n^2).

def selection_sort(T):
    n = len(T)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if T[minIndex] > T[j]:
                minIndex = j
        T[minIndex], T[i] = T[i], T[minIndex]
    return T

T = [5, 4, 3, 7, 2, 1]
print(selection_sort(T))