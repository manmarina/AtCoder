H, W = map(int, input().split())

X = [0 for i in range(W)]
for i in range(H):
    C = input()
    for j in range(W):
        if C[j] == '#':
            X[j] += 1

print(*X)
