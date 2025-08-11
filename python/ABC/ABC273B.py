X, K = map(int, input().split())


def round_digit(num, digit):
    base = 10 ** (digit + 1)
    return int(num / base + 0.5) * base


for i in range(K):
    X = round_digit(X, i)

print(X)
