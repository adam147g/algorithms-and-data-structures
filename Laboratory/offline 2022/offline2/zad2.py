'''
Adam Górka
Implementacja:
Algorytm polega na posortowaniu listy według początków przedziałów, następnie zliczaniu
przedziałów, które zaczynają się od L[i][0] oraz znaleniu największego z nich.
W linijkach 57-63 algorytm sprawdza ile przedziałów zawiera wcześniej znaleziony najdłuższy
przedział zaczynający sie na L[i][0] oraz znalezieniu pierwszego, który się w nim nie zawiera.
W linijce 64 algorytm dodaje przedziały zawierające się w całości w analizowanym przedziale.
W 70 linijce algorytm szuka pierwszego przedziału w L, który ma być analizowany jako kolejny -
czyli pierwszego o takim samym początku, jak ten, który się pierwszy nie zawierał - next_start.
Poprawność:
Algorytm nie analizuje przedziałów, które się w całości zawierają w większym (obecnym),
przez co mamy pewność, że te mniejsze nie będą przedziałem, w którym się zawiera najwięcej pozostałych .
Złożoność wynika głównie z sortowania i wynosi O(n*logn)
'''
from zad2testy import runtests


def quick_sort(T, p, r):
    if p < r:
        T[(p + r) // 2], T[p] = T[p], T[(p + r) // 2]
        pivot = T[p][0]
        i = p - 1
        j = r + 1
        while True:
            i += 1
            while T[i][0] < pivot:
                i += 1
            j -= 1
            while T[j][0] > pivot:
                j -= 1
            if i >= j:
                q = j
                break
            T[i], T[j] = T[j], T[i]
        quick_sort(T, p, q)
        quick_sort(T, q + 1, r)


def depth(L):
    n = len(L)
    quick_sort(L, 0, n - 1)
    i = 0
    next_start = 0
    curr_max = 0
    while i < n:
        intervals_start_with_me = 0
        max_start_with_me = L[i][1]
        j = i + 1
        flag = True
        while j < n and L[i][0] == L[j][0]:
            if L[j][1] > max_start_with_me:
                max_start_with_me = L[j][1]
            intervals_start_with_me += 1
            j += 1
        curr = 0
        while j < n and L[j][0] <= max_start_with_me:
            if L[j][1] <= max_start_with_me:
                curr += 1
            elif flag:
                next_start = j
                flag = False
            j += 1
        if curr + intervals_start_with_me > curr_max:
            curr_max = curr + intervals_start_with_me
        if flag:
            next_start = j
        i = next_start
        if i < n:
            while i > 0 and L[i][0] == L[i - 1][0]:
                i -= 1
    return curr_max


runtests(depth)
