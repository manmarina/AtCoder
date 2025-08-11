X, K = map(int, input().split())


def round_digit(num, digit):
    base = 10 ** (digit + 1)
    return (num + base // 2) // base * base


for i in range(K):
    X = round_digit(X, i)

print(X)
