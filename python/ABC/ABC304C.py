import sys
from collections import deque

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


def bfs(s: int, dist: list[int]) -> None:
    """
    頂点 s を始点とする BFS
    """
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for v2 in range(N):
            if dist[v2] != -1:
                continue
            if not is_connected(v, v2):
                continue
            dist[v2] = dist[v] + 1
            q.append(v2)


# 実行
dist = [-1] * N  # 再帰DFS版のseenと同じ役割
bfs(0, dist)
# print(dist)

# 出力
for v in range(N):
    print("Yes" if dist[v] != -1 else "No")

"""
BFS
けんちょん

この問題は、まず「グラフの問題だと思えるか」どうかが一つの壁になるかもしれないですね。

頂点：N人の人たち
辺：人 iと人 jとの距離が D以下であるとき、辺 (i,j)を張る
としたグラフを考えましょう。
こうして作ったグラフにおいて、各頂点が頂点 1 とつながっているかどうかを調べればよいです。
（けんちょん）

グラフを作成せず、bfsで直接感染距離かどうか計算する点が初回コードと異なる
（初回コードのほうが直感的）
再帰DFS版とはseen配列（bfsではdist配列）の値が異なるが、効用は同じ
"""
