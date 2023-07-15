# John pracował cały dzień i zapisał na długim pasku papieru swoją ulubioną liczbę n składającą się z l cyfr.
# Niestety pasek okazał się tak długi, że nie zmieścił się na półce Johna. Rozwiązać
# problem, Jan postanowił podzielić pasek na dwie niepuste części, tak aby każda z nih zawierała
# dodatnia liczba całkowita bez wiodących zer. Następnie obliczy sumę dwóch liczb całkowitych
# i zapisz to na nowym pasku. John chce, aby wynikowa liczba całkowita była jak najmniejsza, ponieważ
# zwiększa szanse, że suma zmieści się na półce. Pomóż Johnowi zdecydować, co to jest
# minimalna suma, którą może uzyskać.
from math import inf


def split_a_number(l, n):
    min_sum = inf
    T = [-1, 0, 1]
    for i in range(len(T)):
        mid = l // 2 + T[i]
        while 0 < mid < l and n[mid] == '0':
            if T[i] == -1:
                mid -= 1
            else:
                mid += 1
        if 0 < mid < l:
            min_sum = min(min_sum, int(n[mid:]) + int(n[:mid]))
    return min_sum


l = 20
n = '67378957561978988538'
print(split_a_number(l, n))

# to samo, ale mniej "sprytnie", bardziej ogólnie, dla zrozumienia
def sum(l,n):
    min_sum = inf
    for i in range(len(n)):
        if 0<i<l:
            min_sum = min(min_sum, int(n[i:]) + int(n[:i]))
    return min_sum

print(sum(l,n))