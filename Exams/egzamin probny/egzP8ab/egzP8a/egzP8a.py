from egzP8atesty import runtests
from bisect import bisect_right


def bin_search(T, x):
    lo, hi = 0, len(T)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if T[mid][0] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def reklamy(T, S, o):
    n = len(T)
    P = [(T[i][0], T[i][1], S[i]) for i in range(n)]
    P.sort(key=lambda x: x[0])
    result = 0
    DP = [0 for _ in range(n)]
    DP[n - 1] = P[n - 1][2]

    for i in range(n - 2, -1, -1):
        if DP[i + 1] > P[i][2]:
            DP[i] = DP[i + 1]
        else:
            DP[i] = P[i][2]

    for i in range(n):
        end = P[i][1]
        idx = bin_search(P, end)
        second_company = 0
        if idx < n and S[idx] != end:
            second_company = DP[idx]
        if P[i][2] + second_company > result:
            result = P[i][2] + second_company

    return result


runtests(reklamy, all_tests=True)
