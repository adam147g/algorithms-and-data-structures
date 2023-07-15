from egzP6atesty import runtests

'''
Złożoność wzorcowa, ale można też powrzucać po długościach do kubełków
i zrobić selecta tylko w kubełku z odpowiednią długością hasła
'''


def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j][0] <= pivot[0]:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def select(T, p, r, x):
    if p == r:
        return T[p][1]
    q = partition(T, p, r)
    if x == q:
        return T[x][1]
    elif x < q:
        return select(T, p, q - 1, x)
    else:
        return select(T, q + 1, r, x)

def google(H, s):
    # print(H)

    T = []
    for i in range(len(H)):
        letters = 0
        lenght = 0
        for x in H[i]:
            lenght += 1
            if ord('z') >= ord(x) >= ord('a'):
                letters += 1
        T.append([-lenght, -letters, i])

    select(T, 0, len(H) - 1, s - 1)
    repair = []
    less_than = 0
    pivot = T[s - 1]
    for i in range(len(T)):
        if T[i][0] < pivot[0]:
            less_than += 1
        elif T[i][0] == pivot[0]:
            repair.append([T[i][1], T[i][2]])

    return H[select(repair, 0, len(repair) - 1, s - less_than - 1)]


runtests(google, all_tests=True)
