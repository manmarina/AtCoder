from collections import defaultdict
import sys
sys.setrecursionlimit(120000)

N = int(input())
G = defaultdict(list)  # 技i -> [必要な技] 1-indexed
T = [0] * (N + 1)  # 技i　-> 習得時間　1-indexed
for i in range(1, N + 1):  # 1-indexed
    t, _, *a = map(int, input().split())
    G[i] = a
    T[i] = t
# print(G)
# print(T)

ans = 0  # 習得時間の総和


def dfs(n):
    global ans
    ans += T[n]  # 習得時間を加算
    for g in G[n]:
        if not visited[g]:
            visited[g] = True
            dfs(g)
    return


# DFS
visited = [False] * (N + 1)
visited[N] = True
dfs(N)
# print(visited)

print(ans)  # 習得時間の総和を出力

"""
グラフ探索（DFS/BFS）
リトライ
再帰DFSテンプレートを使用。

https://atcoder.jp/contests/abc226/tasks/abc226_c
"""
