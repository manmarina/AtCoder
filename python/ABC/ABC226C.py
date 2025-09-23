N = int(input())
T = []  # 必要な時間
deps = []  # 必要な技番号 0-index
for i in range(N):
    tmp = list(map(int, input().split()))
    T.append(tmp[0])
    deps.append([x - 1 for x in tmp[2:]])  # 技番号を0-index化
print(T)
print(deps)


def dfs(v):
    if v in visited:
        return
    visited.add(v)
    for u in deps[v]:
        dfs(u)


visited = set()
dfs(N - 1)  # 最後の技から探索

ans = sum(T[i] for i in visited)
print(ans)


"""
グラフ探索（DFS/BFS）
チャッピー

最後に覚えたい技 N に必要な技だけを後ろからたどって集め、その技集合の Tiを合計すれば答え。
依存は Ai,j<i が保証→有向非巡回グラフ。

この問題は技Nが習得できることが保証されていますか？
各技の前提は必ず番号が小さい技だけです。したがって依存関係にサイクルは発生せず（DAG）、
N から前提をたどると必ず K=0 の技（特に i=1 は K1=0 が強制）に到達します。
ゆえに有限回で学習が完了します。
"""
