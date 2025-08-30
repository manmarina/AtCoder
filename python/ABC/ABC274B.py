H, W = map(int, input().split())
C = [input() for _ in range(H)]

# print(C)

ans = []
for j in range(W):
    count = 0
    for i in range(H):
        if C[i][j] == '#':
            count += 1
    ans.append(count)
print(*ans)
