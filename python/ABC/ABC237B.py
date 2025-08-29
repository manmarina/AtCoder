H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

AT = [[0] * H for _ in range(W)]
for i in range(H):
    for j in range(W):
        AT[j][i] = A[i][j]

for row in AT:
    print(*row)
