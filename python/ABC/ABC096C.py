import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]
vis = [[False] * W for _ in range(H)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(i, j):
    vis[i][j] = True
    deg = 0  # 隣接する'#'の数
    for dx, dy in dirs:
        ni, nj = i + dx, j + dy
        if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '#':
            deg += 1
            if not vis[ni][nj]:
                dfs(ni, nj)
    # 自分自身が孤立していたらNG（子の戻り値は見ない）
    if deg == 0:
        raise SystemExit("No")


for i in range(H):
    for j in range(W):
        if S[i][j] == '#' and not vis[i][j]:
            dfs(i, j)
print("Yes")


"""
再帰DFS版
むりやりDFSで実装したが、今回の問題では、'#'が孤立かどうかを判定できれば十分。
DFSを再帰呼び出しする前に孤立かどうか判断できてしまうので、
DFSで'#'に隣接する#をどんどんdfsで探索する意義がない。

なぜ今回はDFSがいらない？
    孤立かどうかは、そのマスの周囲4マスだけ見れば決まる（局所判定）。
    DFSで子へ進んだ時点で、子には少なくとも“親”という隣接 # が1つあるので、
    子が「孤立」と判定されることはない（孤立が起きるのは成分サイズ1=根だけ）。
    計算量も局所チェック O(HW) とDFS O(HW) は同程度で、優位性がない。
"""
