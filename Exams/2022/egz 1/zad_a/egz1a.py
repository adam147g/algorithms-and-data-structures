"""
Zuzanna Olszówka
Algorytm zachłanny:
Istnieje taki dzień, w którym śnieg na wszystkich obszarach do tego dnia albo się stopi albo zostanie zebrany.
W związu z tym chcemy zebrać śnieg z obszarów z największą ilością śniegu, ponieważ na każdym obszarze śnieg topi się równomiernie.
Dzięki temu nie ma też różnicy w tym, czy będziemy zbierać śnieg z zachodniej czy ze wschodniej strony, bo do żeby wymaksować
ilość śniegu wystarczy zebrać te największe obszary do momentu aż wszystko pozostałe się stopi.


Do kolejki priorytetowej wkładam wszystkie elementy z tablicy S, ale z ujemnym znakiem, żeby wyciągać z niej najpierw te największe wartości z S.
Mam licznik dni, który będę zwiększała co iterację.
Do momentu gdy kolejka będzie pusta albo gdy różnica x-d - (już dodatniej) wartości wyciągniętej z kolejki i liczby dni, które minęły będzie większa od 0
zwiększam wartość res o x-d.
Zwracam res.

Złożoność algorytmu: O(nlogn)
"""

from egz1atesty import runtests
from queue import PriorityQueue


def snow(S):
    q = PriorityQueue()
    for i in range(len(S)):
        q.put(-S[i])

    d, x, res = -1, -1, 0
    while x - d >= 0:
        res += x - d
        x = -q.get()
        d += 1

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)

# def snow(S):
#     S.sort(reverse=True)
#     ct, day = 0, 0
#     for i in range(len(S)):
#         if S[i] - day <= 0: break
#         ct += S[i] - day
#         day += 1
#     return ct
#
#
# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(snow, all_tests=True)
