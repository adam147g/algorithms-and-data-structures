# Proszę zaimplementować Quick Sort iteracyjnie.
from random import randint, seed


def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def iterative_quicksort(T):
    S = []
    p = 0
    r = len(T) - 1
    S.append(p)
    S.append(r)
    # S.append((p,r))
    while len(S) > 0:
        r = S.pop()
        p = S.pop()
        # (p,r) = S.pop
        q = partition(T, p, r)
        if q - 1 > p:
            S.append(p)
            S.append(q - 1)
        if q + 1 < r:
            S.append(q + 1)
            S.append(r)


seed(50)
n = 11
T = [randint(0, 20) for _ in range(n)]
print(T)
print()
iterative_quicksort(T)
print()
print(T)

'''
O(logn) - pamięci dodatkowej

def iterative_quicksort(T):
    S=[]
    p = 0
    r = len(T) - 1
    S.append(p)
    S.append(r)
    while len(S)>0:
        r = S.pop()
        p = S.pop()
        if p<r:
            q = partition(T, p ,r)
            if q-p>r-q:     #lewa jest większa od prawej
                S.append(p)
                S.append(q-1)
                S.append(q+1)
                S.append(r)
            else:
                S.append(q+1)
                S.append(r)
                S.append(p)
                S.append(q-1)
'''
