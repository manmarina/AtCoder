X, K = map(int, input().split())

for i in range(K):
    base = 10**(i + 1)
    X = (X + base // 2) // base * base

print(X)
