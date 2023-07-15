from random import randint


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
    k = i + 1
    l = i + 1
    if k <= r:
        while l <= r:
            while k <= r and A[k] == x:
                k += 1
                l += 1
            while l <= r and A[l] != x:
                l += 1
            if l <= r:
                A[k], A[l] = A[l], A[k]
            k += 1
            l += 1
    if k > 1:
        while k - 1 < r and A[k - 2] == A[k - 1]:
            k += 1
        return i, k - 2
    return i, i

def quicksort(A, p, r):
    flag = True
    while p < r:
        x, y = partition(A, p, r)
        quicksort(A, p, x - 1)
        quicksort(A, y + 1, r)
        if not flag:
            break
        flag = False


n = 11
T = [randint(0, 5) for i in range(n)]
print(T)
quicksort(T, 0, len(T) - 1)
print(T)
# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while arr[i] < pivot:
#             i += 1
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1
#         if i >= j:
#             return j
#         arr[i], arr[j] = arr[j], arr[i]
#
#
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi)
#         quickSort(arr, pi + 1, high)
#
#
# ''' Function to print an array '''
#
#
# def printArray(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()
#
#
# # Driver code
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("Sorted array:")
# printArray(arr, n)
