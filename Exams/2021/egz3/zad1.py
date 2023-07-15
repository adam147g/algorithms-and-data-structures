# NIE MAM POJĘCIA CZEMU TEST NR 3 NIE DZIAŁA, IMO JEST DOBRZE
# O(n^2)
from zad1testy import runtests


def printlist(A, P, i, res):
    res.append(A[i])
    if P[i] != -1:
        printlist(A, P, P[i], res)
    return res


def find_max(A, B):
    n = len(A)
    F = [0] * n
    L = [0] * n
    P = [0] * n
    F[n - 1] = B[n - 1]
    for i in range(n):
        for j in range(n - 1, i, -1):
            if A[i] + B[j] > F[i]:
                F[i] = A[i] + B[j]
                L[i] = i
                P[i] = j
    idx_l = 0
    idx_r = 0
    best = F[0]
    for i in range(1, n):
        if F[i] > best:
            best = F[i]
            idx_l = L[i]
            idx_r = P[i]
    if A[n - 1] >= best:
        return n - 1, None
    if B[0] >= best:
        return None, 0
    return idx_l, idx_r


def mr(A):
    n = len(A)
    malejace_do_i = [1] * n
    malejace_parenty = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] > A[i] and malejace_do_i[j] + 1 > malejace_do_i[i]:
                malejace_do_i[i] = malejace_do_i[j] + 1
                malejace_parenty[i] = j

    rosnace_od_i = [1] * n
    rosnace_parenty = [-1] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if A[j] > A[i] and rosnace_od_i[j] + 1 > rosnace_od_i[i]:
                rosnace_od_i[i] = rosnace_od_i[j] + 1
                rosnace_parenty[i] = j

    res_ros = []
    res_mal = []
    idx = find_max(malejace_do_i, rosnace_od_i)
    if idx[0] is not None:
        res_mal = printlist(A, malejace_parenty, idx[0], [])
        res_mal.reverse()

    if idx[1] is not None:
        res_ros = printlist(A, rosnace_parenty, idx[1], [])
    if len(res_ros) != 0 and len(res_mal) != 0 and res_mal[len(res_mal) - 1] == res_ros[0]:
        res_mal.pop()
    '''
    print("-----------------")
    print(A)
    print("-----------------")
    print(res_mal + res_ros)
    print("-----------------")
    '''
    return res_mal + res_ros


'''
A = [4, 10, 5, 1, 1000, 1, 8, 2, 3, 4, 0, 0]
A.sort()
print(mr(A))
print(zad([4,10,5,1,1,8,2,3,4]))
'''
runtests(mr)
