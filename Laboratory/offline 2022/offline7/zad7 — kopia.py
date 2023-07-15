from zad7testy import runtests
from math import inf


def dfs(G, north_south, visited, res, v, finish, left, step_1=0, step_2=1):
    # a = res, left, visited
    visited[v] = True
    left -= 1
    if left == 0:
        if north_south[v][0] and not north_south[v][1]:
            if finish in G[v][1]:
                res.append(v)
                return True
        elif north_south[v][1] and not north_south[v][0]:
            if finish in G[v][0]:
                res.append(v)
                return True
        return False

    if not north_south[v][step_1]:
        flag = None
        for u in G[v][step_1]:
            if not visited[u]:
                res.append(v)
                north_south[v][step_1] = True
                if v in G[u][0]:
                    north_south[u][0] = True
                    flag = 0
                elif v in G[u][1]:
                    north_south[u][1] = True
                    flag = 1

                if dfs(G, north_south, visited, res, u, finish, left):
                    return True

                res.remove(v)
                north_south[v][step_1] = False
                if flag != None:
                    north_south[u][flag] = False
        visited[v] = False
        # left += 1
        return False

    if not north_south[v][step_2]:
        flag = None
        for u in G[v][step_2]:
            if not visited[u]:
                res.append(v)
                north_south[v][step_2] = True
                if v in G[u][0]:
                    north_south[u][0] = True
                    flag = 0
                elif v in G[u][1]:
                    north_south[u][1] = True
                    flag = 1
                if len(G[u][0]) < len(G[u][1]):
                    if dfs(G, north_south, visited, res, u, finish, left, 0, 1):
                        return True
                else:
                    if dfs(G, north_south, visited, res, u, finish, left, 1, 0):
                        return True
                res.remove(v)
                north_south[v][step_2] = False
                if flag != None:
                    north_south[u][flag] = False
        visited[v] = False
        # left += 1
        # return False

    return False


def droga(G):
    print(G)
    n = len(G)
    north_south = [[False, False] for _ in range(n)]
    visited = [False] * n
    res = []
    vertex = None
    ct = inf
    for i in range(n):
        if len(G[i][0]) < ct:
            ct = len(G[i][0])
            vertex = i, 0, 1
        if len(G[i][1]) < ct:
            ct = len(G[i][1])
            vertex = i, 1, 0
    # print(vertex, ct)
    if dfs(G, north_south, visited, res, vertex[0], vertex[0], n, vertex[1], vertex[2]):
        return res
    return None


runtests(droga, all_tests=True)
# print(droga(
#     [([1, 10], [2, 3, 4]), ([0, 10], [2, 5, 6]), ([1, 5, 6], [0, 3, 4]), ([0, 2, 4], [5, 7, 8]), ([0, 2, 3], [6, 7, 9]),
#      ([1, 2, 6], [3, 7, 8]), ([1, 2, 5], [4, 7, 9]), ([4, 6, 9], [3, 5, 8]), ([3, 5, 7], [9, 10]), ([4, 6, 7], [8, 10]),
#      ([0, 1], [8, 9])]
#     ))
