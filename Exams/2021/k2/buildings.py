# Inwestor planuje wybudować nowe osiedle akademików. Architekci przedstawili projekty budynków,
# z których inwestor musi wybrać podzbiór spełniając jego oczekiwania. Każdy budynek
# reprezentowany jest jako prostokąt o pewnej wysokości h, podstawie od punktu a do punktu b,
# oraz cenie budowy w (gdzie h, a, b i w to liczby naturalne, przy czym a < b). W takim budynku
# może mieszkać h ⋅ (b − a) studentów.
# Proszę zaimplementować funkcję:
# def select_buildings(T, p):
# ...
# która przyjmuje:
# • Tablicę T zawierająca opisy n budynków. Każdy opis to krotka postaci (h, a, b, w), zgodnie
# z oznaczeniami wprowadzonymi powyżej.
# • Liczbę naturalną p określającą limit łącznej ceny wybudowania budynków.
# Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych
# od 0), które nie zachodzą na siebie, kosztują łącznie mniej niż p i mieszczą maksymalną liczbę
# studentów. Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja powinna zwrócić
# zbiór o najmniejszym łącznym koszcie budowy. Dwa budynki nie zachodzą na siebie, jeśli nie mają
# punktu wspólnego.
# Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek. Funkcja
# powinna być możliwie jak najszybsza i zużywać jak najmniej pomięci. Należy bardzo skrótowo
# uzasadnić jej poprawność i oszacować złożoność obliczeniową.
# Przykład. Dla argumentów:
# T = [ (2, 1, 5, 3),
#       (3, 7, 9, 2),
#       (2, 8, 11, 1) ]
# p = 5
# wynikiem jest tablica: [ 0, 2 ]

from Exercise_1_tests import runtests

from math import inf


def print_tab(T):
    for i in T:
        print(i)
    print()


def select_buildings(T, p):
    T.sort(key=lambda x: x[2])
    n = len(T)
    D = [[-inf] * (p + 1) for _ in range(n)]
    results = [[-inf] * (p + 1) for _ in range(n)]

    D[0][T[0][3]] = (T[0][2] - T[0][1]) * T[0][0]
    results[0][T[0][3]] = True

    for i in range(1, n):
        for w in range(p + 1):
            # biorę
            if T[i][3] == w:
                D[i][w] = (T[i][2] - T[i][1]) * T[i][0]
                results[i][w] = True
            k = 0
            while T[k][2] < T[i][1] and k < i:
                if w - T[i][3] > -1 and D[k][w - T[i][3]] != -inf:
                    D[i][w] = D[k][w - T[i][3]] + (T[i][2] - T[i][1]) * T[i][0]
                    results[i][w] = k
                k += 1
            # nie biorę
            k = 0
            while k < i:
                if D[k][w] > D[i][w]:
                    D[i][w] = D[k][w]
                    results[i][w] = -1
                k += 1
    print_tab(D)

    max = val = 0
    for i in range(p + 1):
        if D[n - 1][i] > max:
            max = D[n - 1][i]
            val = i

    last = []
    n = n - 1
    while n > 0:
        if results[n][val] == -1:
            while results[n][val] == -1:
                n -= 1
        last.append(n)
        n, val = results[n][val], val - T[n][3]
    if results[n][val]:
        last.append(n)
    last.reverse()
    return last


# T = [(2, 1, 5, 3),
#      (3, 7, 9, 2),
#      (2, 8, 11, 1)]
# p = 5

T = [(1, 8, 12, 5), (4, 7, 8, 2), (3, 2, 3, 6), (9, 7, 8, 5), (8, 21, 22, 8), (5, 4, 7, 10), (1, 21, 24, 10), (7, 14, 16, 1)]
p = 32

res = select_buildings(T, p)
print(res)

# runtests(select_buildings)
