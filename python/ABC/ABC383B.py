H, W, D = map(int, input().split())
S = [input().strip() for _ in range(H)]

floors = [(i, j) for i in range(H) for j in range(W) if S[i][j] == '.']

ans = 0
for i in range(len(floors)):
    ax, ay = floors[i]
    for j in range(i + 1, len(floors)):
        bx, by = floors[j]
        cnt = 0
        for x in range(H):
            for y in range(W):
                if S[x][y] == '.' and (
                    abs(ax - x) + abs(ay - y) <= D or abs(bx - x) + abs(by - y) <= D
                ):  # すべての床を探索して、2つの加湿器どちらかが届くか判定
                    cnt += 1
        ans = max(ans, cnt)

print(ans)
