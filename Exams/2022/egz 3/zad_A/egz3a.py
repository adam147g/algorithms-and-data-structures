# Adam Górka
# Wszystkie punkty (początki i końce przedziałów) wrzucam do osobnej tablicy, rozróżniając czy punkt był początkiem, czy
# końcem pewnego przedziału. Następnie podaną tablicę sortuję. Na samym końcu przechodzą ją liniowo i szukam takiego
# jej fragmentu, gdzie punkty będące początkami przedziałów występują obok siebie największą liczbę razy. Ich ilość
# jest rozwiązaniem zadania. Zachłanne podejście przedstawione tutaj zadziała poprawnie, ponieważ pewna ilość punktów
# rozpoczynających przedziały leżąca obok siebie oznacza, że żaden z tych przedziałów jeszcze się nie zakończył (punkty
# są posortowane) i powstanie konstrukcja o wysokości równej ilości tych przedziałów. Dopiero natrafienie na pewien
# punkt kończący przedział powoduje, że ilość śniegu może się zmniejszyć.
# Złożoność czasowa: O(n log n)
# Złożoność pamięciowa: O(n)

from egz3atesty import runtests


def snow( T, I ):
    n = len(I)
    arr = [(None, None)] * 2 * n
    ctr = 0
    for x, y in I:
        arr[ctr] = (x, 0)
        arr[ctr + 1] = (y, 1)
        ctr += 2
    arr.sort()
    solution, ctr = 0, 0
    for x in range(1, len(arr)):
        if arr[x-1][1] == 0:
            ctr += 1
        else:
            ctr -= 1
        solution = max(solution, ctr)
    return solution


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
