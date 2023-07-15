'''
Adam Górka
Algorytm w pierwszych linijkach tworzy graf graph_list z listy E.
W kolejnym kroku dodaje do nowego grafu krawędzie między wierzchołkami z listy S o wadze 0, gdyż między tymi
wierzchołkami możemy się przemieszczać bez kosztu. Po przygotowaniu grafu wywyołujemy na nim algorytm Dijkstry,
który znajdzie nam najmniejszą odległość z wierzchołka a do wierzchołka b.
Jako, że potrzebujemy tylko dystans pomiędzy a i b, w algorytmie Dijkstry dałem warunek, że jeśli z kolejki
priorytetowej ściągamy wierzchołek b, to nie potrzebujemy, aby algorytm działał dalej i zwracamy szukaną odległość.
Algorytm jest poprawny, ponieważ zagięcie czasoprzestrzeni, to w rzeczywistości koszt 0 dotarcia do innego wierzchołka,
a użyty algorytm Dijkstry wiemy, że jest poprawny.
Złożoność czasowa to O(m logn) - czyli złożoność algorytmu Dijkstry.
'''
from kol3atesty import runtests
from queue import PriorityQueue
from math import inf


def dijkstra_algorithm(n, graph, a, b):
    queue = PriorityQueue()
    distances = [inf] * n
    queue.put((0, a))
    while not queue.empty():
        curr_dist, v = queue.get()
        if v == b:
            return curr_dist
        if curr_dist < distances[v]:
            distances[v] = curr_dist
            for edge in graph[v]:
                queue.put((curr_dist + edge[1], edge[0]))
    return None


def spacetravel(n, E, S, a, b):
    len_s = len(S)
    graph_list = [[] for _ in range(n)]
    for i in range(len(E)):
        graph_list[E[i][0]].append((E[i][1], E[i][2]))
        graph_list[E[i][1]].append((E[i][0], E[i][2]))
    for i in range(1, len_s):
        graph_list[S[i]].append((S[i - 1], 0))
        graph_list[S[i - 1]].append((S[i], 0))

    return dijkstra_algorithm(n, graph_list, a, b)


runtests(spacetravel, all_tests=True)
