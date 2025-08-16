N = int(input())


def is_in_9by9(num):
    for i in range(1, 9 + 1):
        for j in range(1, 9 + 1):
            if N == i * j:
                return True

    return False


print("Yes" if is_in_9by9(N) else "No")
