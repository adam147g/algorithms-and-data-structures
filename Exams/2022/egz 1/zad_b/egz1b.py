"""
Zuzanna Olszówka
W moim algorytmie na początku wyliczam jego wysokość (maxh).
Następnie znajduję poziom drzewa (H), na którym znajduje się najwięcej węzłów -przejście liniowe po tablicy i znalezienie maxa pod największym indeksem jeśli jest kilka maxów,
zliczając w tablicy o wysokości drzewa liczbę węzłów.
W kolejnym kroku dla każdego węzła zaznaczam w T.x True jeśli znajduje się na poziomie H albo False jeśli się nie znajduje.
Przechodze jeszcze raz rekurencyjnie po drzewie i zaznaczam dla każdego węzła True jeśli chociaż jeden z jego synów miał jakiegoś potomka na poziomie H i False jeśli żaden z potomków nie był na tym poziomie.
Na koniec zliczam liczbę węzłów, które nie mają żadnego potomka na poziomie H. Jeśli pole x węzła ma wartość False to już nie szukam głębiej, po muszę odciąć tylko jedną krawędź by usunąć całe poddrzewo.

Złożoność algorytmu: O(n)

"""

from egz1btesty import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = None  # pole do wykorzystania przez studentow


def wideentall(T):
    # def get_h(T, h=0): # liczy całkowitą wysokość drzewa
    #     nonlocal maxh
    #     if T is None:
    #         return
    #     maxh = max(maxh, h)
    #     get_h(T.left, h + 1)
    #     get_h(T.right, h + 1)

    def get_max(T, curr=0):
        if T is None:
            return 0
        return max(curr, get_max(T.left, curr + 1), get_max(T.right, curr + 1))

    def count_nodes(T, nodes, h=0):  # zlicza liczbę węzłów na każdym poziomie w drzewie
        if T is None:
            return
        nodes[h] += 1
        count_nodes(T.left, nodes, h + 1)
        count_nodes(T.right, nodes, h + 1)

    def is_on_H(T, H, currh=0):  # T.x = True jeśli węzeł lub jakiś jego potomek znajduje się na poziomie H
        if T is None:
            return
        if H == currh:
            T.x = True
        else:
            T.x = False
            a = is_on_H(T.left, H, currh + 1)
            b = is_on_H(T.right, H, currh + 1)
            if a or b:
                T.x = True
        return T.x

    def count_edges(T):  # zlicza liczbę krawędzi, które trzeba odciąć
        nonlocal res
        if T is None:
            return
        if not T.x:
            res += 1
            return
        count_edges(T.left)
        count_edges(T.right)

    # maxh = 0
    # get_h(T)
    maxh = get_max(T)
    nodes = [0] * (maxh + 1)
    count_nodes(T, nodes)
    H = 0
    curr_nodes = 1

    for i in range(1, maxh + 1):  # znajduje poziom drzewa na którym jest najwięcej węzłów
        if nodes[i] >= curr_nodes:
            curr_nodes = nodes[i]
            H = i

    is_on_H(T, H)
    res = 0
    count_edges(T)

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wideentall, all_tests=True)
