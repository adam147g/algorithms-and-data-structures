# Ile jest w liście wejściowej słów składających się z takiej samej ilości takich samych liter?

from kol1btesty import runtests


def counting_sort(A, k, idx):
    C = [0] * k
    B = [0] * len(A)
    for i in range(len(A)):
        C[A[i][idx]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        C[A[i][idx]] -= 1
        B[C[A[i][idx]]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]


def f(T):
    n = len(T)
    size = (ord('z') - ord('a') + 1)
    new_T = [[0] * size for _ in range(n)]
    max_ = [0] * size
    for i in range(n):
        for s in T[i]:
            new_T[i][ord(s) - ord('a')] += 1
            max_[ord(s) - ord('a')] = max(max_[ord(s) - ord('a')], new_T[i][ord(s) - ord('a')])
    # radix_sort
    idx = size - 1
    while idx > -1:
        if max_[idx]:
            counting_sort(new_T, max_[idx] + 1, idx)
        idx -= 1
    result = 1
    curr_idx = 0
    curr = 1
    for k in range(1, n):
        if new_T[k] == new_T[curr_idx]:
            curr += 1
        else:
            if curr > result:
                result = curr
            curr = 1
            curr_idx = k
    if curr > result:
        result = curr
    return result


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(f, all_tests=True)
