from collections import deque

H, W = map(int, input().split())
S = [list(input().strip()) for _ in range(H)]

dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)]

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            continue
        ans += 1

        # BFS で成分をつぶす
        S[i][j] = '.'  # 訪問済みマーキング（塗り替え）
        dq = deque([(i, j)])
        while dq:
            x, y = dq.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '#':
                    S[nx][ny] = '.'
                    dq.append((nx, ny))
print(ans)

"""
BFS
ポイントは「# の 8近傍での連結成分数を数える」ことです。
つまり上下左右+斜めを含む 8 方向でつながっている # の塊の個数を求めます。

典型手順（BFS 例）
    盤面を読み込む。
    まだ未訪問の # を見つけたら、そこから BFS（または DFS）を始めて同じ成分内の # をすべて訪問済みにする。
    BFS/DFS を 1 回始めるごとに答えを +1。
    全マスを走査して終了。
"""
