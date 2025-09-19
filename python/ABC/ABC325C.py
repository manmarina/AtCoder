from collections import deque

H, W = map(int, input().split())
S = [list(input().strip()) for _ in range(H)]

# -1: 未訪問, 0以上: 訪問済み
dp = [[-1] * W for _ in range(H)]


def bfs(sx, sy):
    dp[sx][sy] = 0
    que = deque()
    que.append((sx, sy))
    while que:
        x, y = que.popleft()
        # 8方向配列（dirs）を用いずに8方向走査
        for x2 in range(x - 1, x + 2):
            for y2 in range(y - 1, y + 2):
                if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W:
                    continue
                if S[x2][y2] == '.' or dp[x2][y2] != -1:
                    continue
                dp[x2][y2] = dp[x][y] + 1
                que.append((x2, y2))


num = 0
for x in range(H):
    for y in range(W):
        if S[x][y] == '.' or dp[x][y] != -1:
            continue
        num += 1
        bfs(x, y)

# print(dp)
print(num)

"""
BFS（けんちょん）
ポイントは「# の 8近傍での連結成分数を数える」ことです。
つまり上下左右+斜めを含む 8 方向でつながっている # の塊の個数を求めます。

典型手順（BFS 例）
    盤面を読み込む。
    まだ未訪問の # を見つけたら、そこから BFS（または DFS）を始めて同じ成分内の # をすべて訪問済みにする。
    BFS/DFS を 1 回始めるごとに答えを +1。
    全マスを走査して終了。

visited配列(dp)を用いるのと、8方向配列(dirs)を用いてない点がチャッピーとの相違点
ほぼ同じロジックだが初回とチャッピーのほうが素直
"""
