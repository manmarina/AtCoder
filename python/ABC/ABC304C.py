import sys
sys.setrecursionlimit(1 << 25)

# 入力
N, D = map(int, sys.stdin.readline().split())
X = [0] * N
Y = [0] * N
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    X[i] = x
    Y[i] = y

D2 = D * D  # Dの二乗を前計算


def is_connected(i: int, j: int) -> bool:
    """
    頂点 i, j 間が連結かどうか
    """
    dx = X[i] - X[j]
    dy = Y[i] - Y[j]
    return dx * dx + dy * dy <= D2


# DFS
seen = [False] * N


def dfs(v: int) -> None:
    seen[v] = True
    for v2 in range(N):
        if seen[v2]:
            continue
        if is_connected(v, v2):
            dfs(v2)


# 実行
dfs(0)

# 出力
for v in range(N):
    print("Yes" if seen[v] else "No")

"""
再帰DFS
けんちょん

この問題は、まず「グラフの問題だと思えるか」どうかが一つの壁になるかもしれないですね。

頂点：N人の人たち
辺：人 iと人 jとの距離が D以下であるとき、辺 (i,j)を張る
としたグラフを考えましょう。
こうして作ったグラフにおいて、各頂点が頂点 1 とつながっているかどうかを調べればよいです。
（けんちょん）

グラフを作成せず、dfsで直接感染距離かどうか計算する点が初回コードと異なる
"""
