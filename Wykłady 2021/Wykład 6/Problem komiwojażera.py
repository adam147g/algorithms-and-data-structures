# Problem komiwojżera
# Dane: C = {0, ..., n-1} - zbiór miast
#       d: CxC -> R       - odległości między miastami
# Zadanie:
# Znaleźć taką kolejność odwiedzania miast, że startujemy
# w 0, każde miasto odwiedzamy jednokrotnie (nie licząc 0),
# kończymy w mieście 0 i suma pokonanych odległości
# jest minimalna.

'''
1) Próbujemy wszystkich możliwości - O*(n!)
2) Algorytm dynamiczny
    f(X,i) = koszt najkrótszej ścieżki startującej w mieście 0,
             przebiegającej wszystkie miasta z X i nic więcej,
             i kończąca w mieście i
    X - zbiór miast, zawierający 0 oraz i

    Rozwiązanie:  min f(C,i) + d(i,0)
                 i!=0            ^^ -koszt przejechania od i do 0

    Rekurencja:
    f(X,i) =   min  f(X-{i},j) + d(j,i)
              j!=i
        j należy do X-{0}

    O( (2^n) * (n^2) )
'''