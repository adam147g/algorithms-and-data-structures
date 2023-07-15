# Dany jest zbiór przedziałów domkniętych I = {[a1, b1], ..., [an, bn]} gdzie każdy przedział zaczyna
# się i kończy na liczbie naturalnej (wliczając 0). Dane są także dwie liczby naturalne x i y. Dwa
# przedziały można skleić (czyli zamienić na przedziały będące ich sumą mnogościową) jeśli mają
# dokładnie jeden punkt wspólny. Jeśli pewne przedzoały można posklejać tak, że powstaje z nich
# przedział [x, y] to mówimy, że są przydatne. Proszę napisać funkcję:
# def intuse(I, x, y):
#     ...
# która zwraca listę numerów wszystkich przydatnych przedziałów. Zbiór I jest reprezentowany jako
# lista par opisujących przedziały. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.


def binary_search(T, x):
    l = 0
    r = len(T) - 1
    while l <= r:
        mid = (l + r) // 2
        if T[mid] == x:
            return mid
        elif T[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def dfs(graph, visited, u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, visited, v)


def intuse(I, x, y):
    T = []
    for i in range(len(I)):
        T.append(I[i][0])
        T.append(I[i][1])
    T.sort()
    print(T)

    vertices = [T[0]]
    idx = 0
    for i in range(1, len(T)):
        if T[i] != vertices[idx]:
            vertices.append(T[i])
            idx += 1
    print(vertices)

    result = []
    if binary_search(vertices, x) == -1 or binary_search(vertices, y) == -1:
        return result

    x_graph = [[] for _ in range(len(vertices))]
    y_graph = [[] for _ in range(len(vertices))]

    for i in range(len(I)):
        value_1 = binary_search(vertices, I[i][0])
        value_2 = binary_search(vertices, I[i][1])
        x_graph[value_1].append(value_2)
        y_graph[value_2].append(value_1)
    print('X_GRAPH', x_graph)
    print('Y_GRAPH', y_graph)
    x_visited = [False] * len(vertices)
    dfs(x_graph, x_visited, binary_search(vertices, x))
    y_visited = [False] * len(vertices)
    dfs(y_graph, y_visited, binary_search(vertices, y))

    for i in range(len(I)):
        value_1 = binary_search(vertices, I[i][0])
        value_2 = binary_search(vertices, I[i][1])
        if x_visited[value_1] and y_visited[value_2]:
            result.append(i)
    return result


print(1)
I = [[3, 4], [2, 5], [1, 3], [4, 6], [1, 4]]
x, y = 1, 6
print(I, x, y)
print(intuse(I, x, y))
"hint: [0,2,3,4]"
print("--------------------")
print(2)
I = [[3000000, 4000000], [2000000, 5000000], [1000000, 3000000], [4000000, 6000000], [1000000, 4000000]]
x, y = 1000000, 6000000
print(I, x, y)
print(intuse(I, x, y))
"hint: [0,2,3,4]"
print("--------------------")
print(3)
I = [(x, x + 3) for x in range(10)]
x, y = 0, 11
print(I, x, y)
print(intuse(I, x, y))
"hint: []"
print("--------------------")
print(4)
I = [(x, x + 3) for x in range(10)]
x, y = 0, 12
print(I, x, y)
print(intuse(I, x, y))
"hint: [0,3,6,9]"
