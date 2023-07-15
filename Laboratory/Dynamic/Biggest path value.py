# Znajdź największą wartość ścieżki w drzewie binarnym
#
#        v
#      /   \
#    u      w
#           /
#          z

'''
           3
         /   \
        5     7
       / \    /
     -2   8  5
    / \   /
   3  1  200
      /
     93
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.f = 0


a = Node(93)
b = Node(1, a)
c = Node(3)
d = Node(-2, c, b)
e = Node(200)
f = Node(8, e)
g = Node(5, d, f)
h = Node(5)
i = Node(7, h)
root = Node(3, g, i)


def find(root):
    def f(v):
        if v is None:
            return 0
        L = f(v.left)
        R = f(v.right)
        v.f = max(0, v.val, v.val + L, v.val + R)
        return v.f

    def solution(v):
        nonlocal res
        if v is None:
            return
        if v.left is not None and v.right is not None and v.val + v.left.f + v.right.f > res:
            res = v.val + v.left.f + v.right.f
        if v.left is not None and v.val + v.left.f > res:
            res = v.val + v.left.f
        if v.right is not None and v.val + v.right.f > res:
            res = v.val + v.right.f

        solution(v.left)
        solution(v.right)

    f(root)
    res = 0
    solution(root)
    return res


print(find(root))
