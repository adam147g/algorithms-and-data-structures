# Mamy zbiór przedziałów, chcemy sprawdzić, czy da się je skleić
# aby utworzyć zadany przedział

a = 0  # początek przedziałów
b = 9  # koniec przedziałów

F = [[None] * (b - a + 1) for _ in range(b - a + 1)]
S = [(0, 3), (1, 5), (3, 7), (5, 7), (7, 9)]


def intervals(i, j, F, S):
    if F[i][j] is not None:
        return F[i][j]

    if (i, j) in S:
        F[i][j] = True
        return F[i][j]

    q = False
    for k in range(i + 1, j):
        q = (intervals(i, k, F, S) and intervals(k, j, F, S))
        if q:
            break

    F[i][j] = q
    return F[i][j]


print(intervals(1, 5, F, S))
print(intervals(1, 9, F, S))
print(intervals(0, 5, F, S))
