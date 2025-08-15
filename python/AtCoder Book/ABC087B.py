A = int(input())
B = int(input())
C = int(input())
X = int(input())


def count_pattern(coin_500, coin_100, coin_50, answer):
    count = 0
    for i in range(coin_500 + 1):
        for j in range(coin_100 + 1):
            for k in range(coin_50 + 1):
                total = 500 * i + 100 * j + 50 * k
                # print(total)
                if total == answer:
                    count += 1
    return count


print(count_pattern(A, B, C, X))
