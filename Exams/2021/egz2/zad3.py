# Dane są lampki o numerach od 0 do n-1. Każda z nich może świecić na zielono, czerwono lub niebiesko
# i ma jeden przełącznik, który zmienia jej kolor (z zielonego na czerwony, z czerwonego na niebieski
# i z niebieskiego na zielony). Początkowo wszystkie lampki świecą na zielono. Operacja (a, b) oznacza
# "wciśnięcie przełącznika na każdej z lampek o numerach od a do b". Wykonanych będzie m operacji.
# Proszę napisać funkcję:
# def lamps(n, L):
#     ...
# która mając daną liczbę n lampek oraz listę L operacji (wykonywanych w podanej kolejności) zwraca
# ile maksymalnie lampek świeciło się na niebiesko (lampki są liczone na początku i po wykonaniu
# każdej operacji).


def lamps(n, T):
    all_lamps = [0] * n
    max_blue = actual_blue = 0
    for i in range(len(T)):
        for j in range(T[i][0], T[i][1] + 1):
            if all_lamps[j] == 0:
                all_lamps[j] = 1
            elif all_lamps[j] == 1:
                all_lamps[j] = 2
                actual_blue += 1
            elif all_lamps[j] == 2:
                all_lamps[j] = 0
                actual_blue -= 1
        max_blue = max(max_blue, actual_blue)
    return max_blue


T = [(0,4),(2,6),(1,6),(2,5),(7,9),(1,7),(1,7),(1,7)]
n = 10
print(lamps(n, T))
# ma wyjść 4

T = [(5, 6), (1, 1), (1, 4), (13, 13), (9, 11), (0, 2), (8, 9), (13, 14),
     (2, 5), (11, 14), (1, 1), (8, 10), (11, 11), (14, 15), (11, 12), (10, 11)]
n = 16
print(lamps(n, T))
# ma wyjść 7