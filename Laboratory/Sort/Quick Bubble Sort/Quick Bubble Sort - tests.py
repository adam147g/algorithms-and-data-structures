from random import seed, randint
from time import perf_counter

seed(42)


def printing(t, f, again):
    sum = 0
    for _ in range(again):
        t_copy = t
        start = perf_counter()
        f(t_copy)
        stop = perf_counter()
        sum += stop - start
    print("Average time: ", sum / again)


def runtests(f, g):
    elements = 500
    t = []
    for i in range(elements):
        t.append(i)
    print("Input: ", t)
    print("Quicksort")
    printing(t, f, 500)
    print("Bubblesort")
    printing(t, g, 500)
    print("--------------")

    t.reverse()
    print("Input: ", t)
    print("Quick")
    printing(t, f, 500)
    print("Bubblesort")
    printing(t, g, 500)
    print("--------------")

    t = [1] * elements
    print("Input: ", t)
    print("Quick")
    printing(t, f, 500)
    print("Bubblesort")
    printing(t, g, 500)
    print("--------------")

    t = [randint(0, elements) for _ in range(elements)]
    print("Input: ", t)
    print("Quick")
    printing(t, f, 500)
    print("Bubblesort")
    printing(t, g, 500)
    print("--------------")
