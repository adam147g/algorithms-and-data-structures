class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def split(L):
    while L.next is not None and L.val <= L.next.val:
        L = L.next
    tail = L.next
    L.next = None
    return tail


def tail(L):
    while L.next is not None:
        L = L.next
    return L


def merge(A, B):
    C = Node(None)
    D = C
    while True:
        if A is None:
            D.next = B
            return C.next, tail(B)

        if B is None:
            D.next = A
            return C.next, tail(A)
        if A.val <= B.val:
            D.next = A
            A = A.next
            D = D.next
        else:
            D.next = B
            B = B.next
            D = D.next


def merge_sort(L):
    T = tail(L)
    while True:
        A = L
        L = split(L)
        if L is None:
            return A
        B = L
        L = split(L)
        C, D = merge(A, B)
        if L is None:
            return C
        T.next = C
        T = D

