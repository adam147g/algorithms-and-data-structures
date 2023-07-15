from time import perf_counter
from random import randint, seed
seed(100)

# Znaleźć elment, który po posortowaniu tablicy znalazłby się na pozycji k-tej

# O(n)

def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def select(T, p, r, x):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if x == q:
        return T[x]
    elif x < q:
        return select(T, p, q-1, x)
    else:
        return select(T, q+1, r, x)


T = [randint(1, 1000) for _ in range(1000)]
start = perf_counter()
print(select(T, 0, len(T)-1, 256))
end = perf_counter()
print(end-start)