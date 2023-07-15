# Dany jest ciąg macierzy A1, A2, ..., An. Znajdź koszt mnożenia macierzy przy
# optymalnym doborze kolejności mnożenia (nawiasowania macierzy). Macierze nie są
# koniecznie kwadratowe (ale znamy ich rozmiary).

from math import inf



def matrixChainMemoised(p, i, j, DP):
    if i == j:
        return 0
    if DP[i][j] != inf:
        return DP[i][j]
    for k in range(i, j):
        DP[i][j] = min(DP[i][j],
                       matrixChainMemoised(p, i, k, DP) + matrixChainMemoised(p, k + 1, j, DP) + p[i - 1] * p[k] * p[j])
#                           po lewej                    +           po prawej                  +         mnożenie
    return DP[i][j]


def MatrixChainOrder(p, n):
    DP = [[inf] * n for _ in range(n)]
    return matrixChainMemoised(p, 1, n-1, DP)


'2 mniej zrozumiały sposób'

def matrix_chain_order(T):
    n = len(T)
    m = [[inf for _ in range(n)] for _ in range(n)]
    for x in range(1, n):                   # nie moę mnożyć samej siebie ze sobą
        m[x][x] = 0
    for L in range(2, n):                   # wypełnianie prawej górnej częśći
        end = n - L + 1                     # ograniczenie dla i odd dołu
        for i in range(1, end):
            j = i + L - 1                   # ograniczenie dla k od prawej
            for k in range(i, j):           # sprawdzanie możliwości
                q = m[i][k] + m[k + 1][j] + (T[i - 1] * T[k] * T[j])
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n - 1]


T = [30, 35, 15, 5, 10, 20, 25]
print(matrix_chain_order(T))
print(MatrixChainOrder(T, len(T)))
