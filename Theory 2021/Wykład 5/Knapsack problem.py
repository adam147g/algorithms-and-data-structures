# We are given weights and values of n items and maximum capacity. We have find out
# the maximum value of items such that the sum of the weights of that items is
# smaller or equal to total capcity of "knapsack."

# O(n*MaxW)
# 1st solution:


def knapsack(W, P, max_W):
    F = [[0] * (max_W + 1) for _ in range(len(W))]
    for w in range(W[0], max_W + 1):
        F[0][w] = P[0]
    for i in range(1, len(W)):
        for w in range(1, max_W + 1):
            F[i][w] = F[i - 1][w]  # gdy nie biore danego przedmiotu
            if w >= W[i]:  # gdy biorę dany przedmiot
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
    return F[len(P) - 1][max_W]


def getsolution(F, W, P, i, w):
    if i < 0: return []
    if i == 0:
        if w >= W[0]: return [0]
        return []
    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return getsolution(F, W, P, i - 1, w - W[i]) + [i]
    else:
        return getsolution(F, W, P, i - 1, w)


# 2nd solution: using memoization


def memoized_knapsack(W, P, max_W, n, F):
    if n == 0 or max_W == 0:
        return 0
    if F[n][max_W] != -1:
        return F[n][max_W]
    if W[n - 1] <= max_W:
        F[n][max_W] = max(P[n - 1] + memoized_knapsack(W, P, max_W - W[n - 1], n - 1, F),
                          memoized_knapsack(W, P, max_W, n - 1, F))
        return F[n][max_W]
    elif W[n - 1] > max_W:
        F[n][max_W] = memoized_knapsack(W, P, max_W, n - 1, F)
        return F[n][max_W]


P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
max_W = 24
print(knapsack(W, P, max_W))
F = [[-1] * (max_W + 1) for _ in range(len(P) + 1)]
print(memoized_knapsack(W, P, max_W, len(P), F))
