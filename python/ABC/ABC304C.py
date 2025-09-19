from itertools import combinations
from math import hypot

N, D = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]
# print(XY)

# 感染距離内ならグラフに追加
G = [[] for _ in range(N + 1)]  # 1-index
for com1, com2 in combinations(enumerate(XY, 1), 2):
    i, (x1, y1) = com1
    j, (x2, y2) = com2
    if hypot(x1 - x2, y1 - y2) <= D:
        G[i].append(j)
        G[j].append(i)
# print(G)


# dfs開始準備
seen = [False] * (N + 1)  # 1-index

# dfs部分
seen[1] = True
stack = [1]
while stack:
    v = stack.pop()
    for nv in G[v]:
        if not seen[nv]:
            seen[nv] = True
            stack.append(nv)

# 結果出力
for infected in seen[1:]:
    print("Yes" if infected else "No")

"""
反復DFS
284Cのコードを参照して自力で実装。

この問題は、まず「グラフの問題だと思えるか」どうかが一つの壁になるかもしれないですね。

頂点：N人の人たち
辺：人 iと人 jとの距離が D以下であるとき、辺 (i,j)を張る
としたグラフを考えましょう。
こうして作ったグラフにおいて、各頂点が頂点 1 とつながっているかどうかを調べればよいです。
（けんちょん）
"""
