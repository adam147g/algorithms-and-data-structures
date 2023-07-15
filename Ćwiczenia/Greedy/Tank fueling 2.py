# Tankowanie czołgu z cenami za paliwo
# L - pojemność baku czołgu (litry)
# Si - odległość stacji od punktu 0 (km)
# czołg spala 1 l/km
# Pi - cena za 1 listr na każdej stacji
# Czołg startuje z pełnym bakiem. Obliczyć minimalny koszt dotarcia do punktu końcowego:
#   a) na każdej stacji można tankować tyle ile się chce,
#   b) jeśli tankujemy to do pełna.
from math import inf


# a)


def tank_fueling_1(distance, fuel_tank, stops, prices):
    if fuel_tank < stops[0]:
        return False
    T = [-1] * (distance + 1)

    for i in range(len(stops)):
        T[stops[i]] = prices[i]
    print(T)  # tworzę trasę

    total_cost = 0
    for i in range(1, distance + 1 - fuel_tank):
        min_cost = inf
        for j in range(i, i + fuel_tank):
            if T[j] != -1:
                min_cost = min(min_cost, T[j])
        total_cost += min_cost

    return total_cost


# b)


def tank_fueling_2(distance, fuel_tank, stops, prices):
    F = [0] * len(stops)
    F[0] = prices[0] * stops[0]
    for i in range(1, len(stops)):
        j = i - 1
        minimum = F[j] + (stops[i] - stops[j]) * prices[i]
        while j >= 0 and fuel_tank >= stops[i] - stops[j]:
            minimum = min(minimum, F[j] + (stops[i] - stops[j]) * prices[i])
            j -= 1
        if j == -1 and fuel_tank >= stops[i]:  # ?
            minimum = min(minimum, prices[i] * stops[i])  # ?
        F[i] = minimum
    result = F[len(stops) - 1]
    for i in range(len(stops)):
        if distance - stops[i] <= fuel_tank:
            result = min(F[i], result)
    print(F)
    return result


stops = [1, 9, 15, 16, 17, 27, 28]
prices = [1, 100, 10, 15, 1, 30, 30]
distance = 30
fuel = 14
print(tank_fueling_1(distance, fuel, stops, prices))
print(tank_fueling_2(distance, fuel, stops, prices))
