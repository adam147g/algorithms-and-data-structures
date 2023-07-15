# Dana jest tablica klocków K[0], K[1], ..., K[n-1]. Każdy klocek to krotka (a,b,c),
# która mówi, że klocek zaczyna się na pozycji a, ciągnie się do b
# (wszystkie pozycje to nieujemne liczby naturalne) oraz ma wysokość c.
# Można założyć że a < b oraz c >= 1, oraz że a, b, c to liczby naturalne.
# Klocki układane są po kolei. Jeśli klocek nachodzi na któryś z poprzednich,
# to jest przymocowany na szczycie poprzedzającego klocka. Na przykład dla klocków
# opisanych przez (1,3,1), (2,5,2), (0,3,2), (8,9,3), (4,6,1) powstje konstrukcja
# o wysokości 5:
#    ___________
# 5||   K[2]    |    _______
# 4||___________|___|__K[4]_|        ____
# 3|        |    K[1]   |           |    |
# 2|     ___|___________|           |K[3]|
# 1|____|_K[0]__|___________________|____|_____
#   0   1   2   3   4   5   6   7   8    9   10
# Napisz finkcję, która zwraca wysokość konstrukcji.


class BST_node:
    def __init__(self, root, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = root
        self.max_height = 0
        self.all = False


def falling_block(root, a, b, last_value):
    if root.left is None and root.right is None:
        return root.max_height
    if root.all:
        return root.max_height
    actual_value = root.key
    if last_value > actual_value:
        if b >= last_value:
            if a > actual_value:
                return falling_block(root.right, a, b, actual_value)
            elif a < actual_value:
                return max(falling_block(root.left, a, b, actual_value), root.right.max_height)
            else:
                return root.right.max_height
        else:
            if b <= actual_value:
                return falling_block(root.left, a, b, actual_value)
            elif a >= actual_value:
                return falling_block(root.right, a, b, actual_value)
            else:
                return max(falling_block(root.left, a, b, actual_value), falling_block(root.right, a, b, actual_value))
    else:
        if a <= last_value:
            if b < actual_value:
                return falling_block(root.left, a, b, actual_value)
            elif b > actual_value:
                return max(falling_block(root.right, a, b, actual_value), root.left.max_height)
            else:
                return root.left.max_height
        else:
            if a >= actual_value:
                return falling_block(root.right, a, b, actual_value)
            elif b <= actual_value:
                return falling_block(root.left, a, b, actual_value)
            else:
                return max(falling_block(root.left, a, b, actual_value), falling_block(root.right, a, b, actual_value))


def place_the_block(root, a, b, last_value, height):
    if root.left is None and root.right is None:
        root.max_height = height
        return
    if root.all:
        root.all = False
        root.left.max_height = root.max_height
        root.left.all = True
        root.right.max_height = root.max_height
        root.right.all = True
    actual_value = root.key
    if last_value > actual_value:
        if b >= last_value:
            if a > actual_value:
                place_the_block(root.right, a, b, actual_value, height)
            elif a < actual_value:
                place_the_block(root.left, a, b, actual_value, height)
                root.right.max_height = height
                root.right.all = True
            else:
                root.right.max_height = height
                root.right.all = True
        else:
            if b <= actual_value:
                place_the_block(root.left, a, b, actual_value, height)
            if a >= actual_value:
                place_the_block(root.right, a, b, actual_value, height)
            else:
                place_the_block(root.right, a, b, actual_value, height)
                place_the_block(root.left, a, b, actual_value, height)
    else:
        if a <= last_value:
            if b < actual_value:
                place_the_block(root.left, a, b, actual_value, height)
            elif b > actual_value:
                place_the_block(root.right, a, b, actual_value, height)
                root.left.max_height = height
                root.left.all = True
            else:
                root.left.max_height = height
                root.left.all = True
        else:
            if a >= actual_value:
                place_the_block(root.right, a, b, actual_value, height)
            elif b <= actual_value:
                place_the_block(root.left, a, b, actual_value, height)
            else:
                place_the_block(root.right, a, b, actual_value, height)
                place_the_block(root.left, a, b, actual_value, height)
    root.max_height = max(root.max_height, height)
    return


def create_interval_tree(T, root, a, b):
    if b < a:
        return BST_node(root, None)
    mid = (a + b) // 2
    new_node = BST_node(root, T[mid])
    new_node.left = create_interval_tree(T, new_node, a, mid - 1)
    new_node.right = create_interval_tree(T, new_node, mid + 1, b)
    return new_node


def block_height(K):
    T = sum([[K[i][0], K[i][1]] for i in range(len(K))], [])
    T.sort()
    T.append(T[len(T) - 1] + 1)
    T = [T[i] for i in range(len(T) - 1) if T[i] != T[i + 1]]
    root = create_interval_tree(T, None, 0, len(T) - 1)
    for i in range(len(K)):
        height = K[i][2] + falling_block(root, K[i][0], K[i][1], -1)
        place_the_block(root, K[i][0], K[i][1], -1, height)
    return root.max_height



K1 = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
R1 = 5

K2 = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1), (5, 7, 1), (6, 8, 1)]
R2 = 6

K3 = [(1, 10 ** 10, 1)]
R3 = 1

TESTY = [(K1, R1), (K2, R2), (K3, R3)]

good = True
for KK, RR in TESTY:
    print("Klocki           : ", KK)
    print("Oczekiwany wynik : ", RR)
    WW = block_height(KK)
    print("Otrzymany wynik  : ", WW)
    if WW != RR:
        print("Błąd!!!!")
        good = False

if good:
    print("OK!")
else:
    print("Problemy!")