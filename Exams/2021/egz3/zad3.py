# Dane jest pełne drzewo binarne T zawierające n wierzchołków. Każdy węzeł
# drzewa zawiera klucz będący liczbą całkowitą. Węzły drzewa numerujemy
# kolejnymi liczbami naturalnymi w ten sposób, że korzeń ma numer 1, jego
# synowie numery 2 i 3, następny poziom od lewej do prawej ma numery 4, 5, 6, 7, itd.
# Dany jest ciąg X zawierający m liczb naturalnych ze zbioru {1, ..., n}.
# Należy załóżyć, że m jest isotnie mnijsze niż n. Proszę zaimplementować funkcję:
#   def maxin( T, C )
#
# ktora zwraca maksymalny klucz spośród węzłów drzewa T o numerach wymienionych w X.
# Funkcja powinna być możliwie jak najszybsza - wychodząc z założenia, że m << n
# i powinna działać na stałej pamięci(poza pamięcią potrzebną n aprzechowywanie
# danych wejściowych). Proszę ozacować złożoność czasową algorytmu.


"""
Złożoność O(m log(n))
"""
from math import inf
from zad3testy import runtests


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.key = None


def baseconvert(number):
    if number == 0:
        return "0"
    a = ""
    hex = "01"
    while number > 0:
        a = hex[number % 2] + a
        number = number // 2
    return a


def find_value(T, curr, look_for, binary, idx):
    if T is None:
        return -inf
    if look_for == curr:
        return T.key
    if binary[idx] == "1":
        return find_value(T.right, (2 * curr) + 1, look_for, binary, idx + 1)
    return find_value(T.left, 2 * curr, look_for, binary, idx + 1)


def maxim(T, C):
    max_ = -inf
    for x in C:
        max_ = max(max_, find_value(T, 1, x, baseconvert(x), 1))
    if max_ != -inf:
        return max_
    return -1


runtests(maxim)
