import sys
sys.setrecursionlimit(1 << 25)

# 入力
H, W = map(int, sys.stdin.readline().split())
C = [list(sys.stdin.readline().strip()) for _ in range(H)]  # 文字列→リストに
# print(C)

# 移動ベクトル（対角8方向）
dxs = [1, 0, -1, 0, 1, 1, -1, -1]
dys = [0, 1, 0, -1, 1, -1, 1, -1]


def dfs(i, j):
    """
    DFS: 戻り値なし
    探索済みの `#` マスは `.` に塗りつぶすのみ
    """
    C[i][j] = '.'  # 訪問済みにする
    for d in range(8):
        ni = i + dxs[d]
        nj = j + dys[d]
        if 0 <= ni < H and 0 <= nj < W and C[ni][nj] == '#':
            dfs(ni, nj)  # グリッド範囲外でなく#なら再帰dfs


# 本体
count = 0
for i in range(H):
    for j in range(W):
        if C[i][j] == '.':
            continue
        dfs(i, j)
        count += 1  # dfsから帰ってきたら無条件で++

print(count)

"""
再帰DFS
ABC300Cのコード（けんちょん）をもとに自力で実装

#を見つけたらDFS。
訪問管理はグリッドを.で塗りつぶして行う。
DFSはひたすら連続する#を.で塗りつぶすのみ。
"""
