# Tablica wag zajęć i terminów do ich zrobienia
# jakie zajęcia należy wybrać aby waga była największa?

def partition(A, B, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]  # swap(A[i],A[j])
            B[i], B[j] = B[j], B[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    B[i + 1], B[r] = B[r], B[i + 1]
    return i + 1

def QuickSort(A, B, p, r):
    while p < r:
        q = partition(A, B, p, r)
        QuickSort(A, B, p, q - 1)
        p = q + 1



def maxProfit(P, D, times):
    n = len(P)
    QuickSort(P, D, 0, n-1)             # sortuję malejąco
    T = [-1 for _ in range(times+1)]
    for i in range(n):
        tmp = D[i]
        while T[tmp] != -1 and tmp >- 1:
            tmp -= 1
        if tmp != -1:
            T[tmp] = P[i]

    res = 0
    for i in T:
        if i != -1:
            res += i

    return res

P = [8, 7, 5, 4, 4, 3]
D = [1, 3, 4, 4, 3, 2]
times = 4
print(maxProfit(P, D, times))