import sys
from collections import deque

# 入力
H, W = map(int, sys.stdin.readline().split())
C = [list(sys.stdin.readline().strip()) for _ in range(H)]  # 文字列→リストに
# print(C)

# 移動ベクトル（対角4方向）
dxs = [1, 1, -1, -1]
dys = [1, -1, 1, -1]


def bfs(si, sj):
    """
    BFS: '#' の個数を返す
    また、探索済みの `#` マスは `.` に塗りつぶす
    """
    C[si][sj] = '.'
    q = deque([(si, sj)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and C[nx][ny] == '#':
                C[nx][ny] = '.'
                q.append((nx, ny))
                cnt += 1
    return cnt


# 本体
N = min(H, W)
res = [0] * N

for i in range(H):
    for j in range(W):
        if C[i][j] == '.':
            continue
        num = bfs(i, j)
        # レベルは '#' の個数を 4 で割った商 - 1
        # （元コードのロジックを忠実に移植）
        res[(num // 4) - 1] += 1

print(*res)

"""
BFS
けんちょんの実装
グリッド上の「X字型（対角方向に伸びる十字）」の大きさを数える問題です。

#を見つけたらDFS。
訪問管理はグリッドを.で塗りつぶして行う。
ひとかたまりの#の数numが返ってくるので、num // 4 - 1をクロスのサイズとする。
"""
