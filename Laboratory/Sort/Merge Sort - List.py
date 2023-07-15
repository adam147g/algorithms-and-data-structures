from random import randint, seed
from math import inf


def mergesort(T, p=0, r=None):
    if r is None:
        r = len(T) - 1
    if p < r:
        m = (p + r) // 2
        mergesort(T, p, m)
        mergesort(T, m + 1, r)
        merge(T, p, m, r)
    return T


def merge(T, p, q, r):
    L = T[p:q + 1]
    R = T[q + 1:r + 1]
    L.append(inf)
    R.append(inf)
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


#seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        break
else:
    print("OK")
