from egzP3btesty import runtests
from queue import PriorityQueue


class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def make_set(v):
    return Node(v)


def convert_to_edges(graph):
    edges = []
    summ = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j][0] > i:
                edges.append((i, graph[i][j][0], -graph[i][j][1]))
                summ += graph[i][j][1]
    return edges, summ


def kruskal_algorithm(graph):
    edges, summ = convert_to_edges(graph)
    edges.sort(key=lambda x: x[2])
    MST = []
    V = []
    for i in range(len(graph)):
        V.append(make_set(i))
    to_add, mst_sum = None, 0
    flag = False
    visited = len(graph)
    for i in range(len(edges)):
        if visited < 0:
            break
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            mst_sum += edges[i][2]
            union(V[u], V[v])
            visited -= 1
        elif not flag and find(V[u]) == find(V[v]):
            to_add = edges[i]
            flag = True
    return summ + to_add[2] + mst_sum


def lufthansa(G):
    return kruskal_algorithm(G)


runtests(lufthansa, all_tests=True)
