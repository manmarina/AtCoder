N = int(input())


def is_N_dollar(total):
    for i in range(total // 7 + 1):
        for j in range((total - 7 * i) // 4 + 1):
            if i * 7 + j * 4 == total:
                return True

    return False


print("Yes" if is_N_dollar(N) else "No")
