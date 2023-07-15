from egzP6btesty import runtests


class QST:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Q = [None for _ in range(4)]
        self.val = 1

    def add(self, other):
        node = self
        flag = True     # - wprowadzone w celu wykluczenia błędu: maximum recursion depth
        while flag:
            # print((self.x,self.y), (other.x ,other.y))
            if node.x == other.x and node.y == other.y:
                node.val += 1
                flag = False
            else:
                if node.x < other.x and node.y <= other.y:
                    if node.Q[0] is None:
                        node.Q[0] = other
                        flag = False
                    else:
                        # node.Q[0].add(other)
                        node = node.Q[0]
                elif node.x >= other.x and node.y < other.y:
                    if node.Q[1] is None:
                        node.Q[1] = other
                        flag = False
                    else:
                        # node.Q[1].add(other)
                        node = node.Q[1]
                elif node.x > other.x and node.y >= other.y:
                    if node.Q[2] is None:
                        node.Q[2] = other
                        flag = False
                    else:
                        # node.Q[2].add(other)
                        node = node.Q[2]
                # elif node.x <= other.x and node.y > other.y:
                else:
                    if node.Q[3] is None:
                        node.Q[3] = other
                        flag = False
                    else:
                        # node.Q[3].add(other)
                        node = node.Q[3]

    def count(self):
        output = 0
        if self.val % 2:
            output += 1
        for i in self.Q:
            if i:
                output += i.count()
        return output


def jump(M):
    x, y = 0, 0
    root = QST(x, y)
    for el in M:
        if el == 'UL':
            x, y = x - 1, y + 2
        elif el == 'UR':
            x, y = x + 1, y + 2
        elif el == 'RU':
            x, y = x + 2, y + 1
        elif el == 'RD':
            x, y = x + 2, y - 1
        elif el == 'DR':
            x, y = x + 1, y - 2
        elif el == 'DL':
            x, y = x - 1, y - 2
        elif el == 'LD':
            x, y = x - 2, y - 1
        elif el == 'LU':
            x, y = x - 2, y + 1
        root.add(QST(x, y))
    return root.count()


runtests(jump, all_tests=True)
