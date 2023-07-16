def MetodaChio(T):
    n = len(T)
    if n == 2:
        return T[0][0] * T[1][1] - T[0][1] * T[1][0]
    mini_matrix = [[1 for _ in range(n - 1)] for _ in range(n - 1)]
    for i in range(1, n):
        for j in range(1, n):
            mini_matrix[i - 1][j - 1] = T[0][0] * T[i][j] - T[0][j] * T[i][0]
    return 1 / (T[0][0] ** (n - 2)) * MetodaChio(mini_matrix)


T = [
    [5,1,1,2,3],
    [4,2,1,7,3],
    [2,1,2,4,7],
    [9,1,0,7,0],
    [1,4,7,2,2]
]
print(MetodaChio(T))
