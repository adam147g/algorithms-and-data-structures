from random import randint


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            quicksort(A, p, q - 1)
            p = q + 1
        else:
            quicksort(A, q + 1, r)
            r = q - 1


n = 11
T = [randint(0, 20) for i in range(n)]
print(T)
quicksort(T, 0, len(T) - 1)
print(T)
