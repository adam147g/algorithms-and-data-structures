# Proszę napisać funkcję znajdującą minimum i maksimum
# w tablicy o długości n, wykonując a 3/2n + c porównań.

# p_inf =  1000
# n_inf = -1000


def minmax(T):
    length = len(T)
    minimal = T[length - 1]     # T[length - 1] to to samo, co T[-1]
    # minimal = p_inf
    maximal = T[length - 1]
    # maximal = n_inf

    for i in range(0, length - 1, 2):
        if T[i] < T[i + 1]:
            if T[i] < minimal:
                minimal = T[i]
            if T[i + 1] > maximal:
                maximal = T[i + 1]
        else:
            if T[i] > maximal:
                maximal = T[i]
            if T[i + 1] < minimal:
                minimal = T[i + 1]
    return maximal, minimal


T = [36, 665, 11, 23, 2, 700, 21]
print(minmax(T))
