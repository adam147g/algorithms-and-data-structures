# Proszę zaimplementować algorytm sortowania przez scalanie dla list jednokierunkowych:
#       a) funkcja scalająca
#       b) funkcja sortująca


# a)



class Node:
    def __init__(self):
        self.next = None
        self.value = None


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        x = Node()
        x.value = A[i]
        C.next = x
        C = x
    return H.next


def printList(L):
    while L is not None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


def merge(L1, L2):
    head = Node()  # tworzę nowego node'a
    tail = head

    while L1 is not None and L2 is not None:
        if L1.value <= L2.value:  # biorę mniejszy i dopinam do node'a stworzonego
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

        tail = tail.next

    if L1 is None:
        tail.next = L2
    if L2 is None:
        tail.next = L1

    while tail.next is not None:
        tail = tail.next
    return head.next, tail


T1 = [0, 2, 4, 6, 7]
T2 = [1, 3, 5, 8, 8, 9]
L1 = tab2list(T1)
L2 = tab2list(T2)
printList(L1)
printList(L2)
print("MERGE")
L, t = merge(L1, L2)
printList(L)
printList(t)
print()


# b)



#  - szukanie 2-ch pierwszych podciągów posortowanych listy -
# cutlist(L) - funkcja szukająca podciągu posortowanego listy
# zwraca pierwszy element po posortowanej
# części listy - H (głowę po aktualnej)

def cutList(L):
    if L is None:
        return None
    while L.next is not None and L.next.value >= L.value:
        L = L.next
    H = L.next
    L.next = None
    return H

T = [3, 1, 2, 6, 2, 7]
L = tab2list(T)
printList(L)
print("CUTLIST")
H = cutList(L)
printList(L)
printList(H)
H_next = cutList(H)
printList(H)
printList(H_next)
print()

# O(n^2)
def MergeSort(L):
    if L is None:
        return None
    tail = cutList(L)
    S = L
    L = tail
    while L is not None:
        tail = cutList(L)
        S, _ = merge(S, L)
        L = tail
    return S


T = [3, 111, 2, 632, 2, 7, 54, 3, 74, 17, 3, 1, 9, 18, 0]
L = tab2list(T)
printList(L)
H = MergeSort(L)
printList(H)
print()

'''
Aby zrobić O(n logn) trzeba łączyć parami, a nie każde po kolei

1ciag   2ciag   3ciag   4ciag
   \      /        \      /
    \    /          \    /
   1,2ciag          3,4ciag
        \             /
         \           /
          \         /
          1,2,3,4ciag
          
A NIE:
1ciag   2ciag   3ciag   4ciag
   \      /  
    \    /  
   1,2ciag      3ciag   4ciag
        \         /
         \       /
        1,2,3ciag       4ciag
            \             /
             \           /
              \         /
              1,2,3,4ciag
'''

def cutlist(L):
    if L is None:
        return None
    while L.next is not None and L.next.value >= L.value:
        L = L.next
    H = L.next
    L.next = None
    return H, L # L to ogon

def mergesort(L):
    while True:
        NH = None
        NT = None
        while True:

            if L == None:
                L = NH
                break
            A = L
            L, T = cutlist(L)

            if NT == None and L == None:
                return A
            if L == None:
                NT.next = A
                L = NH
                break
            B = L
            L, _ = cutlist(L)


            X, T = merge(A,B)

            if NH == None:
                NH = X
            else:
                NT.next = X
            NT = T

T = [3, 111, 2, 632, 2, 7, 54, 3, 74, 17, 3, 1, 9, 18, 0]
L = tab2list(T)
printList(L)
H = mergesort(L)
printList(H)