class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None


root = Node()
root.value = 11
left_1 = Node()
root.left = left_1
left_1.parent = root
left_1.value = 3
left_2 = Node()
left_1.left = left_2
left_2.parent = left_1
left_2.value = 2
left_1_right = Node()
left_1.right = left_1_right
left_1_right.parent = left_1
left_1_right.value = 7
left_1_right_left = Node()
left_1_right.left = left_1_right_left
left_1_right_left.parent = left_1_right
left_1_right_left.value = 5
right = Node()
root.right = right
right.parent = root
right.value = 13


from math import inf


def in_order(root, t):
    if root is not None:
        in_order(root.left, t)
        t.append(root)
        in_order(root.right, t)


def maketree(t, l, r, root):
    n = r - l + 1
    if n > 0 and l > -1 and l + n // 2 + n // 2 < len(t):
        if t[l + n // 2] is not inf:
            root.left = t[l + n // 2]
            root.left.parent = root
            maketree(t, l, n // 2 - 1, root.left)

        if t[l + n // 2 + n // 2] is not inf:
            root.right = t[l + n // 2 + n // 2]
            root.right.parent = root
            maketree(t, n // 2 + 1, r, root.right)


t = []


def ConvertTree(root, t):
    in_order(root, t)
    n = len(t)
    root = t[n // 2]
    t[n // 2] = inf
    maketree(t, 0, n - 1, root)
    return root


ConvertTree(root, t)
t = []
in_order(root, t)
for i in range(len(t)):
    print(t[i].value, end=" ")
