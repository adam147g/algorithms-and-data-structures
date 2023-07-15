# Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
# class Node:
#     def __init__(self):
#         self.value = None
#         self.next = None
# Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste
# a[1], a[2], ..., a[n] (lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego
# elementu zachodzi, że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej
# o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
# [1, 0, 3, 2, 4, 6, 5], a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
# Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
# Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
# oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n
# listy oraz parametru k). Proszę oszacować jego złożoność czasową dla k = Θ(1), k = Θ(log(n))
# oraz k = Θ(n).

from Exercise_2_tests import runtests
from time import perf_counter

class Node:
    def __init__(self):
        self.val = None
        self.next = None

def heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and A[l].val < A[m].val: m = l
    if r < n and A[r].val < A[m].val: m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)
    return A


def buildheap(A):
    n = len(A)
    for i in range(((n - 1) - 1) // 2, -1, -1):
        heapify(A, n, i)
    return A


def HeapSort(A):
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
    return A


def SortH(p, k):
    if k == 0:
        return p

    if p.next == None:
        return p
    if k == 1:
        q = p.next
        if q.val < p.val:
            first = q
            p.next = q.next
            first.next = p
            q = p.next
        else:
            first = p
        while q != None and q.next != None:
            if q.next.val < q.val:
                p.next = q.next
                q.next = q.next.next
                p.next.next = q
            p = q
            q = q.next
        return first

    A = []
    i = 0
    while i <= k and p.next != None:
        A.append(p)
        p = p.next
        i += 1
    buildheap(A)
    first = A[0]
    new = first
    while p.next != None:
        A[0] = p
        heapify(A, len(A), 0)
        p = p.next
        new.next = A[0]
        new = new.next
    A.append(p)
    HeapSort(A)
    A.pop()
    while len(A) > 0:
        new.next = A.pop()
        new = new.next
    new.next = None
    return first


runtests(SortH)