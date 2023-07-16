from math import inf
from time import perf_counter

def dfs_recursive_list(G, v):
    visited = [False] * (len(G) + 1)
    result = [v]

    def dfs_list(u, G, visited, result):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                result.append(v)
                dfs_list(v, G, visited, result)

    dfs_list(v, G, visited, result)
    return result


def dfs_recursive_dict(G, s):
    visited = [False] * len(G)
    result = [s]

    def dfs_dict(s, G, visited, result):
        visited[s - 1] = True
        for u in G[s]:
            if not visited[u - 1]:
                result.append(u)
                dfs_dict(u, G, visited, result)

    dfs_dict(s, G, visited, result)
    return result


def dfs_iterative_dict(G, s):
    max_ = -inf
    for val_tab in G.values():
        for val in val_tab:
            if val > max_:
                max_ = val

    visited = [False] * (max_ + 1)
    parent = [None] * (max_ + 1)

    result = [s]
    visited[s] = True
    while len(result) != max_:
        flag = False
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                visited[u] = True
                result.append(u)
                s = u
                flag = True
                break
        if not flag:
            s = parent[s]

    return result


def dfs_iter_dict(G, s):
    max_ = -inf
    for val_tab in G.values():
        for val in val_tab:
            if val > max_:
                max_ = val

    visited = [False] * (max_ + 1)
    stack = [s]

    result = [s]
    visited[s] = True
    while len(stack) != 0:
        for i in range(len(G[s])):
            if not visited[G[s][len(G[s]) - i - 1]]:
                stack.append(G[s][len(G[s]) - i - 1])
        s = stack.pop()
        if not visited[s]:
            visited[s] = True
            result.append(s)

    return result


G_dict = {
    1: [2, 3, 5],
    2: [1, 4, 6],
    3: [1, 7],
    4: [2],
    5: [1, 6],
    6: [2, 5],
    7: [3]}

a=perf_counter()
print(dfs_iterative_dict(G_dict, 1))
b=perf_counter()
print(dfs_iter_dict(G_dict, 1))
c=perf_counter()
print(b-a)
print(c-b)
# print(dfs_recursive_dict(G_dict, 1))

G_list = [
    [],
    [2, 3, 5],
    [1, 4, 6],
    [1, 7],
    [2],
    [1, 6],
    [2, 5],
    [3]]

# print(dfs_recursive_list(G_list, 1))
