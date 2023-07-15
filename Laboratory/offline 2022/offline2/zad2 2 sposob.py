from zad2testy import runtests
from math import inf


def merge(T, p, q, r):
    L = T[p:q + 1]
    R = T[q + 1:r + 1]
    L.append([inf, inf])
    R.append([inf, inf])
    i = j = 0
    for k in range(p, r + 1):
        if L[i][0] <= R[j][0]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


def merge_sort(T, p, r):
    if len(T) <= 1:
        return T
    elif p < r:
        m = (p + r) // 2
        merge_sort(T, p, m)
        merge_sort(T, m + 1, r)
        merge(T, p, m, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][1] >= x[1]:
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


def depth(L):
    n = len(L)
    quicksort(L, 0, n - 1)
    merge_sort(L, 0, n - 1)
    A = [0] * n
    i = 0
    next_start = 0
    curr_max = 0
    while i < n:
        j = i + 1
        flag = True
        while j < n and L[j][0] <= L[i][1]:
            if L[j][1] <= L[i][1]:
                A[i] += 1
            elif flag:
                next_start = j
                flag = False
            j += 1
        if A[i] > curr_max:
            curr_max = A[i]
        if flag:
            next_start = j
        i = next_start
    return curr_max


runtests(depth)
