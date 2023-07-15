# Dana jest tablica symboli S oraz tablica ich częstości F. Przykładowe dane to:
#   S = ["a", "b", "c", "d", "e", "f" ]
#   F = [10 , 11 ,  7 , 13 ,  1 , 20  ]
#   symbol "a" ma częstość 10, symbol "b" ma częstość 11 itd.
#
# Proszę napisać funkcję huffman( S, F), która oblicza kod Huffmana dla
# takich danych, wypisuje symbol (w kolejności z tablicy S) wraz z jego
# kodem, oraz łączną liczbę bitów potrzebną do wypisania napisu, w którym
# każdy symbool występuje podaną częstość razy. Przykładowy wynik dla
# podanego powyżej wejścia to:
# a : 011
# b : 10
# c : 0101
# d : 11
# e : 0100
# f : 00
# długość napisu: 150

from queue import PriorityQueue


class Node():
    def __init__(self, left=None, right=None, value=None):
        self.value = value
        self.left = left
        self.right = right


def create_huffman_tree(frequencies):
    queue = PriorityQueue()
    for value in frequencies:
        queue.put(value)
    while queue.qsize() > 1:
        left, right = queue.get(), queue.get()
        node = Node(left, right)
        queue.put((left[0] + right[0], node))
    return queue.get()


def walk_tree(node, prefix="", code=None):
    if code is None:
        code = []
    if isinstance(node[1].left[1], Node):
        walk_tree(node[1].left, prefix + "0", code)
    else:
        code.append((node[1].left[1], prefix + "0"))
    if isinstance(node[1].right[1], Node):
        walk_tree(node[1].right, prefix + "1", code)
    else:
        code.append((node[1].right[1], prefix + "1"))
    return code


def huffman(S, F):
    T = [0] * len(F)
    for i in range(len(S)):
        T[i] = (F[i], i, S[i])
    node = create_huffman_tree(T)
    code = walk_tree(node)
    code.sort(key=lambda x: x[0])
    for i in range(len(S)):
        print(S[i][0], ":", code[i][1])
    result = 0
    for i in range(len(S)):
        result += + len(code[i][1]) * F[i]
    print("length of string:", result)


S = ["a", "b", "c", "d", "e", "f"]
# F = [ 10,  11,  7,   13,  1,   20]
F = [8.71, 7.9, 3.45, 1.29, 3.1, 4.63]

huffman(S, F)
