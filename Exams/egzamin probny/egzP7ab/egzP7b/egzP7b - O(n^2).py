from egzP7btesty import runtests


def ogrod(S, V):
    n = len(S)
    result = 0
    for i in range(n):
        curr = 0
        visited = [0 for _ in range(len(V))]
        for j in range(i, n):
            if visited[S[j] - 1] == 0:
                curr += V[S[j] - 1]
                if curr > result:
                    result = curr
            elif visited[S[j] - 1] == 1:
                curr -= V[S[j] - 1]
            visited[S[j] - 1] += 1
        if curr > result:
            result = curr
    return result


runtests(ogrod, all_tests=True)
