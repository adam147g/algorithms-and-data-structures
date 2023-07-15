# Kaja Dudek
# Używam Dijkstry, a komnaty traktuję jak graf - drzwi to krawędzie. Sprawdzając, czy mogę wejśc do komnaty sprawdzam,
# czy ilość sztabek, którą aktualnie posiadam + ilość sztabek w skrzyni byłaby wystarczająca, aby wejść do rozpatrywanej komnaty
# jeśli tak, to zostawiam odpowiednia ilość sztabek, a jeśli ilość sztabek w skrzyni już jest odpowiednia, to dobieram resztę.
# Złozoność O(n2logn)

from egz2btesty import runtests
from queue import PriorityQueue

def magic( C ):
    n = len(C)
    #
    # for i in range(n):
    #     print(C[i])

    D = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]

    Q = PriorityQueue()
    Q.put((0,C[0][0]))               # aktualna komnata, liczba sztabek złota
    C[0][0]=0

    while not Q.empty():
        current,dist = Q.get()

        for komnata in range(1,4):  # sprawdzamy dojście do każdej komnaty (sprawdzamy drzwi)
            where = C[current][komnata][1]

            if where != -1 and not visited[where]:    # jesli nie jest odwiedzona i jeśli nie prowadzi w przepaść

                curr_dist = dist

                # sprawdza, czy w ogóle można dojść z danej komnaty do kolejnej
                if C[current][komnata][0] <= dist + C[current][0]:

                    if C[current][0] < C[current][komnata][0]:
                        curr_dist -= C[current][komnata][0] - C[current][0]

                    # jeśli można i jest nadwyżka złota, to dobieramy sztabki
                    else:
                        curr_dist += min(C[current][0] - C[current][komnata][0],10)

                    # relaksacja
                    if D[where] < curr_dist:
                        D[where] = curr_dist
                        Q.put((where,D[where]))

        visited[current] = True
    print(D)
    return D[n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True)
