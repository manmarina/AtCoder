N = int(input())
T = input()


def is_1122(t):
    lt = len(t)
    if lt % 2 == 0:  # ltは奇数である。
        return False

    pos = (lt + 1) // 2 - 1  # (lt + 1) // 2 文字目が '/' である。
    if t[pos] != '/':
        return False

    for i in range(pos):  # 1 文字目から (lt + 1) // 2 - 1 文字目までが 1 である。
        if t[i] != '1':
            return False

    for i in range(
        (lt + 1) // 2,
            lt):  # (lt + 1) // 2 + 1 文字目から lt 文字目までが 2 である。
        if t[i] != '2':
            return False

    return True


print(is_1122(T))
