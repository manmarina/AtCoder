import sys
from collections import deque

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

# bfs開始準備
seen = [False] * N
comp = 0

# 全ての頂点からスタート
for s in range(N):
    if seen[s]:
        continue
    comp += 1

    # bfs部分
    seen[s] = True
    q = deque([s])
    while q:
        v = q.popleft()
        for nv in G[v]:
            if not seen[nv]:
                seen[nv] = True
                q.append(nv)

print(comp)

"""
BFS
(反復DFSとはスタック、キューの違いのみ）

「無向グラフの連結成分の個数」を数える問題です。
必要なテクは次のいずれか：
    DFS（深さ優先探索）
    BFS（幅優先探索）
    Union-Find（Disjoint Set Union, DSU）
"""
