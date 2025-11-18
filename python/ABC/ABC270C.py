import sys
sys.setrecursionlimit(1 << 25)

N, X, Y = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
# print(G)

path = []


def dfs(n):
    path.append(n)
    if n == Y:
        print(*path)
        exit()

    for g in G[n]:
        if not visited[g]:
            visited[g] = True
            dfs(g)
            path.pop()
    return


# DFS
visited = [False] * (N + 1)
visited[X] = True
dfs(X)

"""
TLE & MLE
"""
