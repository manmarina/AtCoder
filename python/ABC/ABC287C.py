from collections import defaultdict, deque


N, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
# print(G)

# 辺の数が頂点数-1でないときは終了
if N - M != 1:
    print("No")
    exit()

# 次数（頂点から出る辺の本数）が3以上のときは終了
for i in range(1, N + 1):
    if len(G[i]) > 2:
        print("No")
        exit()

# BFS
visited = [False] * (N + 1)
visited[1] = True
dq = deque([1])

while dq:
    v = dq.popleft()
    for nv in G[v]:
        if not visited[nv]:
            visited[nv] = True
            dq.append(nv)

# 出力
print("Yes" if all(visited[1:]) else "No")  # 全体が接続ならOK
# print(visited)

"""
BFS
公式解説
パスグラフ（分岐や循環のないグラフ）を判定する問題。

https://atcoder.jp/contests/abc287/tasks/abc287_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691d4c05-e86c-8324-9570-6199651d9876
"""
