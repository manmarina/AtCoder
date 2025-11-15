import sys
# 再帰呼び出しの深さの上限を 120000 に設定
# これがないとRE
sys.setrecursionlimit(120000)

N, M = map(int, input().split())

# 　隣接リストを作成
G = [[] for _ in range(N + 1)]  # 1-indexed
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
# print(G)


def dfs(n):
    for g in G[n]:
        if not visited[g]:
            visited[g] = True
            dfs(g)
    return


# DFS
ans = 0
for i in range(1, N + 1):  # 1~Nのすべてをスタート地点にしてDFS
    visited = [False] * (N + 1)
    visited[i] = True
    dfs(i)
    # print(visited)

    ans += visited.count(True)  # visitedになった数がiをスタートにした時のゴールの数

print(ans)

"""
DFS（深さ優先探索）
再帰DFSテンプレを使用。
すべてのスタート地点からdfsして、visitedになった数の総和が答え。

https://atcoder.jp/contests/abc204/tasks/abc204_c
"""
