# Znajdź długość najdłuższego wspólnego podciągu A[n], B[n].

# f(i,j) - długość najdłuższego wspólnego podciągu do znków A[i], B[j]
# f(i,0) = f(0,j) = 0
# f(i,j) = max(T[i-1][j], T[i][j-1]),
#                   lub
#          T[i-1][j-1]+1, gdy A[i-1] == B[j-1]

def longest_common_subsequence(A, B):
    T = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    return T[len(A)][len(B)]


A = [1, 5, 4, 5, 10, 2]
B = [1, 4, 5, 2, 0, 9]
print(longest_common_subsequence(A, B))
