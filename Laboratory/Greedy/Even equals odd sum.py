'''
Opcja 1.
T = [1, 2, 2, 1]    swap = 0
           ^  ^
T = [1, 2, 1, 2]    swap = 1
        ^  ^
T = [1, 1, 2, 2]    swap = 2

Opcja 2.
T = [1, 2, 2, 1]    swap = 0
        ^     ^
T = [1, 1, 2, 2]    swap = 1
'''


def suit_and_tie_1(T):
    swaps = 0
    for i in range(0, len(T), 2):
        for j in range(i + 1, len(T)):
            if T[i] == T[j]:
                index = j
                while T[i] != T[i + 1]:
                    T[index], T[index - 1] = T[index - 1], T[index]
                    index -= 1
                    swaps += 1
    return swaps


T = [7, 6, 2, 1, 4, 3, 3, 7, 2, 6, 5, 1, 8, 5, 8, 4]
print(suit_and_tie_1(T))
print(T)

def suit_and_tie_2(T):
    swaps = 0
    for i in range(0, len(T), 2):
        for j in range(i + 1, len(T)):
            if T[i] == T[j]:
                if j!=i+1:
                    T[i+1], T[j] = T[j], T[i+1]
                    swaps += 1
                break
    return swaps

T = [7, 6, 2, 1, 4, 3, 3, 7, 2, 6, 5, 1, 8, 5, 8, 4]
print(suit_and_tie_2(T))
print(T)