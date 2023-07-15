'''
Chcemy posortować tblicę rozmiaru n, zawierającą
liczby naturalne od 0 do k-1
'''


# np. dla k=5
# A=[1, 3, 2', 4, 0, 3, 2'']
#
#    0, 1, 2, 3, 4  - indeksy tablicy C
# C=[1, 1, 2, 2, 1] - tablica zawierająca ile jest danych liczb
# C=[1, 2, 4, 6, 7] - tablica zawierająca ile jest <= liczbie
#
#  Przegląda tablicę A od tyłu i wypełniam tablicę B
#    0, 1, 2, 3, 4, 5, 6 - indeksy B (od 0, do len(A))
# B=[ ,  ,  , 2'',  ,  ,  ]
# C=[1, 2, 3, 6, 7]

# B=[ ,  ,  , 2'',  , 3,  ]
# C=[1, 2, 3, 5, 7]

# B=[0,  ,  , 2'',  , 3,  ]
# C=[0, 2, 3, 5, 7]

# B=[0,  ,  , 2'',  , 3, 4]
# C=[0, 2, 3, 5, 6]

# B=[0,  , 2', 2'',  , 3, 4]
# C=[0, 2, 2, 5, 6]

# B=[0,  , 2', 2'', 3, 3, 4]
# C=[0, 2, 2, 4, 6]

# B=[0, 1, 2', 2'', 3, 3, 4]
# C=[0, 1, 2, 4, 6]
#
#  z tego wynika
# A=[0, 1, 2', 2'', 3, 3, 4]

# O(n+k)
def CountSort(A, k):
    C = [0] * k
    B = [0] * len(A)
    #    for x in A:
    #        C[x]+=1
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]


A = [1, 3, 2, 4, 0, 3, 2]
print(A)
print()
CountSort(A, 5)
print(A)
