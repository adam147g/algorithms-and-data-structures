'''
Adam Górka
Algorytm polega na znalezieniu najmniejszego początku oraz największego końca przedziałów.
Następnie program tworzy odpowiednią liczbę kubełków, do których wrzuca wartości z listy T.
Po takim przejściu program sortuje każdy z kubełków, po czym wypełnia tablicę T wartościami
z koljnych ubełków, już posortowanych.
Algorytm jest poprawny oraz szybki, ponieważ dane pochodzą z rozkładu jednostajnego,
który jest szybko sortowany za pomocą BucketSort'a
'''
from zad3testy import runtests


def QuickSort(T, idx, p, r):
    if p < r:
        T[idx][(p + r) // 2], T[idx][p] = T[idx][p], T[idx][(p + r) // 2]
        pivot = T[idx][p]
        i = p - 1
        j = r + 1
        while True:
            i += 1
            while T[idx][i] < pivot:
                i += 1
            j -= 1
            while T[idx][j] > pivot:
                j -= 1
            if i >= j:
                q = j
                break
            T[idx][i], T[idx][j] = T[idx][j], T[idx][i]
        QuickSort(T, idx, p, q)
        QuickSort(T, idx, q + 1, r)


def BucketSort(T, idx):
    n = len(T[idx])
    max_ = -1
    min_ = -1
    if n > 2:
        min_ = min(T[idx])
        max_ = max(T[idx])
    if n > 2 and max_ != min_:
        bucket = [[] for _ in range(n + 1)]
        divide = (max_ - min_) / n
        for x in T[idx]:
            bucket[int((x - min_) / divide)].append(x)

        for i in range(n):
            bucket_len = len(bucket[i])
            if bucket_len < 2:
                continue
            if bucket_len == 2:
                if bucket[i][0] < bucket[i][1]:
                    continue
                bucket[i][0], bucket[i][1] = bucket[i][1], bucket[i][0]
            else:
                QuickSort(bucket, i, 0, bucket_len - 1)
        k = 0
        for i in range(n + 1):
            for j in range(len(bucket[i])):
                T[idx][k] = bucket[i][j]
                k += 1
    elif n == 2 and T[idx][0] > T[idx][1]:
        T[idx][0], T[idx][1] = T[idx][1], T[idx][0]

    return T


def SortTab(T, P):
    min_ = min(P, key=lambda x: x[0])[0]
    max_ = max(P, key=lambda x: x[1])[1]
    bucket = [[] for _ in range(max_ - min_)]
    for x in T:
        bucket[int(x - min_)].append(x)
    for idx in range(max_ - min_):
        BucketSort(bucket, idx)
    k = 0
    for i in range(max_ - min_):
        for j in range(len(bucket[i])):
            T[k] = bucket[i][j]
            k += 1
    return T


runtests(SortTab)
