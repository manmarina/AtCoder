A, M, L, R = map(int, input().split())


def ceil_div(a, b):  # b>0
    return -((-a) // b)


def count_terms(A, M, L, R):  # 　L ≤ A + kM ≤ R　→　(L - A)/M ≤ k ≤ (R - A)/M
    k_min = ceil_div(L - A, M)   # 最小のk
    k_max = (R - A) // M         # 最大のk（floor）
    return max(0, k_max - k_min + 1)


print(count_terms(A, M, L, R))
