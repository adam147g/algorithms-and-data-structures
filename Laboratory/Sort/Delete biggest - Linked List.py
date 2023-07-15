class Node:
    def __init__(self):
        self.next = None
        self.value = None

def printList(L):
    if L is not None:
        print(L.value, end=' ')
        printList(L.next)
    else:
        print()


# Proszę zaimplementować usuwanie z listy jednokierunkowej największej liczby.

def delete_max(L):
    first = L
    max = L.next
    max_prev = L
    q = L
    L = L.next
    while L is not None:
        if L.value > max.value:
            max_prev = q
            max = L
        q = L
        L = L.next

    max_prev.next = max.next
    return first

# lub

def delMax(L):
    p = L.next
    p_prev = L

    prev = L
    L = L.next
    while prev.next is not None:
        if prev.next.value > p.value:
            p_prev = prev
            p = prev.next
        prev = prev.next

    p_prev.next = p.next
    return L


L = Node()
node1 = Node()
node1.value = 2
L.next = node1

node2 = Node()
node2.value = 5
node1.next = node2

node3 = Node()
node3.value = 1
node2.next = node3

node4 = Node()
node4.value = 14
node3.next = node4

node5 = Node()
node5.value = 7
node4.next = node5

node6 = Node()
node6.value = 4
node5.next = node6

while L.next is not None:
    printList(L)
    delete_max(L)
