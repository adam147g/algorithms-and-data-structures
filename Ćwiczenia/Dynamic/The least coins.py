# Problem wydania danej kwoty w jak najmniejszej liczbie nominałów


# f(i) - min liczba monet do wydania i
# f(0) = 0
# f(i) = min    f(i-m_j)+1
#       dla j - należącego {1, ..., n}

from math import inf

def coins(x, M):
    T = [inf for _ in range(x + 1)]  # nie osiągniemy tej liczby
    T[0] = 0
    for y in range(x + 1):
        for m in M:
            if y >= m and T[y - m] + 1 < T[y]:
                T[y] = T[y - m] + 1
    return T[x]


M = [10,3,5,2]
x = 11
print(coins(x, M))
