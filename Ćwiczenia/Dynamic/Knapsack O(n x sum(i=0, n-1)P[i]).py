# Proszę przedstawić algorytm problemu knapsack działający w czasie O(n*sum(i=0, n-1)P[i])
'''
T(i,j) - najmniejsza waga przedmiotów do i włącznie dla zadanego profitu >= j
T(0,j) = W[0]
T(i,j) = min( T(i - 1, j), T(i - 1, j - values[i]) + weights[i] )
                                    if j - values[i] >= 0
'''
from math import inf


def knapsack_problem(weights, values, max_W):
    n = len(weights)
    sum_val = sum(values)
    T = [[inf] * (sum_val + 1) for _ in range(n)]
    for x in range(values[0] + 1):
        T[0][x] = weights[0]
    for i in range(1, n):
        for j in range(sum_val):
            if j - values[i] > -1:
                T[i][j] = min(T[i - 1][j], T[i - 1][j - values[i]] + weights[i])
            else:
                T[i][j] = T[i - 1][j]
    for i in range(sum_val, -1, -1):
        if T[-1][i] <= max_W:
            return i


values = [10, 8, 4, 5, 3, 7]
weights = [4, 5, 12, 9, 1, 13]
max_W = 24
print(knapsack_problem(weights, values, max_W))
