class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n  # 負なら根 & その絶対値がサイズ

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:  # サイズが大きい方を根に
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True


N, M = map(int, input().split())
uf = UnionFind(N + 1)
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    if uf.same(a, b):
        ans += 1  # これを追加すると閉路ができる → 削除すべき辺の数
    else:
        uf.union(a, b)

print(ans)

# print(uf.parent)

# # ここから連結成分の情報を取り出す部分
# L = []  # 各連結成分の頂点数を入れるリスト
# for i in range(1, N + 1):
#     if uf.parent[i] < 0:   # i が根なら、その成分の代表
#         L.append(-uf.parent[i])

# S = len(L)  # 連結成分の個数

# # 出力
# print("S:", S)  # 連結成分の数
# print("L:", L)  # 各連結成分の頂点数

"""
Union-Find
すでに連結している頂点同士をつなぐ辺の数を直接カウントする。
DFS/BFSでも解ける。

https://atcoder.jp/contests/abc288/tasks/abc288_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691d549c-195c-8320-b9de-3759f27a4017
"""
