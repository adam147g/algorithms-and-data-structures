from egzP5atesty import runtests


def inwestor(T):
    n = len(T)
    stack = [-1, 0]
    area = 0
    LS = [-1 for _ in range(n)]
    RS = [n for _ in range(n)]

    for i in range(1, n):
        while stack[-1] != -1 and T[stack[-1]] > T[i]:
            RS[stack[-1]] = i
            stack.pop()
        if T[i] == T[i - 1]:
            LS[i] = LS[i - 1]
        else:
            LS[i] = stack[-1]
        stack.append(i)

    for j in range(n):
        if T[j] * (RS[j] - LS[j] - 1) > area:
            area = T[j] * (RS[j] - LS[j] - 1)

    return area


runtests(inwestor, all_tests=True)
