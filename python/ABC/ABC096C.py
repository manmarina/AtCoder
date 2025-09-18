H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            continue
        ok = False
        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '#':
                ok = True
                break
        if not ok:  # 孤立
            print("No")
            exit()
print("Yes")

"""
カーソル系
DFSを使わない版

上下左右に隣り合う'#'があればよいので、
全探索して孤立する'#'が見つかったら早期終了

グリッド内の 各 # マスに、上下左右のいずれかへ隣接する # が少なくとも1つあるか をチェック。
1つでも“孤立した#（上下左右すべて.または外）”があれば No、なければ Yes。
斜めは 数えません。
"""
