# SKOŃCZONE
import time


def string_compare(P, T):
    def string_compare_rec(P, T, i, j):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        zamian = string_compare_rec(P, T, i - 1, j - 1) + (P[i] != T[j])
        wstawi = string_compare_rec(P, T, i, j - 1) + 1  # tekst T niezmienny, wstawienie do wzoru P
        usunie = string_compare_rec(P, T, i - 1, j) + 1  # usunieto liter ze wzoru P
        min_koszt = min(zamian, wstawi, usunie)
        return min_koszt

    return string_compare_rec(P, T, len(P) - 1, len(T) - 1)


def string_compare_PD(P, T):
    if P[0] != ' ':
        P = ' ' + P
    if T[0] != ' ':
        T = ' ' + T
    i = len(P)
    j = len(T)
    D = [[0 for _ in range(j)] for _ in range(i)]  # macierz ixj
    R = [['X' for _ in range(j)] for _ in range(i)]  # Rodzice I D S M
    for row in range(i):
        for column in range(j):
            if column == 0:
                D[row][column] = row
                R[row][column] = 'D'
            if row == 0:
                D[row][column] = column
                R[row][column] = 'I'
    R[0][0] = 'X'
    for ii in range(1, i):
        for jj in range(1, j):
            zamian = D[ii - 1][jj - 1] + (P[ii] != T[jj])
            wstawi = D[ii][jj - 1] + 1
            usunie = D[ii - 1][jj] + 1
            min_koszt = min(zamian, wstawi, usunie)
            D[ii][jj] = min_koszt
            if min_koszt == zamian and (P[ii] != T[jj]):
                R[ii][jj] = 'S'
            elif min_koszt == zamian and (P[ii] == T[jj]):
                R[ii][jj] = 'M'
            elif min_koszt == wstawi:
                R[ii][jj] = 'I'
            elif min_koszt == usunie:
                R[ii][jj] = 'D'
    min_koszt = D[i - 1][j - 1]
    # PATH RECONSTRUCTION
    i = len(P) - 1
    j = len(T) - 1
    elem = R[i][j]
    path = ""
    while elem != 'X':
        path += elem
        if elem in ['S', 'M']:
            i -= 1
            j -= 1
        elif elem == 'I':
            j -= 1
        elif elem == 'D':
            i -= 1
        elem = R[i][j]
    path = path[::-1]  # odwrócenie
    return min_koszt, path


def fit_substring(P, T):
    if P[0] != ' ':
        P = ' ' + P
    if T[0] != ' ':
        T = ' ' + T
    i = len(P)
    j = len(T)
    D = [[0 for val in range(j)] for _ in range(i)]  # macierz ixj
    for row in range(1, i):
        D[row][0] = row
    for ii in range(1, i):
        for jj in range(1, j):
            zamian = D[ii - 1][jj - 1] + (P[ii] != T[jj])
            wstawi = D[ii][jj - 1] + 1
            usunie = D[ii - 1][jj] + 1
            min_koszt = min(zamian, wstawi, usunie)
            D[ii][jj] = min_koszt
    i = len(P) - 1
    j = 0
    for k in range(1, len(T)):
        if D[i][k] < D[i][j]:
            j = k
    return j - i  # zamiana indeksu konca na poczatek

# Funkcja nws(P, T) oblicza najkrótszą ścieżkę edycji między ciągami znaków P i T, gdzie P jest wzorcem, a T jest tekstem.
# Algorytm wykorzystuje macierz D do przechowywania kosztów, a macierz parent do śledzenia operacji edycji
# (usunięcie, wstawienie, zamiana, dopasowanie). Algorytm przechodzi przez macierz D, obliczając minimalny koszt
# dla każdej komórki. Następnie tworzy ścieżkę edycji, przechodząc wstecz przez macierz parent, a wynikowy ciąg znaków
# jest tworzony na podstawie operacji zamiany i dopasowania.

