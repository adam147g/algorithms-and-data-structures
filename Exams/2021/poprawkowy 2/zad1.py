# Paweł Konop

# Liniowo znajdujemy współrzędne przecięcia (czyli największą współrzędną x
# z lewej strony (max_left) i najmniejszą z prawej (min_right), oraz najmniejszą
# górną współrzędną (min_up) i największą dolną (max_down) (w ten sposób znajdziemy
# najmniejszy prostokąt zawierający się we wszytskich pozostałych))
# zapisujemy też pierwszą mniejszą lub równą od lewej na osi OX (prev_max_left),
# pierwszą większą lub równą prawej na OX (prev_min_right) i analogicznie w osi pionowej
# Zapisuje pole przecięcia (o ile przecięcie istnieje, jeżeli nie pole równe jest 0),
# a następne przechodzę po wszystkich prostokątach
# Jeżeli któraś ze współrzędnych prostokąta jest współrzędną najmniejszego przecięcia
# to liczę pole nowego przecięcia, zamieniając współrzędne przecięcia na
# te współrzędne prawie graniczne (prev_...) (jakby usuwając dany prostokąt z pola
# przecięcia). Wybieram ten prostokąt, którego usunięcie pozostawi największe pole p

from zad1testy import runtests
from math import inf


def rect(D):
    max_left = -inf
    prev_max_left = -inf
    min_right = inf
    prev_min_right = inf
    max_down = -inf
    prev_max_down = -inf
    min_up = inf
    prev_min_up = inf

    for x1, y1, x2, y2 in D:
        if x1 > max_left:
            prev_max_left = max_left
            max_left = x1
        elif x1 > prev_max_left:
            prev_max_left = x1
        if x2 < min_right:
            prev_min_right = min_right
            min_right = x2
        elif x2 < prev_min_right:
            prev_min_right = x2
        if y1 > max_down:
            prev_max_down = max_down
            max_down = y1
        elif y1 > prev_max_down:
            prev_max_down = y1
        if y2 < min_up:
            prev_min_up = min_up
            min_up = y2
        elif y2 < prev_min_up:
            prev_min_up = y2

    best_rect = None
    if max_left > min_right or max_down > min_up:
        area = 0
    else:
        area = (min_right - max_left) * (min_up - max_down)

    n = len(D)

    for i in range(n):
        x1, y1, x2, y2 = D[i]
        new_x1 = max_left
        if x1 == max_left:
            new_x1 = prev_max_left

        new_x2 = min_right
        if x2 == min_right:
            new_x2 = prev_min_right

        new_y1 = max_down
        if y1 == max_down:
            new_y1 = prev_max_down

        new_y2 = min_up
        if y2 == min_up:
            new_y2 = prev_min_up

        if new_x1 > new_x2 or new_y1 > new_y2:
            new_area = 0
        else:
            new_area = (new_x2 - new_x1) * (new_y2 - new_y1)

        if best_rect is None and new_area == area:
            best_rect = i
        if new_area > area:
            area = new_area
            best_rect = i

    return best_rect


# D = [(2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7), (1, 1, 2, 2)]

runtests(rect)
