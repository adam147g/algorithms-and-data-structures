'''
Adam Górka
Algorytm polega na wkładaniu do kolejki priorytetowej kolejnych plam, do których możemy dojechać mając
obecną ilość paliwa w baku, wyciąganiu największej plamy ropy, do której możemy dojechać
i zapisywaniu jej do listy "result".
Te czynność wykonujemy, dopóki nie będziemy w stanie dojechać do miasta B.
Gdy to nastąpi - sortujemy listę "result" i zwracamy ją jako wynik.
'''

from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    n = len(T)
    if T[0] >= n - 1:
        return [0]
    Queue = PriorityQueue()
    result = []
    i = 1
    j = 0
    Queue.put((-T[0], 0))
    while not Queue.empty():
        fuel, idx = Queue.get()
        result.append(idx)
        j -= fuel
        if j < n - 1:
            while i <= j:
                if T[i] != 0:
                    Queue.put((-T[i], i))
                i += 1
        else:
            return sorted(result)
    return None

runtests(plan, all_tests=True)
