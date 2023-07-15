from zad1testy import runtests

'''
Martyna Olszewska
Tworzymy dwie pomocnicze tablice (inc i dec), w jednej przechowujemy pod indeksem i najdłuższy podciąg malejący kończący się w X[i],
a w drugiej przechowujemy najdłuższy podciąg rosnący zaczynający się w X[i].
Następnie wybieramy max z tablcy inc, dec,  lub inc[i] + dec[i] - 1 i jest to długość najdłuższego ciągu typu MR.
złożoność czasowa n^2.
Algorytm może działać szybciej jeśli użyjemy wyszukiwania binarnego, wtedy O(nlogn).
'''


def printsolution(A, P, i, res):
    if P[i] != -1:
        printsolution(A, P, P[i], res)
    res.append(A[i])


def mr(X):
    n = len(X)
    dec = [1 for _ in range(n)]  # pomocnicza tabica z długościami ciągów malejących
    inc = [1 for _ in range(n)]  # pomocnicza tablica z długościami ciągów rosnących
    parent_inc = [-1 for _ in range(n)]
    parent_dec = [-1 for _ in range(n)]

    for i in range(1, n):
        # najdłuszy ciąg malejący konczący się w i
        for j in range(i):
            if X[i] < X[j] and dec[i] < dec[j] + 1:
                dec[i] = 1 + dec[j]
                parent_dec[i] = j  # zaznaczam w tablicy parenty, aby można było póżniej odtworzyć ciąg

    for i in range(n - 1, -1, -1):  # najdłuższy rosnący zaczynający się w i
        for j in range(i + 1, n):
            if X[i] < X[j] and inc[i] < inc[j] + 1:
                inc[i] = inc[j] + 1
                parent_inc[i] = j
    max_inc = max_dec = 0

    for i in range(n):
        if inc[i] > max_inc:
            i_inc = i
            max_inc = inc[i]
        if dec[i] > max_dec:
            i_dec = i
            max_dec = dec[i]
    res_dec = []
    res_inc = []
    if i_inc == i_dec:
        printsolution(X, parent_inc, i_inc, res_inc)
        printsolution(X, parent_dec, i_dec, res_dec)
        res_inc.reverse()
        res_inc.pop(0)
        return res_dec + res_inc
    elif max_dec >= max_inc:
        printsolution(X, parent_dec, i_dec, res_dec)
        return res_dec
    else:
        printsolution(X, parent_inc, i_inc, res_inc)
        res_inc.reverse()
        return res_inc


#runtests(mr)
print(mr([4,10,5,1,1,8,2,3,4]))