N, Y = map(int, input().split())


def otoshidama(total_count, total_yen):
    for i in range(total_count + 1):
        for j in range(total_count + 1 - i):
            k = total_count - i - j
            if 10000 * i + 5000 * j + 1000 * k == total_yen:
                return i, j, k
    return -1, -1, -1


print(*otoshidama(N, Y))
