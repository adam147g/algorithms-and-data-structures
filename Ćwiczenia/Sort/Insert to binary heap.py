# Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego.
# zakładamy, że kopiec jest poprawny

def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2

def insert(T, key, n):
    T.append(key)
    # T[n + 1] = key
    i = n + 1
    while i > 0 and T[i] > T[parent(i)]:
        T[i], T[parent(i)] = T[parent(i)], T[i]
        i = parent(i)


T = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
insert(T, 10, len(T)-1)
print(T)