def nws(P, T):  # P JEST EDYTOWANY, TEKST T NIERUSZANY
    if P[0] != ' ':
        P = ' ' + P
    if T[0] != ' ':
        T = ' ' + T
    i = len(P)
    j = len(T)
    D = [[0 for _ in range(j)] for _ in range(i)]  # macierz ixj
    R = [['X' for _ in range(j)] for _ in range(i)]  # Rodzice I D S M
    for row in range(i):
        for column in range(j):
            if column == 0:
                D[row][column] = row
                R[row][column] = 'D'
            if row == 0:
                D[row][column] = column
                R[row][column] = 'I'
    R[0][0] = 'X'
    for ii in range(1, i):
        for jj in range(1, j):
            zamian = D[ii - 1][jj - 1] + (float('inf') if P[ii] != T[jj] else 0)
            wstawi = D[ii][jj - 1] + 1
            usunie = D[ii - 1][jj] + 1
            min_koszt = min(zamian, wstawi, usunie)
            D[ii][jj] = min_koszt
            if min_koszt == zamian and (P[ii] != T[jj]):
                R[ii][jj] = 'S'
            elif min_koszt == zamian and (P[ii] == T[jj]):
                R[ii][jj] = 'M'
            elif min_koszt == wstawi:
                R[ii][jj] = 'I'
            elif min_koszt == usunie:
                R[ii][jj] = 'D'
                # PATH RECONSTRUCTION
    i = len(P) - 1
    j = len(T) - 1
    elem = R[i][j]
    path = ""
    while elem != 'X':
        path += elem
        if elem in ['S', 'M']:
            i -= 1
            j -= 1
        elif elem == 'I':
            j -= 1
        elif elem == 'D':
            i -= 1
        elem = R[i][j]
    path = path[::-1]  # odwrócenie
    result = ''
    index = 0
    for k in range(len(path)):
        if path[k] == 'D':
            index += 1
        elif path[k] == 'M':
            index += 1
            result += P[index]
    return result

# Funkcja npm(T) oblicza najkrótszą ścieżkę edycji między ciągiem znaków T a jego posortowaną wersją P.
# Algorytm jest podobny do nws(P, T), ale zaczyna od posortowanego wzorca P. Po obliczeniu macierzy D i parent,
# tworzona jest ścieżka edycji i wynikowy ciąg znaków jest generowany.


def npm(T):
    P = sorted(T)
    P = "".join(P)
    if P[0] != ' ':
        P = ' ' + P
    if T[0] != ' ':
        T = ' ' + T
    i = len(P)
    j = len(T)
    D = [[0 for val in range(j)] for _ in range(i)]  # macierz ixj
    R = [['X' for val in range(j)] for _ in range(i)]  # Rodzice I D S M
    for row in range(i):
        for column in range(j):
            if column == 0:
                D[row][column] = row
                R[row][column] = 'D'
            if row == 0:
                D[row][column] = column
                R[row][column] = 'I'
    R[0][0] = 'X'
    for ii in range(1, i):
        for jj in range(1, j):
            zamian = D[ii - 1][jj - 1] + (float('inf') if P[ii] != T[jj] else 0)
            wstawi = D[ii][jj - 1] + 1
            usunie = D[ii - 1][jj] + 1
            min_koszt = min(zamian, wstawi, usunie)
            D[ii][jj] = min_koszt
            if min_koszt == zamian and (P[ii] != T[jj]):
                R[ii][jj] = 'S'
            elif min_koszt == zamian and (P[ii] == T[jj]):
                R[ii][jj] = 'M'
            elif min_koszt == wstawi:
                R[ii][jj] = 'I'
            elif min_koszt == usunie:
                R[ii][jj] = 'D'
                # PATH RECONSTRUCTION
    i = len(P) - 1
    j = len(T) - 1
    elem = R[i][j]
    path = ""
    while elem != 'X':
        path += elem
        if elem in ['S', 'M']:
            i -= 1
            j -= 1
        elif elem == 'I':
            j -= 1
        elif elem == 'D':
            i -= 1
        elem = R[i][j]
    path = path[::-1]  # odwrócenie
    result = ''
    index = 0
    for k in range(len(path)):
        if path[k] == 'D':
            index += 1
        elif path[k] == 'M':
            index += 1
            result += P[index]
    return result


def main():
    TESTS = [("kot","pies"),("democrat","republicanic"),("ten autobus","tamten autokar"),("traktat","traktor")]
    for test in TESTS:
        print('\nWersja rekurencyjna dla {0} i {1}'.format(test[0],test[1]))
        t_start = time.perf_counter()
        result = string_compare(test[0],test[1])
        t_stop = time.perf_counter()
        print('Liczba operacji: {}'.format(result))
        print("Czas obliczeń:", "{:.7f}s".format(t_stop - t_start))

        print('\nWersja PD dla {0} i {1}'.format(test[0],test[1]))
        t_start = time.perf_counter()
        result = string_compare_PD(test[0],test[1])
        t_stop = time.perf_counter()
        print('Liczba operacji: {}'.format(result))
        print("Czas obliczeń:", "{:.7f}s".format(t_stop - t_start))


    print("fit_substring")
    print(fit_substring('bin', 'mokeyssbanana'))
    print(nws('democrat', 'republican'))
    print(npm('243517698'))



if __name__ == '__main__':
    main()
