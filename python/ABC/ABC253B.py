H, W = map(int, input().split())
S = [input() for _ in range(H)]

# print(S)

pos = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            pos.append((i, j))

# print(pos)

(i1, j1), (i2, j2) = pos
ans = abs(i1 - i2) + abs(j1 - j2)
print(ans)
