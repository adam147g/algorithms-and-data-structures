# Podajemy odległość, która jest odległością w km do pokonania przez samochód na jednej drodze.
# Podajemy również przystanki będące stacjami benzynowymi i całkowitą pojemnością zbiornika paliwa. Każda stacja
# jest zdefiniowany jako odległość od punktu 0, tj. s jest odległością między [i]-tą stacją
# i punkt 0. Znajdź algorytm, który obliczy minimalną liczbę uzupełnień (ilość
# stacje, na których samochód musi się zatrzymać) na całej trasie.


def car_fueling(distance, full_tank, stops):
    refills = 0
    current_refill = 0
    limit = full_tank
    while limit < distance:
        if current_refill >= len(stops) or stops[current_refill] > limit:
            return False
        while current_refill < len(stops) - 1 and stops[current_refill + 1] <= limit:
            current_refill += 1
        refills += 1
        limit = stops[current_refill] + full_tank
        current_refill += 1
    return refills


distance = 950
full_tank = 400
stops = [200, 375, 550, 750]
print(car_fueling(distance, full_tank, stops))