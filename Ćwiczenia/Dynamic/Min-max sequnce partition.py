# Mając ciąg A, znaleźć taki podział ciądu na k podciągów,
# aby najmniejsza wartość spośród kawałków była jak największa


from math import inf


def printing(T):
    for x in T:
        print(x)
    print()


def f(A, k, F, i, j):
    if F[i][j] != 0:
        return F[i][j]
    if i == 0 or j > i + 1:
        return 0
    if i + 1 == j:
        F[i][j] = max(f(A, k, F, i - 1, j - 1), A[i])
        return F[i][j]
    if j == 1:
        F[i][j] = f(A, k, F, i - 1, j) + A[i]
        return F[i][j]

    for x in range(i):
        F[i][j] = max(F[i][j], min(f(A, k, F, x, j - 1), sum(A[x + 1:i + 1])))
    return F[i][j]


def minmax(A, k):
    F = [[0] * (k + 1) for _ in range(len(A))]
    F[0][1] = A[0]
    return f(A, k, F, len(A) - 1, k)


A = [60, 10, 20, 15, 10, 5, 40, 10]
k = 3
print(minmax(A, k))
