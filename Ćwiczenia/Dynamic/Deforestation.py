# Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las składa
# się z n drzew rosnących na pozycjach 0, ..., n-1. Dla każdego i {0, ..., n-1} znany
# jest zysk c[i], jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce
# uzyskać maksymalny zysk ze ścinanych drzew, ale prawo zabrania ścinania dwóch drzew
# pod rząd. Proszę zaproponować algorytm, dzięki któremu John znajdzie optymalny plan
# wycinki.

# f(i) - maksymalny zysk z drzew do indeksu i włącznie
# f(i) = max{f(i-1), f(i-2)+c[i]}
# f(0) = c[0]
# f(1) = max{c[0], c[1]}

# O(n)

def deforestation(C):
    n = len(C)
    DP = [0] * n
    DP[0] = C[0]
    DP[1] = max(C[0], C[1])
    for i in range(2, n):
        DP[i] = max(DP[i - 2] + C[i], DP[i - 1])
    return DP[-1]


C = [3, 4, 10, 4, 2, 8, 2, 5]
print(deforestation(C))

# największy zysk ze ścięcia drzewa od 0, do i włącznie
def f(i, F, G, C):
    if F[i] != -1:
        return F[i]
    F[i] = C[i] + g(i - 1, F, G, C)
    return F[i]

# największy zysk ze ścięcia drzewa od 0, do i bez i
def g(i, F, G, C):
    if G[i] != -1:
        return G[i]
    G[i] = max(f(i - 1, F, G, C), g(i - 1, F, G, C))
    return G[i]


def zadanie(C):
    n = len(C)
    F = [-1] * n
    G = [-1] * n
    F[0] = C[0]
    G[0] = 0
    return f(n-1, F, G, C)

print(zadanie(C))