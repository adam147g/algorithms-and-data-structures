from zad6ktesty import runtests


def haslo(S):
    print(S)
    n = len(S)
    if n == 0: return 1
    for i in range(1, n):
        if S[i] == S[i - 1] == '0':
            return 0
    F = [0] * n
    F[0] = 1
    if int(S[0]) * 10 + int(S[1]) <= 26 and S[0] != '0':
        F[1] = 2
    else:
        F[1] = 1
    for i in range(2, n):
        if S[i] != '0':
            F[i] += F[i - 1]
        if S[i - 1] != '0' and int(S[i - 1]) * 10 + int(S[i]) <= 26:
            F[i] += F[i - 2]
    return F[-1]


runtests(haslo)
