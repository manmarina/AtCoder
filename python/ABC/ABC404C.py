from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# まず M==N でなければ即アウト
if M != N:
    print("No")
    exit()

G = [[] for _ in range(N)]
deg = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    deg[a] += 1
    deg[b] += 1

# 各頂点の次数がすべて2か確認
for d in deg:
    if d != 2:
        print("No")
        exit()

# 連結性チェック（BFS or DFS）
seen = [False] * N
q = deque([0])
seen[0] = True

while q:
    v = q.popleft()
    for nv in G[v]:
        if not seen[nv]:
            seen[nv] = True
            q.append(nv)

# すべて訪問できたか？
if all(seen):
    print("Yes")
else:
    print("No")

"""
BFS
チャッピー

サイクルグラフとは、
頂点が円環状に連なって閉じたループ（輪）を形成するグラフのことを指します。
頂点数： n
辺数： n
各頂点の次数（つながっている辺の数）：2
辺の構造：頂点が輪のようにつながっている。

https://atcoder.jp/contests/abc404/tasks/abc404_c
https://chatgpt.com/c/690025bd-252c-8324-881a-00fb957303a0
"""
