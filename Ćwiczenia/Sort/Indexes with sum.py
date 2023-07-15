# Tablica A, n elemenotwa, posortowana, x - liczba
# Proszę podać algorytm znajdujący indeksy i oraz j takie że
# A[i] + A[j] = x (lub ich nie ma)


def find_sum(T, x):
    i = 0
    j = len(T) - 1
    while i <= j:
        if T[i] + T[j] == x:
            if i != j:   return i, j
            else:   return None
        elif T[i] + T[j] > x:
            j -= 1
        else:
            i += 1

T = [1, 3, 3, 5, 6, 7, 9, 9, 10, 12]
for i in range(23):
    print(find_sum(T, i), i)