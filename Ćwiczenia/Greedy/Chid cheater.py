# Grupa m dzieci bawi się w układanie możliwie jak największej wieży. Każde dziecko ma
# klocki różnej wysokości. Pierwsze dziecko ma klocki o wysokościach w1, ..., wn, drugie
# dziecko klocki o wyskościach w1', ..., wn', itd. Dzieci właśnie poszły zjeść deser zanim
# ułożą swoje wieże, ale jedno dziecko zostało. Ma teraz jedyną okazję, żeby podebrać
# kilka klocków innym dzieciom tak, żeby jego wieża była najwyższa. Proszę podać algorytm
# rozwiązujący ten problem, który zabiera minimalną ilość klocków.
from queue import PriorityQueue


def build_tower(T):
    summary = []
    Queue = PriorityQueue()
    for i in range(len(T)):
        T[i].sort()
        summary.append(sum(T[i]))
        Queue.put((-summary[i], i))
    count = tower_height = 0
    while tower_height < max(summary):
        # index = summary.index(max(summary)) # zapamiętuję indeks największej dotychczas sumy
        _, index = Queue.get()  # zabieram ostatni klocek (po posortowaniu - z największą wartością)
        height = T[index].pop()
        tower_height += height
        summary[index] -= height
        Queue.put((-summary[index], index))
        count += 1
    return count


bricks = [[16, 1, 30, 9, 12],
          [36, 47, 8, 19, 1, 72],
          [6, 38, 22, 31, 37]]


print(build_tower(bricks))
