H, W, D = map(int, input().split())
S = [input().strip() for _ in range(H)]

# 床座標だけ集める
P = [(i, j) for i in range(H) for j in range(W) if S[i][j] == '.']
F = len(P)

ans = 0
for a in range(F):
    ax, ay = P[a]
    for b in range(a + 1, F):          # 2台は別の床マスに置く前提
        bx, by = P[b]
        cnt = 0
        # 床マスを1つずつ見て、どちらかから距離≤Dならカウント
        for x, y in P:
            if abs(ax - x) + abs(ay - y) <= D or abs(bx - x) + \
                    abs(by - y) <= D:
                cnt += 1
        ans = max(ans, cnt)

print(ans)
