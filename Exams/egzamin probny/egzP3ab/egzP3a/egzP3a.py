from egzP3atesty import runtests
from math import inf


class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze
        self.x = None


def f(DP, P, W, cost, idx):
    if cost < 0:
        return -inf
    if idx < 0 or idx >= len(P):
        return 0
    if DP[idx][cost] is not None:
        return DP[idx][cost]
    taken, not_taken = f(DP, P, W, cost - W[idx], idx - 1) + P[idx], f(DP, P, W, cost, idx - 1)
    if taken > not_taken:
        DP[idx][cost] = taken
    else:
        DP[idx][cost] = not_taken
    return DP[idx][cost]


def wybory(T):
    result = 0
    for el in T:
        cost = el.fundusze
        P = []
        W = []
        p = el
        while p is not None:
            P.append(p.wyborcy)
            W.append(p.koszt)
            p = p.next
        DP = [[None for _ in range(cost + 1)] for _ in range(len(P))]
        result += f(DP, P, W, cost, len(P) - 1)
    return result


runtests(wybory, all_tests=True)
