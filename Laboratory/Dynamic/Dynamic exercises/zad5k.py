from zad5ktesty import runtests
from math import inf

'''
# F(i, j) represents the maximum value the user
# can collect from i'th coin to j'th coin.
#
# F(i, j) = Max(Vi + min(F(i+2, j), F(i+1, j-1) ),
#               Vj + min(F(i+1, j-1), F(i, j-2) ))
# As user wants to maximise the number of coins.
#
# Base Cases
#     F(i, j) = Vi           If j == i
#     F(i, j) = max(Vi, Vj)  If j == i + 1

def garek(arr):
    n = len(arr)
    # Create a table to store
    # solutions of subproblems
    table = [[0] * n for _ in range(n)]
    # Fill table using above recursive
    # formula. Note that the table is
    # filled in diagonal fashion
    # from diagonal elements to
    # table[0][n-1] which is the result.
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            x = 0
            if ((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if ((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if (i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
    return table[0][n - 1]

'''


# f(i, j) - zwraca tuplę (x, y), gdzie x to maksymalny zysk z gry w przedziale i, j
#                                    a y to maksymalny zysk z gry po moim ruchu
#
#             / f(T, F, i + 1, j)[1] + T[i], f(T, F, i + 1, j)[0]
#            /  gdy  f(T, F, i + 1, j)[1] + T[i] > f(T, F, i, j - 1)[1] + T[j]
# f(i, j) = <
#            \  f(T, F, i, j - 1)[1] + T[i], f(T, F, i, j - 1)[0]
#             \ w p.p.
#


def f(T, F, i, j):
    if F[i][j] != (-inf, -inf):
        return F[i][j]
    if i < 0 or j < 0:
        return -inf, -inf
    take_left = f(T, F, i + 1, j)
    take_right = f(T, F, i, j - 1)
    if T[i] + take_left[1] > T[j] + take_right[1]:
        F[i][j] = take_left[1] + T[i], take_left[0]
    else:
        F[i][j] = take_right[1] + T[j], take_right[0]
    return F[i][j]


def garek(arr):
    n = len(arr)
    F = [[(-inf, -inf)] * n for _ in range(n)]
    for i in range(n - 1):
        F[i][i] = arr[i], 0
        if arr[i + 1] > arr[i]:
            F[i][i + 1] = (arr[i + 1], arr[i])
        else:
            F[i][i + 1] = (arr[i], arr[i + 1])

    F[n - 1][n - 1] = arr[n - 1], 0
    return f(arr, F, 0, n - 1)[0]


runtests(garek)
