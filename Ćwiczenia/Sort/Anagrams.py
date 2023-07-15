# Mamy dane dwa słowa a,b. Proszę podać algorytm sprawdzający czy są anagramami.
# kot, tok - anagramy
# kot, kat - nie anagramy
from math import inf
from random import randint


def check_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    max_, min_ = 0, inf
    for i in range(len(word1)):
        max_ = max(max_, ord(word1[i]), ord(word2[i]))
        min_ = min(min_, ord(word1[i]), ord(word2[i]))

    counters = [0] * (max_ - min_ + 1)

    for i in range(len(word1)):
        counters[ord(word1[i]) - min_] += 1
        counters[ord(word2[i]) - min_] -= 1

    for i in range(len(word1)):
        if counters[ord(word1[i]) - min_] != 0:
            return False
    return True


word1 = "lo/$x3%h121b"
word2 = "h1b12ox/$%3l"
word3 = "dafag ssrgeg"
print(check_anagrams(word1, word2))
print(check_anagrams(word1, word3))


def num(ch):
    return ord(ch) - ord('A')


# gdy dostajemy tablice c ze śmieciami

def anagrams(w1, w2, c):
    l_1 = len(w1)
    l_2 = len(w2)
    if l_2 != l_1:
        return False

    for i in range(l_1):
        c[num(w1[i])] = 0

    for i in range(l_1):
        c[num(w1[i])] += 1
        c[num(w2[i])] -= 1

    for i in w1:
        if c[num(i)] != 0:
            return False
    return True


c = []
for _ in range(ord('Z') + 2):
    c.append(randint(1, 1000))

print(anagrams(word1, word2, c))
print(anagrams(word1, word3, c))
