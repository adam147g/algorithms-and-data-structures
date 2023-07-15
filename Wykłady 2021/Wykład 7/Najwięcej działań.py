# Biorąc pod uwagę n czynności z ich czasem rozpoczęcia i zakończenia (początek, zakończenie).
# Znaleźć zestaw, który ma maksymalną liczbę niekonfliktowych działań, które można wykonać
# w jednym przedziale czasowym.

def activity_selection(T):
    T.sort(key=lambda x: x[1])
    A = [T[0]]
    index = 0
    for i in range(1, len(T)):
        if T[i][0] >= A[index][1]:
            A.append(T[i])
            index += 1
    return A


T = [(8, 12), (6, 10), (8, 11), (5, 7), (12, 16), (5, 9),
     (3, 5), (0, 6), (1, 4), (2, 14), (3, 9)]
print(activity_selection(T))