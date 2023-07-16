from math import inf

def dfs_recursive_dict(G, v):
    flag = [True]

    max_ = -inf
    for val_tab in G.values():
        for val in val_tab:
            if val > max_:
                max_ = val

    visitings = [False] * (max_ + 1)

    def dfs_dict(u, G, visitings, flag):
        visitings[u] +=1
        if u in G:
            for v in G[u]:
                if not visitings[v]==3:
                    if visitings[u]==visitings[v]==2:
                        flag[0] = False
                    else:
                        dfs_dict(v, G, visitings, flag)

        return flag[0]

    return dfs_dict(v, G, visitings, flag)

def is_acyclic_dict(G):
    for i in G:
        if not dfs_recursive_dict(G,i):
            return False
    return True
print()

def dfs_recursive_list(G, v):
    flag = [True]
    visitings = [0] * (len(G) + 1)

    def dfs_list(u, G, visitings, flag):
        visitings[u] +=1
        for v in G[u]:
            if not visitings[v]==3:
                if visitings[u]==visitings[v]==2:
                    flag[0] = False
                else:
                    dfs_list(v, G, visitings, flag)

        return flag[0]

    return dfs_list(v, G, visitings, flag)


def is_acyclic_list(G):
    G_copy = make_graph(G)
    for i in range(len(G_copy)):
        if not dfs_recursive_list(G_copy,i):
            return False
    return True


def make_graph(G):
    max_ = -inf
    for val_tab in G.values():
        for val in val_tab:
            if val > max_:
                max_ = val
    G_copy = [[] for _ in range(max_ + 1)]
    for key in G:
        G_copy[key] = G[key]
    return G_copy



G_1 = {1: [2, 3], 3: [4]}
print(is_acyclic_dict(G_1))
print(is_acyclic_list(G_1))
print("------------")
G_2 = {1: [2], 2: [3], 3: [1]}
print(is_acyclic_dict(G_2))
print(is_acyclic_list(G_2))
print("------------")
G_3 = {2: [1, 3], 3: [2]}
print(is_acyclic_dict(G_3))
print(is_acyclic_list(G_3))
print("------------")
G_4 = {1: [2], 3: [2, 4], 4: [3]}
print(is_acyclic_dict(G_4))
print(is_acyclic_list(G_4))
print("------------")
G_5 = {1: [2, 3], 2: [4], 3: [4]}
print(is_acyclic_dict(G_5))
print(is_acyclic_list(G_5))
print("------------")
G_6 = {1: [2, 3], 2: [3]}
print(is_acyclic_dict(G_6))
print(is_acyclic_list(G_6))
print("------------")
G_7 = {1: [2], 2: [3], 3: [1, 4]}
print(is_acyclic_dict(G_7))
print(is_acyclic_list(G_7))

