from collections import defaultdict, deque


N = int(input())
AB = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    AB[a].append(b)
    AB[b].append(a)
# print(AB)

visited = defaultdict(bool)
# print(visited)

visited[1] = True
dq = deque([1])

while dq:
    v = dq.popleft()
    for nv in AB[v]:
        if not visited[nv]:
            visited[nv] = True
            dq.append(nv)

# print(visited)
print(max([i for i, v in visited.items() if v]))  # vがTrueであるiの最大値

"""
BFS
リトライ

visitedにdefaultdictを用いて、座標圧縮を行わずに実装。

https://atcoder.jp/contests/abc277/tasks/abc277_c
https://chatgpt.com/c/68cbfc15-cdf4-8325-ae0f-3ed64021fae7
"""
