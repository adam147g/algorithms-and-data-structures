# Sortowanie tablicy rozmiaru n zawierającej logn róznych wartości.

from math import log2, inf


def counting_sort(T, k):
    A = [0] * k
    B = [0] * len(T)
    for i in range(len(T)):
        A[T[i]] += 1
    for i in range(1, k):
        A[i] += A[i - 1]
    for i in range(len(T) - 1, -1, -1):
        A[T[i]] -= 1
        B[A[T[i]]] = T[i]

    for i in range(len(T)):
        T[i] = B[i]


def insertion_sort(T):
    for i in range(len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    # return T


def binary_search(A, x, p=0, r=None):
    if r == None:
        r = len(A) - 1
    if r >= p:
        mid = (p + r) // 2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            return binary_search(A, x, mid + 1, r)
        else:
            return binary_search(A, x, p, mid - 1)
    return -1


def sort(T):
    A = [-inf] * int(log2(len(T)))
    count = 0
    for i in range(len(T)):
        if binary_search(A, T[i]) == -1:  # binary - O(log rozmiaru tablicy) - czyli tu O(log(logn))
            A[0] = T[i]
            insertion_sort(A)
            if count < int(log2(len(T))) - 1:
                count += 1
            else:
                break
    print(A)

    for i in range(len(T)):
        T[i] = binary_search(A, T[i])

    print()
    print(T)
    counting_sort(T, len(A))
    print(T)
    for i in range(len(T)):
        T[i] = A[T[i]]
    return T


T = [38, 19, 38, 38, 271, 271, 19, 271, 271, 33, 33, 33, 19, 33, 19, 33]
print(T)
print()
print(sort(T))
