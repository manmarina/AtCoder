# ### 鉄則本の実装とすこし異なるが機能はまったく同じ ###
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # parentの初期値は各インデックス値とする実装
        self.size = [1] * n  # sizeを別配列で管理する実装 0-indexed

    def find(self, x):
        if self.parent[x] != x:  # 自分のインデックスではない時
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False  # すでに同じグループ
        # union by size
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True
# ### 鉄則本の実装とすこし異なるが機能はまったく同じ ###


N, M = map(int, input().split())
uf = UnionFind(N)
# print(uf.parent)

# Union-Findを使って、すべての頂点が孤立した状態から、連結させてゆく
K = N  # 現在の連結成分数=頂点数
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1  # 0-indexed
    v -= 1  # 0-indexed
    if not uf.same(u, v):  # 別の連結成分のとき
        uf.unite(u, v)  # 連結させて
        K -= 1  # 連結成分数を1減らす

print(M - (N - K))  # チャッピーの解説を参照
"""
チャッピーの解説要約
連結する頂点をn,全頂点をN,連結成分数をKとする時、
ある連結成分において、n頂点が閉路を持たないときの辺の数はn-1、
-> すべての連結成分における、N頂点が閉路を持たないときの辺の数はN-Kとなる。
すべての辺の数MよりN-Kを引くと、求めたい「削除する辺の数」となる。
"""

"""
Union-Find(DSU)
DFS,BFSでも解けるらしい。
Union-Findで、ばらばらの頂点を連結させてゆき、連結成分数Kを求める。
現在の辺の数Mと頂点数N、連結成分数Kのより、M-(N-K)が削除する辺の本数となる。

公式解説
https://atcoder.jp/contests/abc399/editorial/12559
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69076aa7-1740-8321-a267-e75375673038
公式解説をチャッピーに解説してもらったらわかりやすかった。

https://atcoder.jp/contests/abc399/tasks/abc399_c
"""
