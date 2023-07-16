import numpy as np


class Node:
    def __init__(self, key, color=None):
        self.key = key
        self.color = color

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, weight=1):
        self.weight = weight

    def __str__(self):
        return str(self.weight)


class NMGraph:
    def __init__(self):
        self.map = {}
        self.vertices = []
        self.matrix = []

    def insertVertex(self, vertex):
        if not hash(vertex) in self.map:
            self.map[hash(vertex)] = len(self.vertices)
            self.vertices.append(vertex)
            if len(self.matrix) == 0:
                self.matrix.append([0])
            else:
                self.matrix.append([0 for _ in self.matrix])
                for elem in self.matrix:
                    elem.append(0)

    def insertEdge(self, vertex1, vertex2, edge):
        index1 = self.map[hash(vertex1)]
        index2 = self.map[hash(vertex2)]
        if self.matrix[index1][index2] == 0:
            self.matrix[index1][index2] = self.matrix[index2][index1] = 1

    def deleteVertex(self, vertex):
        index = self.map[hash(vertex)]
        self.map.pop(hash(vertex))
        self.vertices.pop(index)
        self.matrix.pop(index)
        for verse in self.matrix:
            verse.pop(index)
        for key, value in self.map.items():
            if value > index:
                self.map[key] = value - 1

    def deleteEdge(self, vertex1, vertex2):
        self.matrix[self.map[hash(vertex1)]][self.map[hash(vertex2)]] = \
            self.matrix[self.map[hash(vertex2)]][self.map[hash(vertex1)]] = 0

    def getVertexIdx(self, vertex):
        return self.map.get(hash(vertex), None)

    def getVertex(self, vertex_idx):
        return self.vertices[vertex_idx]

    def neighbours(self, vertex_idx):
        neighbours = []
        for i in range(len(self.matrix[vertex_idx])):
            if self.matrix[vertex_idx][i] != 0:
                neighbours.append(i)
        return np.array(neighbours)

    def order(self):
        return len(self.matrix)

    def size(self):
        size = 0
        for i in range(len(self.matrix)):
            for j in range(i, len(self.matrix)):
                if self.matrix[i][j]:
                    size += 1
        return size

    def edges(self):
        edges = []
        for i in range(len(self.matrix)):
            for j in range(i, len(self.matrix)):
                if self.matrix[i][j] != 0:
                    key1 = self.getVertex(i).key
                    key2 = self.getVertex(j).key
                    edges.append((key1, key2))
        return edges

    def getmatrix(self):
        return np.array(self.matrix)

    def degree(self, vertex_id):
        return np.sum(self.matrix[vertex_id])


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for j in nbrs:
            print(g.getVertex(j), end=";")
        print()
    print("-------------------")


def create_m0(p, g):
    p_ord = p.order()
    g_ord = g.order()
    m0 = np.zeros((p_ord, g_ord))
    for i in range(p_ord):
        for j in range(g_ord):
            m0[i][j] = p.degree(i) <= g.degree(j)
    return m0.astype(np.uint8)


def neighbours(g, vertex_idx):
    neighbours = []
    for i in range(len(g[vertex_idx])):
        if g[vertex_idx][i]:
            neighbours.append(i)
    return np.array(neighbours)


def prun(p, g, m):
    changed = 1
    while changed:
        changed = 0
        for i in range(len(p)):
            for j in range(len(g)):
                if m[i][j] == 1:
                    for x in neighbours(p, i):
                        mxy = []
                        for y in neighbours(g, j):
                            mxy.append(m[x][y])
                        if (np.array(mxy) == 0).all():
                            m[i][j] = 0
                            changed = 1
    for row in m:
        if (row == 0).all():
            return True
    return False


def ullman(p, g, m0=None, m_org=None, used_columns=None, current_row=0, no_recursion=0, no_izo=0, pr=False):
    if m_org is None:
        m_org = np.ones((len(p), len(g)))
        used_columns = np.zeros(len(m_org[0]))

    no_recursion += 1
    m = m_org.copy()

    if current_row == len(m):
        if (p == (m @ ((m @ g).T))).all():
            no_izo += 1
        return no_izo, no_recursion

    if pr:
        if prun(p, g, m):
            return no_izo, no_recursion

    for i in range(len(used_columns)):
        if used_columns[i] == 0 and (m0 is None or m0[current_row][i] == 1):
            m[current_row] = [0 for _ in range(len(m[0]))]
            m[current_row][i] = 1
            used_columns[i] = 1
            no_izo, no_recursion = ullman(p, g, m0, m, used_columns, current_row + 1, no_recursion, no_izo, pr)
            used_columns[i] = 0

    return no_izo, no_recursion



graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
G = NMGraph()
P = NMGraph()
for key in ['A', 'B', 'C', 'D', 'E', 'F']:
    G.insertVertex(Node(key))
for v1, v2, weight in graph_G:
    G.insertEdge(Node(v1), Node(v2), Edge(1))
for key in ['A', 'B', 'C']:
    P.insertVertex(Node(key))
for v1, v2, w in graph_P:
    P.insertEdge(Node(v1), Node(v2), Edge(w))

g = G.getmatrix()
p = P.getmatrix()
m = create_m0(P, G)

print(ullman(p, g))
print(ullman(p, g, m))
print(ullman(p, g, m, pr=True))
