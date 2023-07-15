from egzP9btesty import runtests


def euler_cycle(G):
    stack = []
    result = []
    stack.append(0)
    while len(stack):
        u = stack[-1]
        if len(G[u]) == 0:
            result.append(u)
            stack.pop()
        else:
            stack.append(G[u][0])
            G[u].remove(G[u][0])
    result.reverse()
    return result


def dyrektor(G, R):
    for i in range(len(G)):
        for j in R[i]:
            G[i].remove(j)
    return euler_cycle(G)


runtests(dyrektor, all_tests=True)
