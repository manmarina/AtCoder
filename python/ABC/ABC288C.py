from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
L = 0  # 閉路を作らないように残せる最大の辺の本数

for i in range(1, N + 1):  # スタート位置をすべて試す
    if visited[i]:  # Trueならパスする
        continue

    # i を始点に BFS
    n = 1  # この連結成分に含まれる頂点数
    dq = deque([i])
    visited[i] = True

    while dq:
        v = dq.popleft()
        for nv in G[v]:
            if not visited[nv]:
                visited[nv] = True
                n += 1
                dq.append(nv)

    L += n - 1  # この成分から残せる最大の辺を加算

# 出力
print(M - L)  # 削除すべき辺の本数

"""
BFS
各連結成分の頂点数nをカウントする -> n-1が各連結成分の残せる最大の辺の数。
L += n - 1で辺の数を累積する。
削除すべき辺の本数は、MからLを引いたものとなる。

https://atcoder.jp/contests/abc288/tasks/abc288_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691d549c-195c-8320-b9de-3759f27a4017
"""
