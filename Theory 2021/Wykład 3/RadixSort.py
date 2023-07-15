from time import perf_counter
from random import randint, seed

seed(100)


def counting_sort(T, k):
    C = [0] * len(T)
    B = [0] * 10
    for i in range(len(T)):
        index = int((T[i] / k) % 10)
        B[index] += 1
    for i in range(1, 10):
        B[i] += B[i - 1]
    j = len(T) - 1
    while j >= 0:
        index = int((T[j] / k) % 10)
        C[B[index] - 1] = T[j]
        B[index] -= 1
        j -= 1
    for i in range(len(T)):
        T[i] = C[i]


# sortowanie pozycyjne - dla liczb typu 110, 117, 190, 196 - od tyłu je sortuje
# 523     472     523     266
# 266     523     349     349
# 783 --> 783 --> 266 --> 472
# 472     266     472     523
# 349     349     783     783


def radix_sort(T):
    maximum = 0
    for i in range(len(T)):
        maximum = max(maximum, T[i])  # trzeba znaleźć największą liczbę
    i = 1
    while maximum // i > 0:
        counting_sort(T, i)
        i *= 10


T = [randint(1, 100) for _ in range(20)]
start = perf_counter()
radix_sort(T)
print(T)
end = perf_counter()
print("Czas - ", end - start)
print()
Tablica_z_przykladu = [523, 266, 783, 472, 349, 2]
print(Tablica_z_przykladu)
print()
radix_sort(Tablica_z_przykladu)
print(Tablica_z_przykladu)
