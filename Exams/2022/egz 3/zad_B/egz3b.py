# Adam Górka
# Algorytm polega na stworzeniu listy list DP, w której zapisywane są największe wartości liczby komnat,
# które przeszliśmy. Najpierw startujemy z 0,0 i wstawiamy do kolejki możliwe komnaty do których możemy się dostać.
# W tym kroku uwzględniamy, że nie możemy się cofać do komnaty, z której przyszliśmy.
# Po zabieraniu z kolejki kolejnych wartości sprawdzamy czy w DP jest wartość mniejsza, jęśli tak, to nadpisujemy ją
# i wykonujemy algorytm dalej.
# Algorytm sprawdza wszystkie możliwości, a dzięki temu, że możemy się poruszać tylko w prawo, dół i górę, wystarczy nie
# iść w górę, gdy z niej przyszliśmy, i nie iść w dół, gdy z niego przyszliśmy. Jest to spowodowane tym, że nie możemy
# iść ani w lewo, ani skoczyć o 2 komnaty w dół lub górę.
# Na końcu zwracamy najmniejszą wartość dla n-1, n-1

from egz3btesty import runtests
from collections import deque


# def f(x, y, was_x, was_y, moves, I, DP, n):
#     if DP[x][y] != -1:
#         return DP[x][y]
#     best = -1
#     for k in range(3):
#         x_ = x + moves[k][0]
#         y_ = y + moves[k][1]
#         if was_x == x_ and was_y == y_:
#             continue
#         if n>x_>-1 and n>y_>-1:
#             if I[x_][y_] != '#':
#                 best = max(best, f(x_, y_, x, y, moves, I, DP, n))
#     if best != -1:
#         DP[x][y] = best + 1
#     return DP[x][y]
#
#
# def maze(L):
#     n = len(L)
#     moves = [(1, 0), (-1, 0), (0, -1)]
#     DP = [[-1 for _ in range(n)] for _ in range(n)]
#     DP[0][0] = 0
#     return f(n - 1, n - 1, None, None, moves, L, DP, n)


# def maze(L):
#     n = len(L)
#     DP = [[-1 for _ in range(n)] for _ in range(n)]
#     moves = [(1, 0), (-1, 0), (0, 1)]
#     q = deque()
#     q.append((0, 0, 0, None, None))
#     while q:
#         dist, x, y, last_x, last_y = q.popleft()
#         if DP[x][y] < dist:
#             DP[x][y] = dist
#         for next_move in moves:
#             next_x = x + next_move[0]
#             next_y = y + next_move[1]
#             if next_x != last_x or next_y != last_y:
#                 if -1 < next_x < n and -1 < next_y < n:
#                     if L[next_x][next_y] != '#':
#                         q.append((dist + 1, next_x, next_y, x, y))
#     return DP[n - 1][n - 1]


# 0 - z dołu
# 1 - z góry
# 2 - z prawej

def f(row, col, value, direction, DP, I, n):
    if DP[row][col][direction] < value:
        DP[row][col][direction] = value
    if row == col == 0:
        return
    if direction == 0:
        if row - 1 > -1 and I[row - 1][col] != '#':
            f(row - 1, col, value + 1, 0, DP, I, n)
        if col - 1 > -1 and I[row][col - 1] != '#':
            f(row, col - 1, value + 1, 2, DP, I, n)
    if direction == 1:
        if row + 1 < n and I[row + 1][col] != '#':
            f(row + 1, col, value + 1, 1, DP, I, n)
        if col - 1 > -1 and I[row][col - 1] != '#':
            f(row, col - 1, value + 1, 2, DP, I, n)
    if direction == 2:
        if row - 1 > -1 and I[row - 1][col] != '#':
            f(row - 1, col, value + 1, 0, DP, I, n)
        if row + 1 < n and I[row + 1][col] != '#':
            f(row + 1, col, value + 1, 1, DP, I, n)
        if col - 1 > -1 and I[row][col - 1] != '#':
            f(row, col - 1, value + 1, 2, DP, I, n)


def maze(L):
    n = len(L)
    DP = [[[-1 for _ in range(3)] for _ in range(n)] for _ in range(n)]
    DP[n - 1][n - 1][0] = DP[n - 1][n - 1][1] = DP[n - 1][n - 1][2] = 0
    if L[n - 2][n - 1] != '#':
        f(n - 2, n - 1, 1, 0, DP, L, n)
    if L[n - 1][n - 2] != '#':
        f(n - 1, n - 2, 1, 2, DP, L, n)
    return max(DP[0][0][0], DP[0][0][1], DP[0][0][2])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
