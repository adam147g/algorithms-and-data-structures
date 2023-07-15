# Inwestor planuje wybudować nowe osiedle akademików. Architekci przedstawili projekty budynków,
# z których inwestor musi wybrać podzbiór spełniając jego oczekiwania. Każdy budynek reprezentowany
# jest jako prostokąt o pewnej wysokości h, podstawie od punktu a do punktu b, oraz cenie budowy w
# (gdzie h, a, b i w to liczby naturalne, przy czym a < b). W takim budynku może mieszkać h*(b − a)
# studentów. Proszę zaimplementować funkcję:
# def select_buildings(T, p):
#     ...
# która przyjmuje:
#   - Tablicę T zawierającą opisy n budynków. Każdy opis to krotka postaci (h, a, b, w), zgodnie
# z oznaczeniami wprowadzonymi powyżej.
#   - Liczbę naturalną p określającą limit łącznej ceny wybudowania budynków.
# Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych od 0),
# które nie zachodzą na siebie, kosztują łącznie mniej niż p i mieszczą maksymalną liczbę studentów.
# Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja powinna zwrócić zbiór
# o najmniejszym łącznym koszcie budowy. Dwa budynki nie zachodzą na siebie, jeśli nie mają punktu
# wspólnego. Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek.
# Funkcja powinna być możliwie jak najszybsza i zużywać jak najmniej pomięci. Należy bardzo skrótowo
# uzasadnić jej poprawność i oszacować złożoność obliczeniową.

'''
Adam Górka
Algorytm spełnia funkcję f, gdzie
f(i,j) - oznacza maksymalną ilość studentów, jaką mogą pomieścić budynki nie nachodzące się na siebie
         w kolejności od lewej strony do i-tego indeksu o maksymalnej łącznej cenie budowy <= j.

f(0,j) =  0,                        dla j  < T[0][3]
         (T[0][2]-T[0][1])*T[0][0], dla j >= T[0][3]

f(i,j) = max{ f(i-1,j), (T[i][2]-T[i][1])*T[i][0],  f(parent[i], j - T[i][3]) + (T[i][2]-T[i][1])*T[i][0]}
                                                ,gdzie parent[i] - pierwszy
                                                nienachodzący na i-ty budynek
Lista parent jest wypełniana w linijkach 40-44.
Po wypełnieniu macierzy F, znajdujemy listę budynków, zapomocą funkcji get_res,
rekurencyjnie przechodząc po tablicy i sprawdzając, które budynki wybieraliśmy by uzyskać optymalne rozwiązanie.
'''
# Poprawione na n(logn)

from Exercise_1_tests import runtests


def binary_search(T, x, p, r):
    if r < p:
        return None
    if p == r and p == 0:
        if T[0][2] < x:
            return 0
        return None
    k = (p + r) // 2
    if T[k + 1][2] >= x and T[k][2] < x:
        return k
    elif T[k][2] >= x:
        return binary_search(T, x, p, k - 1)
    return binary_search(T, x, k + 1, r)


def get_res(T, F, parent, idx, val, res):
    '''
    Działa dobrze, bo dla 1 testu są 2 poprawne odpowiedzi
    :param res: dotychczasowe budynki
    :return: wynikowa lista
    '''
    if idx is None:
        return res
    if idx == 0:
        if val >= T[0][3]:
            res.append(T[0][4])
        return res
    if F[idx - 1][val] == F[idx][val]:
        return get_res(T, F, parent, idx - 1, val, res)
    res.append(T[idx][4])
    return get_res(T, F, parent, parent[idx], val - T[idx][3], res)


def select_buildings(T, p):
    n = len(T)
    print(T)
    for i in range(n):
        T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    T.sort(key=lambda x: x[2])
    parent = [None] * n
    F = [[0 for _ in range(p + 1)] for _ in range(n)]
    for i in range(1, n):
        parent[i] = binary_search(T, T[i][1], 0, i - 1)
    for val in range(T[0][3], p + 1):
        F[0][val] = (T[0][2] - T[0][1]) * T[0][0]
    for idx in range(1, n):
        for val in range(p + 1):
            F[idx][val] = F[idx - 1][val]
            if parent[idx] is not None and val >= T[idx][3] and \
                    F[parent[idx]][val - T[idx][3]] + (T[idx][2] - T[idx][1]) * T[idx][0] > F[idx][val]:
                F[idx][val] = F[parent[idx]][val - T[idx][3]] + (T[idx][2] - T[idx][1]) * T[idx][0]
            elif parent[idx] is None and val >= T[idx][3] and (T[idx][2] - T[idx][1]) * T[idx][0] > F[idx][val]:
                F[idx][val] = (T[idx][2] - T[idx][1]) * T[idx][0]

    result = []
    result = get_res(T, F, parent, n - 1, p, result)
    return sorted(result)


runtests(select_buildings)