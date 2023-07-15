from zad1ktesty import runtests


def ssp1(T):
    n = len(T)
    result = 0
    partial = 0
    for i in range(n):
        partial += T[i]
        partial = max(0, partial)
        result = max(partial, result)
    return result


def roznica(S):
    print(S)
    n = len(S)
    F = []
    i = 0
    while i < n:
        sum = 0
        if S[i] == '0':
            while i < n and S[i] == '0':
                sum += 1
                i += 1
            F.append(sum)
        else:
            while i < n and S[i] == '1':
                sum -= 1
                i += 1
            F.append(sum)
    if len(F) == 1 and F[0] < 0:
        return -1
    return ssp1(F)


runtests(roznica)

'''

def roznica(S):
    S = str(S)
    n = len(S)
    F = [[-1 for _ in range(n)] for _ in range(n)]

    for s in range(n):
        one = 0
        zero = 0
        for e in range(s + 1, n):
            if int(S[e]) % 2 == 1:
                one += 1
            else:
                zero += 1
            F[s][e] = max(F[s][e - 1], zero - one)

    maxi = -1
    for i in range(n):
        maxi = max(maxi, F[i][n - 1])

    return maxi


runtests(roznica)
'''
