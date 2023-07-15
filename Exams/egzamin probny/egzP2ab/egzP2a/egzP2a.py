from egzP2atesty import runtests


def partition(T, swap, p, r):
    pivot = T[swap[r]][1]
    i = p - 1
    for j in range(p, r):
        if T[swap[j]][1] >= pivot:
            i += 1
            T[swap[j]], T[swap[i]] = T[swap[i]], T[swap[j]]
    T[swap[i + 1]], T[swap[r]] = T[swap[r]], T[swap[i + 1]]
    return i + 1


def select(T, swap, p, r, x):
    if p < r:
        q = partition(T, swap, p, r)
        if q < x:
            return select(T, swap, q + 1, r, x)
        elif q > x:
            return select(T, swap, p, q - 1, x)


def zdjecie(T, m, k):
    n = len(T)
    START = [0] * m
    END = [0] * m

    curr_end = -1
    curr_width = k + m - 1
    for i in range(m):
        START[i] = curr_end + 1
        curr_end += curr_width
        END[i] = curr_end
        curr_width -= 1

    swap = [0] * n
    idx = 0
    col, row = 0, 0
    while idx < n:
        if START[row] + col <= END[row]:
            swap[START[row] + col] = idx
            idx += 1
        row += 1
        if row >= m:
            row = 0
            col += 1

    last = END[m - 1]
    for x in range(m - 2, -1, -1):
        select(T, swap, 0, last, END[x])
        last = END[x] - 1

    return None


runtests(zdjecie, all_tests=False)
