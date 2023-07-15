from egzP4btesty import runtests


class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None


def max_val(x):
    max_ = x
    while max_.right is not None:
        max_ = max_.right
    return max_


def find_prev(x):
    if x.left is not None:
        return max_val(x.left)
    p = x
    p_par = p.parent
    while p_par:
        if p != p_par.left:
            break
        p = p_par
        p_par = p.parent
    return p_par


def min_val(x):
    min_ = x
    while min_.left is not None:
        min_ = min_.left
    return min_


def find_next(x):
    if x.right is not None:
        return min_val(x.right)
    p = x
    p_par = p.parent
    while p_par:
        if p != p_par.right:
            break
        p = p_par
        p_par = p.parent
    return p_par


def sol(root, T):
    result = 0
    for x in T:
        if find_prev(x).key + find_next(x).key == x.key * 2:
            result += x.key

    return result


runtests(sol, all_tests=True)
