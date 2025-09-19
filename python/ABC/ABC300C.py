import sys
sys.setrecursionlimit(1 << 25)

# 入力
H, W = map(int, sys.stdin.readline().split())
C = [list(sys.stdin.readline().strip()) for _ in range(H)]  # 文字列→リストに
# print(C)

# 移動ベクトル（対角4方向）
dxs = [1, 1, -1, -1]
dys = [1, -1, 1, -1]


def dfs(i, j):
    """
    DFS: '#' の個数を返す
    また、探索済みの `#` マスは `.` に塗りつぶす
    """
    cnt = 1
    C[i][j] = '.'  # 訪問済みにする
    for d in range(4):
        ni = i + dxs[d]
        nj = j + dys[d]
        if 0 <= ni < H and 0 <= nj < W and C[ni][nj] == '#':
            cnt += dfs(ni, nj)  # グリッド範囲外でなく#なら再帰dfs
    return cnt


# 本体
N = min(H, W)
res = [0] * N

for i in range(H):
    for j in range(W):
        if C[i][j] == '.':
            continue
        num = dfs(i, j)
        # レベルは '#' の個数を 4 で割った商 - 1
        # （元コードのロジックを忠実に移植）
        res[(num // 4) - 1] += 1

print(*res)

"""
再帰DFS
けんちょんの実装
グリッド上の「X字型（対角方向に伸びる十字）」の大きさを数える問題です。

#を見つけたらDFS。
訪問管理はグリッドを.で塗りつぶして行う。
ひとかたまりの#の数numが返ってくるので、num // 4 - 1をクロスのサイズとする。
"""
