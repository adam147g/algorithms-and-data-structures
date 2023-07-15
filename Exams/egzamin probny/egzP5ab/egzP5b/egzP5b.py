from egzP5btesty import runtests


def articulation(G):
    time = 0
    n = len(G)
    # art_pts = 0
    ART = [0 for _ in range(n)]
    LOW = [None for _ in range(n)]
    D = [None for _ in range(n)]  # czas odwiedzenia

    def dfs(G, ART, LOW, D, v):
        nonlocal time
        children = 0

        time += 1
        LOW[v] = time
        D[v] = time
        for s in G[v]:
            if D[s] is None:
                children += 1
                dfs(G, ART, LOW, D, s)

                if LOW[s] >= D[v]:
                    ART[v] = 1
                LOW[v] = min(LOW[v], LOW[s])
            else:
                LOW[v] = min(LOW[v], D[s])
        return children

    for i in range(n):
        if D[i] is None:
            if dfs(G, ART, LOW, D, i) > 1:
                ART[i] = 1
            else:
                ART[i] = 0

    return sum(ART)


def koleje(B):
    n = len(B)
    max_vertex = 0
    T = []
    for i in range(n):
        if B[i][0] > B[i][1]:
            T.append((B[i][1], B[i][0]))
            if B[i][0] > max_vertex:
                max_vertex = B[i][0]
        else:
            T.append((B[i][0], B[i][1]))
            if B[i][1] > max_vertex:
                max_vertex = B[i][1]

    T.sort(key=lambda x: (x[0], x[1]))
    G = [[] for _ in range(max_vertex+1)]
    last = None
    for x in T:
        if last != x:
            last = x
            G[x[0]].append(x[1])
            G[x[1]].append(x[0])

    return articulation(G)


runtests(koleje, all_tests=True)
