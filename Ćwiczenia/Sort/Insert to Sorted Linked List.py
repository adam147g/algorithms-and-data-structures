class Node:
    def __init__(self):
        self.next = None
        self.value = None

# Proszę zaimplementować wstawianie Node'a do posortowanej listy jednokierunkowej.

def insert_to_node(node, L):    # 'node' to wstawiany element
    start = L
    while L.next is not None and L.next.value < node.value:     # bo z wartownikiem
        L = L.next
    node.next = L.next
    L.next = node
    return start


def printList(L):
    if L is not None:
        print(L.value, end=' ')
        printList(L.next)
    else:
        print()




L = Node()

node1 = Node()
node1.value = 2
L.next = node1
printList(L)

node2 = Node()
node2.value = 5
node1.next = node2
printList(L)

node3 = Node()
node3.value = 7
insert_to_node(node3, L)
printList(L)

node4 = Node()
node4.value = 6
insert_to_node(node4, L)
printList(L)

node5 = Node()
node5.value = 1
insert_to_node(node5, L)
printList(L)

print()