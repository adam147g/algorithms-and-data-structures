#!/usr/bin/python
# -*- coding: utf-8 -*-

# Funkcja path_exist(V, x, y) sprawdza, czy istnieje ścieżka między wierzchołkami x i y
# w grafie reprezentowanym przez słownik V.
#
# Funkcja GTSP(G, a) rozwiązuje problem komiwojażera dla grafu G

from copy import deepcopy
from math import inf
import numpy as np
from typing import Dict, List


def path_exist(V, x, y):
    current = y
    for i in range(len(V.keys())):
        if current not in V.keys():
            return False
        current = V[current]
        if current == x:
            return True



def GTSP(G, a):
    V = dict()
    suma = 0
    a_copy = deepcopy(a)
    while len(V.keys()) < len(G.keys()):
        if (a_copy == inf).all() and len(V.keys()) < len(G.keys()):
            raise RuntimeError("Can't find solution")
        x, y = np.argmin(a_copy) // len(a_copy), np.argmin(a_copy) % len(a_copy[0])
        a_copy[x][y] = inf
        if x in V.keys() or y in V.values():
            continue
        if (y in V.keys() and x in V.values()) and (len(V.keys()) < (len(G.keys()) - 1)):
            if path_exist(V, x, y):
                continue
        V[x] = y
        suma += a[x][V[x]]
    return V, suma


def print_tsp(V, suma):
    string = str(0)
    current = V[0]
    for _ in range(len(V.keys())):
        string += ' -> '+ str(current)
        current = V[current]

    print(f"Koszt: {suma} \nCykl:\n{string}")



graph = {
    0: [1, 2, 3, 4],
    1: [0, 3, 6],
    2: [0, 3, 4, 5],
    3: [0, 1, 2, 5, 6],
    4: [0, 2, 5],
    5: [2, 3, 4, 6],
    6: [1, 3, 5],
}

a = np.array([[inf, 2, 1, 4, 3, inf, inf],
              [2, inf, inf, 3, inf, inf, 5],
              [1, inf, inf, 7, 1, 2, inf],
              [4, 3, 7, inf, inf, 4, 4],
              [3, inf, 1, inf, inf, 3, inf],
              [inf, inf, 2, 4, 3, inf, 3],
              [inf, 5, inf, 4, inf, 3, inf]])
'''
a = np.array([[inf, 2, 1, 4, 3, inf, inf],
              [2, inf, inf, 3, inf, inf, 5],
              [1, inf, inf, 7, 1, 2, inf],
              [4, 3, 7, inf, inf, 4, 4000],
              [3, inf, 1, inf, inf, 3, inf],
              [inf, inf, 2, 4, 3, inf, 3],
              [inf, 5, inf, 4000, inf, 3, inf]])
              
'''

g3 = {
    0: [1, 2, 3, 4],
    1: [0, 3, 6],
    2: [0, 3, 4, 5],
    3: [0, 1, 2, 5, 6],
    4: [0, 2, 5],
    5: [2, 3, 4, 6],
    6: [1, 3, 5]
}

a3 = np.array([[inf, 2, 1, 4, 3, 6, 10],
              [2, inf, 2, 3, 3, 3, 5],
              [1, 2, inf, 7, -1, 2, 4],
              [4, 3, 7, inf, 6, 4, 4],
              [3, 3, -1, 6, inf, 3, 8],
              [6, 3, 2, 4, 3, inf, 3],
              [10, 5, 4, 4, 8, 3, inf]])

graph2 = {
    0: [1, 2, 3, 4],
    1: [0, 3, 6],
    2: [0, 3, 4, 5],
    3: [0, 1, 2, 5, 6],
    4: [0, 2, 5],
    5: [2, 3, 4, 6],
    6: [1, 3, 5]
}

a2 = np.array([[inf, 2, 1, 4, 3, 12, 15],
              [2, inf, 14, 3, 30, 10, 5],
              [1, 20, inf, 7, 1, 2, 42],
              [4, 3, 7, inf, 32, 4, 4],
              [3, 5, 1, 43, inf, 3, 3],
              [16, 17, 2, 4, 3, inf, 3],
              [1, 5, 23, 4, 22, 3, inf]])


graph4 = {
    0: [1, 2, 3, 4],
    1: [0, 3, 6],
    2: [0, 3, 4, 5],
    3: [0, 1, 2, 5, 6],
    4: [0, 2, 5],
    5: [2, 3, 4, 6],
    6: [1, 3, 5, 9],
    7: [6],
    8: [6, 7],
    9: [8]
}

a4 = np.array([
     [inf, 2, 1, 4, 3, inf, inf, inf, inf, inf],
     [2, inf, inf, 3, inf, inf, 5, inf, inf, inf],
     [1, inf, inf, 7, 1, 2, inf, inf, inf, inf],
     [4, 3, 7, inf, inf, 4, 4, inf, inf, inf],
     [3, inf, 1, inf, inf, 3, inf, inf, inf, inf],
     [inf, inf, 2, 4, 3, inf, 3, inf, inf, inf],
     [inf, 5, inf, 4, inf, 3, inf, inf, inf, 0],
     [inf, inf, inf, inf, inf, inf, 4, inf, inf, inf],
     [inf, inf, inf, inf, inf, inf, 0, 4, inf, inf],
     [inf, inf, inf, inf, inf, inf, inf, inf, -1, inf]
])


V, suma = GTSP(graph, a)
print_tsp(V, suma)

V, suma = GTSP(graph2, a2)
print_tsp(V, suma)

V, suma = GTSP(g3, a3)
print_tsp(V, suma)
