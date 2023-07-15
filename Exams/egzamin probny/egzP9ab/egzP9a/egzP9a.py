from egzP9atesty import runtests


def UPDATE(T, idndex, val):
    T.set(idndex, val + T.get(idndex))
    while idndex // 2:
        idndex //= 2
        T.set(idndex, T.get(2 * idndex) + T.get(2 * idndex + 1))


def GETSUM(T, a, b):
    output = 0
    while b - a > 1:
        if a % 2 == 1:
            output += T.get(a)
            a += 1
        if b % 2 == 0:
            output += T.get(b)
            b -= 1
        a //= 2
        b //= 2
    if a != b:
        output += T.get(a) + T.get(b)
    else:
        output += T.get(a)
    return output


def ASD(T, memory, Q, n):
    output = 0
    index_set = n // 2
    for el in Q:
        if el[0] == 0:
            UPDATE(T, index_set + el[1], el[2])
        else:
            output += GETSUM(T, index_set + el[1], index_set + el[2])

    return output


# Podpowiedź. Format zadania jest dość nietypowy (także ze względu na sposób działania testów),
# w takiej formie żadne zadanie raczej nie powinno się pojawić na egzaminie. Zadanie ma na celu
# sprawdzenie zrozumienia struktury #### Drzewa Przedziałowego ####

runtests(ASD, all_tests=True)

#
#        0
#        1
#    0       0
#    2       3
#  0   0   0   0
#  4   5   6   7
# 0 0 0 0 0 0 0 0
# 8 9 A B C D E F
#
