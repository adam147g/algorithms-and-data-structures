from egzP1atesty import runtests


def f(DP, new_string, new_d_tab, idx):
    if DP[idx] != float('inf'):
        return DP[idx]
    res = float('inf')
    for k in new_d_tab:
        if new_string[idx - k[1] + 1:idx + 1] == k[0]:
            if idx - k[1] > -1:
                if f(DP, new_string, new_d_tab, idx - k[1]) + 1 < res:
                    res = f(DP, new_string, new_d_tab, idx - k[1]) + 1
            elif idx - k[1] == -1:
                DP[idx] = 1
                return 1
    DP[idx] = res

    return DP[idx]


def titanic(W, M, D):
    new_string = ''
    for x in W:
        new_string += M[ord(x) - ord('A')][1]

    new_d_tab = [[M[i][1], len(M[i][1])] for i in D]

    # print(W[0:1]) - 1 litera

    DP = [float('inf') for _ in range(len(new_string))]
    f(DP, new_string, new_d_tab, len(new_string) - 1)
    # print(DP)
    return DP[-1]


runtests(titanic, recursion=True)
