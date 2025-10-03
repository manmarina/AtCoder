import sys

input = sys.stdin.readline
H, W = map(int, input().split())
G = [list(input().strip()) for _ in range(H)]

# 方向マップ
dir2d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

visited = [[False]*W for _ in range(H)]
i, j = 0, 0  # 0-index の (0,0) がスタート

while True:
    if visited[i][j]:
        print(-1)
        break
    visited[i][j] = True

    di, dj = dir2d[G[i][j]]
    ni, nj = i + di, j + dj

    # 外に出るなら今の位置を 1-index で出力
    if not (0 <= ni < H and 0 <= nj < W):
        print(i+1, j+1)
        break

    i, j = ni, nj

"""
カーソル系（グリッド走査）
チャッピー

https://atcoder.jp/contests/abc265/tasks/abc265_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df4072-32d0-8323-8628-f71e776a97b0
"""
