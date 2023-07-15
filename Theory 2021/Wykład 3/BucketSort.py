from time import perf_counter
from random import random


def insertion_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return T

# tyle kubełków, co rozmiar tablicy

' DLA ROZKŁADU JEDNOSTAJNEGO ELEMENTÓW TABLICY!!! '
# dla n = 10
# O(n)
def bucket_sort(T):
    n = len(T)
    bucket = [[] for _ in range(n)]
    for i in T:
        index = int(n*i)
        bucket[index].append(i)
    for i in range(n):
        bucket[i] = insertion_sort(bucket[i])
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            T[k] = bucket[i][j]
            k += 1
    return T


T = [random() for _ in range(10)]
start = perf_counter()
print(bucket_sort(T))
end = perf_counter()
print(end-start)