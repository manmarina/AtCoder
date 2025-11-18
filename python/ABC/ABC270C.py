from collections import deque

N, X, Y = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
# print(G)

# X からの BFS で親を記録
parent = [-1] * (N + 1)  # visitedと同じ訪問管理 + 親の番号を記録（pathの復元に使う）
dq = deque([X])
parent[X] = 0  # 根の親は 0 （ダミー）

while dq:
    v = dq.popleft()
    if v == Y:
        break  # Yが出てきたらbreakしてパス復元へ
    for nv in G[v]:
        if parent[nv] == -1:  # -1の時
            parent[nv] = v  # 親の番号を記録
            dq.append(nv)

# Y から親を辿ってパス復元
path = []
cur = Y
while cur != 0:
    path.append(cur)
    cur = parent[cur]

path.reverse()
print(*path)

"""
BFS
チャッピー
再帰DFSではTLEになったのでBFSで実装。（反復DFSでも良い。）
True,Falseによるvisited -> 親番号の記録と訪問管理を兼用するparentを用いる。
ゴールに辿り着いたらparentを使用してパスを復元する。

✔ Python ではどこまで実際に耐えられる？
実測すると：
Python はだいたい 再帰 10万～100万回 で落ちる（環境による）
sys.setrecursionlimit(10**7) でも実際は 100万も行かずにスタックが死ぬ。

競プロで「木のパスを求める」問題は BFS が定番らしい。

https://atcoder.jp/contests/abc270/tasks/abc270_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691c09a0-ce98-8324-8a4e-15e8875193b4
"""
