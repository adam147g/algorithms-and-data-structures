'''
Adam Górka
Algorytm przechodzi po każdej komnacie i zapisuje w liście curr_max największe dotychczasowe znalezione wartości dla
komnat i korzystając z kolejki priorytetowej uaktualnia te wartości
W ostatnim kroku, gdy kolejka jest pusta, zwracamy szukaną maksymalną wartość
'''
from egz2btesty import runtests
from queue import PriorityQueue
from math import inf


def magic(C):
    n = len(C)
    gold_in = []
    curr_max = [-inf] * n
    curr_max[0] = 0
    for i in range(n):
        gold_in.append(C[i][0])

    for i in range(n):
        for k in range(1, 4):
            dist, vertex = C[i][k]
            add = gold_in[i] - dist

            if add <= 10:
                if vertex > i and curr_max[i] + add >= 0 and curr_max[i] + add > curr_max[vertex]:
                    curr_max[vertex] = curr_max[i] + add
    print(curr_max)
    if curr_max[-1] == -inf:
        return -1
    return curr_max[-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
