'''
Adam Górka
Idea algorytmu polega na stworzeniu kopca k - elementowego (funkcja buildheap) za pomocą tablicy A, z którego
na bieżąco zabieramy węzeł o minimalnej wartości, wstawiamy go do już posortowanej listy, a następnie wstwiamy
do kopca kolejny węzeł i naprawiamy kopiec (heapify).
W momencie, gdy nie możemy już dodać żadnych Node'ów, sortujemy tablicę A za pomocą HeapSort i dołączamy pozostałe węzły.
Dzięki rozmiarowi kopca  - k - mamy pewność, że poszczególne wartości będą brane pod uwagę w obrębie k miejsc.
Dla optymalizacji uwzględniłem 2 osobne przypadki - kiedy lista jest posortowana (k==0) oraz gdy węzły listy różnią
się maksymalnie o jedną pozycję (k==1)
Złożoność czasowa algorytmu wynosi O(n*logk) - wynika to z konieczności n razy wywołania funkcji heapify,
która ma złożoność O(logk).
Złożoność dla kolejnych danych:
k: O(1) - O(n)
k: O(logn) - O(n*loglogn)
k: O(n) - O(n*logn)
'''
from zad1testy import Node, runtests


def heapify(A, n, i):
    l = 2 * i + 1   # l = i<<1+1
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

    if p.next is None:
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
        while q is not None and q.next is not None:
            if q.next.val < q.val:
                p.next = q.next
                q.next = q.next.next
                p.next.next = q
            p = q
            q = q.next
        return first

    A = []
    i = 0
    while i <= k and p.next is not None:
        A.append(p)
        p = p.next
        i += 1
    buildheap(A)
    first = A[0]
    new = first
    while p.next is not None:
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
