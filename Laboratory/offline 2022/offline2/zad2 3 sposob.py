from zad2testy import runtests


def partition_increasing(A, p, r):
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

def depth(L):
    n = len(L)
    quicksort_increasing(L, 0, n - 1)
    i = 0
    while i < n:
        j = i + 1
        flag = False
        biggest_idx = i
        if j < n - 1:
            if L[i][0] == L[j + 1][0]:
                if L[i][1] < L[j][1]:
                    biggest_idx = j
                while j < n - 1 and L[i][0] == L[j + 1][0]:
                    if L[biggest_idx][1] < L[j + 1][1]:
                        biggest_idx = j + 1
                    j += 1
                    flag = True

            if L[i][0] == L[j][0] and L[i][1] < L[j][1]:
                L[i], L[j] = L[j], L[i]
        if flag:
            L[i], L[biggest_idx] = L[biggest_idx], L[i]
            i = j + 1
        else:
            i = j

    i = 0
    next_start = 0
    curr_max = 0
    while i < n:
        curr = 0
        j = i + 1
        flag = True
        while j < n and L[j][0] <= L[i][1]:
            if L[j][1] <= L[i][1]:
                curr += 1
            elif flag:
                next_start = j
                flag = False
            j += 1
        if curr > curr_max:
            curr_max = curr
        if flag:
            next_start = j
        i = next_start
    return curr_max

'''
T = [[1, 3], [1, 5], [1, 1], [1, 5], [2, 8], [2, 30], [-1, 1235], [1, 7], [1, 6], [-5, 20], [0, 0]]
print(depth(T))
print(T)
L = [[10, 20], [1, 30], [1, 5], [2, 10], [25, 29], [1, 7], [10, 31], [9, 11], [10, 15], [3, 4],[0,0], [3, 30]]
print(depth(L))
'''
runtests(depth)