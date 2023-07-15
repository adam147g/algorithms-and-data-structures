# Adam Górka
# Algorytm apisuje do tablicy array Node, Node.key oraz indeks interesującego nas klucza
# To algorytmem InOrder - O(n)
# Na koniec przechodzimy po tablicy array i szukamy, czy indeks danej wartości znajduje
# się w tablicy X - O(n+m)

# Złożoność pamięciowa - O(n+m)

from math import inf
from zad3testy import runtests


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.key = None


def traverse_tree(T, array, idx):
    if T is not None:
        traverse_tree(T.left, array, 2 * idx)
        array.append((T, T.key, idx))
        traverse_tree(T.right, array, (2 * idx) + 1)


def maxim(T, C):
    array = []
    traverse_tree(T, array, 1)
    '''array.sort(key=lambda x: x[1])
    array.reverse()
    for i in range(len(array)):
        for j in range(len(C)):
            if array[i][2] == C[j]:
                return array[i][1]
    '''
    visited = [False] * (len(array) + 1)
    for x in C:
        visited[x] = True
    max_ = -inf
    for i in range(len(array)):
        if visited[array[i][2]]:
            max_ = max(max_, array[i][1])
    if max_ != -inf:
        return max_
    return -1


runtests(maxim)
