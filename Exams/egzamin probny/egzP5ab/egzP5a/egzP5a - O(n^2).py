from egzP5atesty import runtests


def f(i, j, DP, T):
    if DP[i][j] != -1:
        return DP[i][j]
    if i == j:
        DP[i][j] = T[i]
    else:
        DP[i][j] = min(T[j], f(i, j - 1, DP, T))
    return DP[i][j]


def inwestor(T):
    n = len(T)
    DP = [[-1 for _ in range(n)] for _ in range(n)]
    result = 0
    for i in range(n):
        f(i, n - 1, DP, T)
        for j in range(i, n):
            result = max(result, (j - i + 1) * DP[i][j])
    return result


runtests(inwestor, all_tests=True)
