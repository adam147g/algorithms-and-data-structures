class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if self.key == other.key:   return True
        return False

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, weight=0, flag=False):
        self.weight = weight
        self.flow = 0
        self.residual = weight
        self.isResidual = flag

    def __repr__(self):
        return str(self.weight) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.isResidual)


class AdjacencyListGraph:
    def __init__(self):
        self.adjacency_list = []
        self.dictionary = {}

    def insertVertex(self, vertex):
        self.dictionary[vertex] = len(self.adjacency_list)
        self.adjacency_list.append([])

    def insertEdge(self, vertex1, vertex2, edge):
        self.adjacency_list[self.dictionary[vertex1]].append([self.dictionary[vertex2], edge])

    def deleteVertex(self, vertex):
        idx = self.dictionary[vertex]
        for i in range(len(self.adjacency_list)):
            if idx in self.adjacency_list[i]:
                self.adjacency_list[i].remove(idx)

            for j in range(len(self.adjacency_list[i])):
                if self.adjacency_list[i][j] > idx:
                    self.adjacency_list[i][j] -= 1

        del self.adjacency_list[idx]
        del self.dictionary[vertex]

        for vertex_, val in self.dictionary.items():
            if val > idx:
                self.dictionary[vertex_] = val - 1

    def deleteEdge(self, vertex1, vertex2):
        self.adjacency_list[self.dictionary[vertex1]].remove(self.dictionary[vertex2])

    def getVertexIdx(self, vertex):
        return self.dictionary[vertex]

    def getVertex(self, vertex_idx):
        for vertex, val in self.dictionary.items():
            if val == vertex_idx:
                return vertex
        return None

    def neighbours(self, vertex_idx):
        return self.adjacency_list[vertex_idx]

    def order(self):
        return len(self.adjacency_list)

    def size(self):
        total = 0
        for x in self.adjacency_list:
            total += len(x)
        return total // 2

    def edges(self):
        result = []
        for i in range(len(self.adjacency_list)):
            for j in self.adjacency_list[i]:
                result.append([self.getVertex(i).key, self.getVertex(j).key])
        return result


def BFS(G):
    visited = [False] * G.order()
    parent = [None] * G.order()
    queue = []
    queue.append(0)
    visited[0] = True
    while len(queue) > 0:
        v = queue.pop(0)
        for u in G.neighbours(v):
            if not visited[u[0]] and u[1].residual > 0:
                queue.append(u[0])
                visited[u[0]] = True
                parent[u[0]] = v
    return parent


def analysys(G, start, finish, parent):
    if parent[finish] is None:
        return 0
    curr_idx = finish
    min_poj = float('inf')
    real = None
    while curr_idx != start:
        for x in G.neighbours(parent[curr_idx]):
            if x[0] == curr_idx:
                real = x[1]
                break
        if real != None and real.residual < min_poj:
            min_poj = real.residual
        curr_idx = parent[curr_idx]

    return min_poj


def augmentation(G, start, finish, parent, min_poj):
    if parent[finish] is None:
        return 0
    curr_idx = finish
    real = rest = None
    while curr_idx != start:
        for x in G.neighbours(parent[curr_idx]):
            if x[0] == curr_idx:
                real = x[1]
                break
        real.flow += min_poj
        real.residual -= min_poj
        for x in G.neighbours(curr_idx):
            if x[0] == parent[curr_idx]:
                rest = x[1]
                break
        rest.residual += min_poj
        curr_idx = parent[curr_idx]


def FrodFulkenson(G):
    parent = BFS(G)
    min_poj = analysys(G, 0, G.order() - 1, parent)
    while min_poj > 0:
        augmentation(G, 0, G.order() - 1, parent, min_poj)
        parent = BFS(G)
        min_poj = analysys(G, 0, G.order() - 1, parent)
    count = 0
    for i in range(G.order() - 1):
        for u in G.neighbours(i):
            if u[0] == G.order() - 1:
                count += u[1].flow
    return count


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


def make_g_0():
    g = AdjacencyListGraph()
    g.insertVertex('s')
    g.insertVertex('u')
    g.insertVertex('v')
    g.insertVertex('t')
    g.insertEdge('s', 'u', Edge(2))
    g.insertEdge('u', 't', Edge(1))
    g.insertEdge('u', 'v', Edge(3))
    g.insertEdge('s', 'v', Edge(1))
    g.insertEdge('v', 't', Edge(2))
    g.insertEdge('u', 's', Edge(0, True))
    g.insertEdge('t', 'u', Edge(0, True))
    g.insertEdge('v', 'u', Edge(0, True))
    g.insertEdge('v', 's', Edge(0, True))
    g.insertEdge('t', 'v', Edge(0, True))
    return g


def main():
    g_0 = make_g_0()
    print(FrodFulkenson(g_0))
    printGraph(g_0)


main()
