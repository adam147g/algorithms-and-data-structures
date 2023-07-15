'''
Adam Górka
Algorytm przechodzi po każdej komnacie i zapisuje w liście curr_max największe dotychczasowe znalezione wartości dla
komnat i korzystając z kolejki priorytetowej uaktualnia te wartości
W ostatnim kroku, gdy kolejka jest pusta, zwracamy szukaną maksymalną wartość
'''
from egz2btesty import runtests
from queue import PriorityQueue
from math import inf
from time import perf_counter


def magic(C):
    n = len(C)
    gold_in = []
    curr_max = [-inf] * n
    curr_max[0] = 0
    for i in range(n):
        gold_in.append(C[i][0])
    queue = PriorityQueue()
    for i in range(1, 4):
        x = C[0][i]
        if x[1] < 0:
            continue
        else:
            '''
            take = min(10, gold_in[0] - x[0])
            _, vertex = x[0], x[1]
            if take >= 0:
                queue.put((-take, vertex))
            '''
            take = gold_in[0] - x[0]
            _, vertex = x[0], x[1]
            if 10 >= take >= 0:
                queue.put((-take, vertex))

    while not queue.empty():
        curr_gold, vertex = queue.get()
        curr_gold = -curr_gold
        if curr_gold > curr_max[vertex]:
            curr_max[vertex] = curr_gold
            if vertex == n - 1:
                continue
            for k in range(1, 4):
                x = C[vertex][k]
                if x[1] < vertex:
                    continue

                else:
                    '''
                    take = min(10, gold_in[vertex] - x[0])
                    dist = curr_gold + take
                    next_vertex = x[1]
                    if dist >= 0:
                        queue.put((-dist, next_vertex))
                    '''
                    take = gold_in[vertex] - x[0]
                    if take <= 10:
                        dist = curr_gold + take
                        next_vertex = x[1]
                        if dist >= 0:
                            queue.put((-dist, next_vertex))

    return curr_max[-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
