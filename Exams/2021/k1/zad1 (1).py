from Exercise_1_tests import runtests
def setBorder(tab, start, pivot, n):
    border = start

    for i in range(start, pivot):
        if tab[i//n][i % n] < tab[pivot//n][pivot % n]:
            tab[border//n][border % n], tab[i//n][i % n] = tab[i//n][i % n], tab[border // n][border % n]
            border += 1
    tab[border // n][border % n], tab[pivot//n][pivot % n] = tab[pivot//n][pivot % n], tab[border // n][border % n]
    return border

def quickSort(tab, start, end, n):
    while start < end:
        border = setBorder(tab, start, end, n)
        quickSort(tab, start, border - 1, n)
        start = border + 1

def Median(T):
    n = len(T)
    quickSort(T, 0, n * n - 1, n)

    toReturn = []
    interval = int((n * n - n) / 2)
    left_id = 0
    middle_id = interval
    right_id = interval + n

    for i in range(n):
        tab = []
        for j in range(n):
            if i > j:
                tab.append(T[left_id // n][left_id % n])
                left_id += 1
            elif i == j:
                tab.append(T[middle_id // n][middle_id % n])
                middle_id += 1
            else:
                tab.append(T[right_id // n][right_id % n])
                right_id += 1

        toReturn.append(tab)
    for i in range(len(T)):
        for j in range(len(T)):
            T[i][j] = toReturn[i][j]
    return T


runtests(Median)