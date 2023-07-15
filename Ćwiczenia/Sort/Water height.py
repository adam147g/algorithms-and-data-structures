# Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami. Pojemniki maja kształty prostokątów,
# rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest przez współrzędne lewego górnego
# rogu i prawego dolnego rogu. Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda
# rurami spłynęła do najniźszych pojemników). Proszę zaproponować algorytm Obliczający ile pojemników
# zostało w pełni zalanych.

def find_water(T, height):
    water = 0
    for i in range(len(T)):
        if height > T[i][1]:
            water += (T[i][1] - T[i][3])*(T[i][2] - T[i][0])
        elif height < T[i][3]:
            water += 0
        else:
            water += (height - T[i][3])*(T[i][2] - T[i][0])
    return water


def fill_containers(T, total_water):
    min_y = T[0][3]
    max_y = T[0][1]
    for i in range(1, len(T)):
        min_y = min(min_y, T[i][3])
        max_y = max(max_y, T[i][1])

    if find_water(T, max_y) < total_water:
        return len(T)

    flag = True
    height = (min_y + max_y) / 2
    # height = ceil((min_y + max_y) / 2) - szybciej, ale tylko dla naturalnych
    while flag:
        find = find_water(T, height)
        if abs(find - total_water) < 0.01:
            flag = False
        elif find < total_water:
            min_y = height
            height = (height + max_y) / 2
        else:
            max_y = height
            height = (height + min_y) / 2
    height += 0.01
    count = 0
    for i in range(len(T)):
        if height >= T[i][1]:
            count += 1
    return count


T = [(1, 5, 2, 3), (2, 4, 3, 1), (5, 6, 10, 4), (9, 7, 11, 0), (2, 8, 3, 3), (1, 2, 2, 1), (5, 3, 6, 1)]
for i in range(1, 40):
    print(fill_containers(T, i),"-",i)
