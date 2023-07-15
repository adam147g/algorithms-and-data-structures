from zad2ktesty import runtests

'''
from math import ceil
Nie działa dla 'dhdhrrawarrawarrhdhd'
O(n)
 
def palindrom(S):
    print(S)
    n = len(S)
    if n == 1:
        return S[0]
    if n == 2:
        if S[0] == S[1]:
            return S[0] + S[1]
        return S[0]
    F = [1] * n
    for i in range(1, n):
        if S[i] == S[i - 2] and i - 2 > -1:
            F[i] = 3
        elif S[i] == S[i - 1]:
            F[i] = 2
        if F[i - 1] % 2 == 1 and i - ceil(F[i - 1] / 2) * 2 > -1 and S[i - ceil(F[i - 1] / 2) * 2] == S[i]:
            F[i] = max(F[i], F[i - 1] + 2)
        elif F[i - 1] % 2 == 0 and i - F[i - 1] - 1 > -1 and S[i - F[i - 1] - 1] == S[i]:
            F[i] = max(F[i], F[i - 1] + 2)

    best = (1, 0)
    for i in range(1, n):
        if F[i] > best[0]:
            best = (F[i], i)
    i = best[1]
    string = ''
    while i > -1 and i > best[1] - best[0]:
        string += S[i]
        i -= 1
    return string


# runtests(palindrom)
'''


def if_pali(string):
    if string[::-1] == string:
        return True
    return False


def palindrom(S):
    n = len(S)
    if if_pali(S):
        return S
    DP = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        DP[i][i] = 1
    maxi = idx = 0
    for s in range(n):
        for e in range(s + 1, n):
            if if_pali(S[s: e]) and DP[s][e - 1] < e - s:  # e-s to len(S[s: e])
                DP[s][e] = e - s
            else:
                DP[s][e] = DP[s][e - 1]

            if DP[s][e] > maxi:
                maxi = DP[s][e]
                idx = s

    return S[idx:idx + maxi]


runtests(palindrom)
