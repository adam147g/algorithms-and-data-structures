# Sortowanie tablicy n liczb ze zbioru {0, 1, ..., n^2 - 1}
# zamieniamy liczby 0 - n^2-1 na  takie w systemie n-kowym
# wtedy długość ich będzie wynosiła 2 w tym systemie

from random import randint


def sort_n_square(T):
    n = len(T)
    B = [0] * n
    C = [0] * n
    for i in range(n):
        C[T[i] % n] += 1
    for i in range(1, n):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[T[i] % n] -= 1
        B[C[T[i] % n]] = T[i]
    print(B)

    C = [0] * n
    D = [0] * n
    for i in range(n):
        C[B[i] // n] += 1
    for i in range(1, n):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[B[i] // n] -= 1
        D[C[B[i] // n]] = B[i]
    for i in range(n):
        T[i] = D[i]
    return T


n = 10
T = [randint(0, n**2 - 1) for _ in range(n)]
print(T)
A = sort_n_square(T)
print(A)
print()

n = 8
T = [randint(0, n**2 - 1) for _ in range(n)]
print(T)
A = sort_n_square(T)
print(A)