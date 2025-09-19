import sys

input = sys.stdin.readline
N, M = map(int, input().split())
# グラフ作成
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
# print(G)

# dfs開始準備
seen = [False] * N
comp = 0

# 全ての頂点からスタート
for s in range(N):
    if seen[s]:
        continue
    comp += 1

    # dfs部分
    seen[s] = True
    stack = [s]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if not seen[nv]:
                seen[nv] = True
                stack.append(nv)

print(comp)

"""
反復DFS

「無向グラフの連結成分の個数」を数える問題です。
必要なテクは次のいずれか：
    DFS（深さ優先探索）
    BFS（幅優先探索）
    Union-Find（Disjoint Set Union, DSU）
"""
