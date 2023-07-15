from zad3testy import runtests

def QuickSort(T, p, r):
    if p < r:
        T[(p + r) // 2], T[p] = T[p], T[(p + r) // 2]
        pivot = T[p]
        i = p - 1
        j = r + 1
        while True:
            i += 1
            while T[i] < pivot:
                i += 1
            j -= 1
            while T[j] > pivot:
                j -= 1
            if i >= j:
                q = j
                break
            T[i], T[j] = T[j], T[i]
        QuickSort(T, p, q)
        QuickSort(T, q + 1, r)


def BucketSort(T):
    n = len(T)
    max_ = -1
    min_ = -1
    if n > 2:
        min_ = min(T)
        max_ = max(T)
    if n > 2 and max_ != min_:
        bucket = [[] for _ in range(n)]
        for x in T:
            if x == max_:
                bucket[int((x - min_) / (max_ - min_) / n) - 1].append(x)
            else:
                bucket[int((x - min_) / (max_ - min_) / n)].append(x)
        for b in bucket:
            bucket_len = len(b)
            if bucket_len < 2:
                continue
            if bucket_len == 2:
                if b[0] < b[1]:
                    continue
                b[0], b[1] = b[1], b[0]
            else:
                QuickSort(b, 0, bucket_len - 1)
        k = 0
        for i in range(n):
            for j in range(len(bucket[i])):
                T[k] = bucket[i][j]
                k += 1
    elif n == 2 and T[0] > T[1]:
        T[0], T[1] = T[1], T[0]

    return T


def SortTab(T, P):
    min_ = min(P, key=lambda x: x[0])[0]
    max_ = max(P, key=lambda x: x[1])[1]
    bucket = [[] for _ in range(max_ - min_)]
    for x in T:
        bucket[int(x - min_)].append(x)
    for b in bucket:
        BucketSort(b)
    k = 0
    for i in range(max_ - min_):
        for j in range(len(bucket[i])):
            T[k] = bucket[i][j]
            k += 1
    return T


runtests(SortTab)
# T = [ 1.2, 1.5, 1.1, 1.02, 3.7, 4.5, 2.5, 3.5, 7.8]
# T = [0.42,0.13,0.07,0.210,0.91,0.130,0.37]
# P = [(1, 5, 0.75), (4, 8, 0.25)]
# print(SortTab(T, P))
