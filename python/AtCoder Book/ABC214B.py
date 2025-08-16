S, T = map(int, input().split())


def count_int(S, T):
    pool = set()
    for a in range(S + 1):
        for b in range(S + 1 - a):
            for c in range(S + 1 - a - b):
                if a + b + c <= S and a * b * c <= T:
                    pool.add((a, b, c))
                    # print(pool)
    return len(pool)


print(count_int(S, T))
