N, M = map(int, input().split())

# 8方向
dirx = [-1, -2, -2, -1, 1, 2, 2, 1]
diry = [-2, -1, 1, 2, 2, 1, -1, -2]

ng = set()  # 置けないマスを管理
for _ in range(M):  # すべてのコマを走査
    x, y = map(int, input().split())
    ng.add((x, y))  # コマのマスをngに追加

    for dx, dy in zip(dirx, diry):  # 8方向走査
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= N and 1 <= ny <= N:
            ng.add((nx, ny))  # 青いマスをngに追加
print(N * N - len(ng))  # 全マス目 - 置けないマス = 置けるマス

"""
カーソル系

Nの制約が大きいので(10^9)、2次元配列ではなくsetを利用。
コマの座標を取得してsetに格納。
コマが動ける位置の座標を計算してsetに格納。
マスの数から、セットに格納された座標の数（コマの位置 + 青の位置）を引いて答えを求める。

https://atcoder.jp/contests/abc377/tasks/abc377_c
"""
