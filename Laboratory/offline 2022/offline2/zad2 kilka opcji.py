from zad2testy import runtests
from random import randint


#####################33
def partitionnn(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
    k = i + 1
    l = i + 1
    if k <= r:
        while l <= r:
            while k <= r and A[k][0] == x:
                k += 1
                l += 1
            while l <= r and A[l][0] != x:
                l += 1
            if l <= r:
                A[k], A[l] = A[l], A[k]
            k += 1
            l += 1
    if k > 1:
        while k - 1 < r and A[k - 2][0] == A[k - 1][0]:
            k += 1
        return i, k - 2
    return i, i


def quicksorttt(A, p, r):
    while p < r:
        x, y = partitionnn(A, p, r)
        quicksorttt(A, p, x - 1)
        p = y + 1


###################
# można spróbować zapamiętywać zamiast jednego while'a
# można zrobić quickersort z podziałem na < pivot, == pivot i > pivot

def partition_increasing(A, p, r):
    # rand = randint(p, r)
    # rand = (p+r)//2
    # A[rand], A[r] = A[r], A[rand]
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quicksort_increasing(A, p, r):
    while p < r:
        q = partition_increasing(A, p, r)
        if q - p < r - q:
            quicksort_increasing(A, p, q - 1)
            p = q + 1
        else:
            quicksort_increasing(A, q + 1, r)
            r = q - 1


def partition(arr, low, high):
    pivot = arr[low][0]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i][0] < pivot:
            i += 1
        j -= 1
        while arr[j][0] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)


def depth(L):
    n = len(L)
    # quicksort_increasing(L, 0, n - 1)
    quicksorttt(L, 0, n - 1)
    # quickSort(L, 0, n - 1)
    i = 0
    next_start = 0
    curr_max = 0
    while i < n:
        intervals_start_with_me = 0
        max_start_with_me = L[i][1]
        j = i + 1
        flag = True
        while j < n and L[i][0] == L[j][0]:
            if L[j][1] > max_start_with_me:
                max_start_with_me = L[j][1]
            intervals_start_with_me += 1
            j += 1
        curr = 0
        while j < n and L[j][0] <= max_start_with_me:
            if L[j][1] <= max_start_with_me:
                curr += 1
            elif flag:
                next_start = j
                flag = False
            j += 1
        if curr + intervals_start_with_me > curr_max:
            curr_max = curr + intervals_start_with_me
        if flag:
            next_start = j
        i = next_start
        if i < n:
            while i > 0 and L[i][0] == L[i - 1][0]:
                i -= 1
    return curr_max


runtests(depth)
