from egzP7btesty import runtests


def TreeUpdate(lo, hi, change, tree_sum, tree_max, TREE_SIZE):
    index_lo = lo + TREE_SIZE
    index_hi = hi + TREE_SIZE

    if lo > hi: return

    tree_sum[index_lo] += change
    tree_max[index_lo] += change

    if index_lo != index_hi:
        tree_sum[index_hi] += change
        tree_max[index_hi] += change

    while index_lo // 2 != index_hi // 2:
        if index_lo % 2 == 0:
            tree_sum[index_lo + 1] += change
            tree_max[index_lo + 1] += change
        if index_hi % 2 == 1:
            tree_sum[index_hi - 1] += change
            tree_max[index_hi - 1] += change

        index_lo //= 2
        index_hi //= 2

        tree_max[index_lo] = max(tree_max[2 * index_lo], tree_max[2 * index_lo + 1]) + tree_sum[index_lo]
        tree_max[index_hi] = max(tree_max[2 * index_hi], tree_max[2 * index_hi + 1]) + tree_sum[index_hi]

    while index_lo != 0:
        index_lo //= 2
        tree_max[index_lo] = max(tree_max[2 * index_lo], tree_max[2 * index_lo + 1]) + tree_sum[index_lo]


def TreeMax(lo, hi, tree_sum, tree_max, TREE_SIZE):
    index_lo = lo + TREE_SIZE
    index_hi = hi + TREE_SIZE
    output = 0
    lo_res = tree_max[index_lo]
    hi_res = tree_max[index_hi]

    while index_lo // 2 != index_hi // 2:
        if index_lo % 2 == 0:
            lo_res = max(lo_res, tree_max[index_lo + 1])
        if index_hi % 2 == 1:
            hi_res = max(hi_res, tree_max[index_hi - 1])

        index_lo //= 2
        index_hi //= 2

        lo_res += tree_sum[index_lo]
        hi_res += tree_sum[index_hi]

    output = max(lo_res, hi_res)

    while index_lo != 0:
        index_lo //= 2
        output += tree_sum[index_lo]

    return output


def sol(S, V):
    n, m = len(S), len(V)
    TREE_SIZE = 1
    while TREE_SIZE < n:
        TREE_SIZE <<= 1
    TREE_SIZE -= 1

    tree_sum = [0 for _ in range(2 * TREE_SIZE)]
    tree_max = [0 for _ in range(2 * TREE_SIZE)]

    for i in range(n):
        S[i] -= 1

    ptr_el = [n for _ in range(m)]
    next_same = [0 for _ in range(n + 1)]
    next_same[n] = n

    for i in range(n - 1, -1, -1):
        next_same[i] = ptr_el[S[i]]
        ptr_el[S[i]] = i

    cnt_val = [0 for _ in range(n)]
    cur_res = 0
    for i in range(n):
        if cnt_val[S[i]] == 0:
            cur_res += V[S[i]]
        if cnt_val[S[i]] == 1:
            cur_res -= V[S[i]]
        cnt_val[S[i]] += 1

        TreeUpdate(i, i, cur_res, tree_sum, tree_max, TREE_SIZE)

    output = TreeMax(0, n - 1, tree_sum, tree_max, TREE_SIZE)

    for i in range(n):
        TreeUpdate(i, next_same[i] - 1, -V[S[i]], tree_sum, tree_max, TREE_SIZE)
        TreeUpdate(next_same[i], next_same[next_same[i]] - 1, V[S[i]], tree_sum, tree_max, TREE_SIZE)
        output = max(output, TreeMax(0, n - 1, tree_sum, tree_max, TREE_SIZE))

    return output


runtests(sol, all_tests=False)
