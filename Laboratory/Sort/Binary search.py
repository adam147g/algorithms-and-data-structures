# Proszę zaimplementować wyszukiwanie binarne w posortowanej tablicy,
# znajdujące najmniejszy indeks z daną wartością.

def binarySearch(T, i, j, x):
    if i > j:
        return None
    c = (i + j) // 2
    if T[c] == x:
        remember = binarySearch(T, i, c - 1, x)
        if remember is not None:
            return remember

        return c
    if T[c] > x:
        return binarySearch(T, i, c - 1, x)
    else:
        return binarySearch(T, c + 1, j, x)


T1 = [0, 1, 2, 3, 4, 5, 5, 5, 6]
for i in range(len(T1)):
    print(i, binarySearch(T1, 0, len(T1) - 1, T1[i]), "-", T1[i])
