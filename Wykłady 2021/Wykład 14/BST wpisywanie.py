from random import randint


class BST_Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def make_tree(T, start, stop, parent, left, right, visited):
    if stop - start > 0 and stop < len(T) and start > -1:
        x = (stop - start) // 2 + start
        visited[x] = True
        lewy = (x - 1 - start) // 2 + start
        if lewy > -1 and not visited[lewy]:
            left[x] = lewy
            parent[lewy] = x
        prawy = (stop - x + 1) // 2 + x
        if prawy < len(T) and not visited[prawy]:
            right[x] = prawy
            parent[prawy] = x
        make_tree(T, start, x - 1, parent, left, right, visited)
        make_tree(T, x + 1, stop, parent, left, right, visited)


def printing(T, left, right, x):
    if left[x] is not None:
        printing(T, left, right, left[x])
    print(T[x], end=" - ")
    if right[x] is not None:
        printing(T, left, right, right[x])


def make_node_tree_with_tabs(T):
    n = len(T)
    parent = [None] * n
    left = [None] * n
    right = [None] * n
    visited = [False] * n
    make_tree(T, 0, n - 1, parent, left, right, visited)
    print(T)
    print("parent -", parent)
    print("left -", left)
    print("right -", right)
    print()
    printing(T, left, right, (n - 1) // 2)
    print()
    print("---------------")
    for i in range(n):
        T[i] = BST_Node(T[i])
    for i in range(n):
        if parent[i] is not None:
            T[i].parent = T[parent[i]]
        if left[i] is not None:
            T[i].left = T[left[i]]
        if right[i] is not None:
            T[i].right = T[right[i]]
    return T[(n - 1) // 2]


def show_if_is_good(p):
    if p.left is not None:
        show_if_is_good(p.left)
    print(p.key, end=" - ")
    if p.right is not None:
        show_if_is_good(p.right)


n = 14
T = [randint(1, 40) for _ in range(n)]
T.sort()
p = make_node_tree_with_tabs(T)
if p is not None:
    show_if_is_good(p)
