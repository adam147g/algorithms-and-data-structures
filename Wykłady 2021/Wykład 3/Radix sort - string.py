from random import randint


def counting_sort(A, idx, max_len):
    k = ord('z') - ord('a') + 2
    C = [0] * k
    B = [0] * len(A)
    for i in range(len(A)):
        if len(A[i]) <= max_len - idx:
            C[0] += 1
        else:
            C[ord(A[i][max_len - idx]) - ord('a') + 1] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        if len(A[i]) <= max_len - idx:
            C[0] -= 1
            B[C[0]] = A[i]
        else:
            C[ord(A[i][max_len - idx]) - ord('a') + 1] -= 1
            B[C[ord(A[i][max_len - idx]) - ord('a') + 1]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]


def radix_sort(T):
    max_len = 0
    for string in T:
        max_len = max(max_len, len(string))
    idx = 1
    while idx <= max_len:
        counting_sort(T, idx, max_len)
        idx += 1
    return T


def rand_str():
    n = randint(1, 15)
    str = ''
    for i in range(n):
        str += chr(randint(ord('a'), ord('z')))
    return str


T = [rand_str() for _ in range(30)]
T += ['aaa', 'baaah', 'baa', 'baaaha', 'aa', 'aaaa']
print(radix_sort(T))
