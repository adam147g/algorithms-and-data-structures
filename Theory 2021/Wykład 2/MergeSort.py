# O(n logn)
from math import inf
def merge(T1, T2):
    res = []
    i = 0
    j = 0
    while i < len(T1) and j < len(T2):
        if T1[i] <= T2[j]:
            res.append(T1[i])
            i += 1
        else:
            res.append(T2[j])
            j += 1

    if i < len(T1):
        while i < len(T1):
            res.append(T1[i])
            i += 1

    if j < len(T2):
        while j < len(T2):
            res.append(T2[j])
            j += 1
    return res


def mergesort(T):
    if len(T) < 2:
        return T
    n = len(T) // 2
    left = mergesort(T[0:n])
    right = mergesort(T[n:len(T)])

    return merge(left, right)

#   A = merge(left, right)
#   return A                    - to samo


T = [12, 15, 68468, 0, 565, 48, 13, 1, 7, 91, 44, 3]

print(mergesort(T))

def merge_(T, p, q, r):
    L = T[p:q+1]
    R = T[q+1:r+1]
    L.append(inf)
    R.append(inf)
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


def merge_sort(T, p, r):
    if len(T) <= 1:
        return T
    elif p < r:
        m = (p+r) // 2
        merge_sort(T, p, m)
        merge_sort(T, m+1, r)
        merge_(T, p, m, r)
