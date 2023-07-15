'Sortowanie przez kopcowanie'


# HeapSort

# wyliczanie indeksu w tablicy lewego dziecka, prawego i rodzica, np.
#
#
#          parent(i)
#          /      \
#         /        \
#        i         coś tam,
#      /   \       nieistotne...
#     /     \
# left(i)   right(i)
#
#
def left(i):
    return 2 * i + 1  # i<<1 + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


# O(logn)
def heapify(A, n, i):
    l = left(i)  # i to potencjalnie zepsuty węzeł, sprawdzamy czy jest on wiekszy od swoch dzieci
    r = right(i)  # chemy ustawić tak, że m będzie miało ten indeks
    m = i  # spośród i, l, r, że m ma największą wartosć
    if l < n and A[l] > A[m]: m = l
    if r < n and A[r] > A[m]: m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)  # wywołujemy głębiej heapify
    return A


# O(n)
def buildheap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):  # for i=parent(n-1) to 0:
        heapify(A, n, i)
    return A


# O(n logn)
def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):  # w kopcu zawsze największa wartość jest w miescu A[0]
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
    return A


print("Heapsort")
# tab = [randint(0, 100) for _ in range(10)]
tab = [5, 5, 7, 2, 5, 1, 7, 5, 1, 2]
print(heapsort(tab))

