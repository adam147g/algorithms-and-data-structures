from Exercise_1_tests import runtests


def swap(T, value_1, value_2):
    T[value_1 // len(T)][value_1 % len(T)], T[value_2 // len(T)][value_2 % len(T)] = \
        T[value_2 // len(T)][value_2 % len(T)], T[value_1 // len(T)][value_1 % len(T)]


def partition(T, l, r):
    T[r // len(T)][r % len(T)], T[(l + r) // 2 // len(T)][((l + r) // 2) % len(T)] = \
        T[(l + r) // 2 // len(T)][((l + r) // 2) % len(T)], T[r // len(T)][r % len(T)]
    pivot = T[r // len(T)][r % len(T)]
    i = l - 1
    for j in range(l, r):
        if T[j // len(T)][j % len(T)] <= pivot:
            i += 1
            swap(T, i, j)
    swap(T, i + 1, r)
    return i + 1


def select(T, p, r, x):
    if p == r:
        return
    q = partition(T, p, r)
    if x == q:
        return
    elif x < q:
        return select(T, p, q - 1, x)
    else:
        return select(T, q + 1, r, x)


def Median(T):
    n = len(T)
    diagonal = 0
    for i in range(n):
        diagonal += i

    select(T, 0, n * n - 1, diagonal)
    select(T, diagonal, n * n - 1, diagonal + n - 1)
    i = 0
    j = n // 2
    diagonal_min_val = T[diagonal // len(T)][diagonal% len(T)]
    while i < j:
        T[i][i], T[j][i] = T[j][i], T[i][i]
        i += 1
    if n % 2 == 0:
        j -= 1
    while i < n:
        T[i][i], T[j][i] = T[j][i], T[i][i]
        i += 1
    i = 1
    j = 0
    while i * n + j < n * n - 1:
        if i * n + j < diagonal or i * n + j > diagonal + n - 1:
            if T[i][j] > diagonal_min_val:
                T[i][j], T[n-1-i][n-j-1] = T[n-1-i][n-j-1], T[i][j]
        j += 1
        if j == n - 1 or i == j:
            j = 0
            i += 1
    return T


runtests(Median)
# T = [
#     [2, 5, 2, 5],
#     [2, 5, 5, 2],
#     [2, 5, 2, 2],
#     [2, 5, 5, 5]
# ]
# Median(T)
# for i in T:
#     print(i)