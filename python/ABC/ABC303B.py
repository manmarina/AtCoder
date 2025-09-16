N, M = map(int, input().split())
adj = [[False] * N for _ in range(N)]

for _ in range(M):
    A = list(map(int, input().split()))
    for i in range(N - 1):
        x, y = A[i] - 1, A[i + 1] - 1  # 0-index化
        adj[x][y] = adj[y][x] = True

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if not adj[i][j]:
            ans += 1
print(ans)

"""
無向グラフ
2次元配列（隣接表）を作成
隣接表の右上の領域のみカウントする
"""
