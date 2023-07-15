# Znajdź największą liczbę słów które są takie same, bądź są anagramami
'''
wzorcowe rozwiązanie - podzielenie na kubełki, zamiana słów, by najbrdziej znacząca litera była mniejsza
np. 'stal' -> 'lats', bo l jest przed s w słowniku
posortowanie radix sortem i zliczenie takich samych
O(n)
'''

'''
Adam Górka ------------ był, ale już nie ma
Algorytm na początku przydziela napisy do odpowiednich pudełek pod względem ich długości, by odrzucić
wszystkie inne napisy podczas porównywania zapisów.
Następnie program sprawdza czy dane 2 wyrazy spełniają warunki zadania.
By algorytm działał szybciej, nie porównujemy napisów, które już wcześniej były zapisane jako równoważne z jakimiś innymi.
Kolejną wprowadzoną oprtyalizacją jest, aby omijać wszystkie pudełka, w których znajduje się mniej wyrazów,
niż maksymalny znaleziony dotychczas wynik.
Program jest poprawny, ponieważ porównuje ze sobą wszystkie napisy, które mogą spełnić warunki - tzn. o tej samej długości
oraz jeśli raz sprawdził słowo "1" ze słowem "2", to jeśli słowo "3" jest równoważne ze słowem "1",
to już nie sprawdzi słów "2" i "3"
'''
from kol1atesty import runtests


def counting_sort(A, idx, max_len):
    k = ord('z') - ord('a') + 2
    C = [0] * k
    B = [0] * len(A)
    for i in range(len(A)):
        C[ord(A[i][max_len - idx]) - ord('a') + 1] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        C[ord(A[i][max_len - idx]) - ord('a') + 1] -= 1
        B[C[ord(A[i][max_len - idx]) - ord('a') + 1]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]


def radix_sort(T):
    max_len = 0
    for string in T:
        max_len = max(max_len, len(string))
    idx = 1
    while idx <= max_len:
        counting_sort(T, idx, max_len)
        idx += 1
    return T


def g(T):
    min_ln, max_ln = 10 ** 10, 0
    for i in range(len(T)):
        ln = len(T[i])
        if ln < min_ln:
            min_ln = ln
        elif ln > max_ln:
            max_ln = ln
        if T[i] < T[i][::-1]:
            T[i] = T[i][::-1]

    buckets = [[] for _ in range(max_ln - min_ln + 1)]
    len_of_bucket = [0 for _ in range(max_ln - min_ln + 1)]
    for i in range(len(T)):
        x = len(T[i]) - min_ln
        buckets[x].append(T[i])
        len_of_bucket[x] += 1

    for i in range(len(buckets)):
        radix_sort(buckets[i])
    # print(T)
    result = 0
    for i in range(len(buckets)):
        if len_of_bucket[i] <= result:
            continue
        j, k = 0, 0
        while k < len_of_bucket[i]:
            j = k
            curr = 0
            while k < len_of_bucket[i] and buckets[i][j] == buckets[i][k]:
                k += 1
                curr += 1
                if curr > result:
                    result = curr
    return result


runtests(g, all_tests=True)
