import sys
from collections import deque

N = int(sys.stdin.readline())
edges = []
vals = {1}  # 座標圧縮に使用
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    edges.append((a, b))
    vals.add(a)
    vals.add(b)
# print(edges)

# 座標圧縮
vals = sorted(vals)  # 逆変換（インデックス → 元の値）に使用
idx = {v: i for i, v in enumerate(vals)}  # 順変換（元の値 → 連番インデックス)に使用
K = len(vals)
# print(vals)
# print(idx)

# グラフを作成（idxを使用してインデックスに変換）
G = [[] for _ in range(K)]
for a, b in edges:
    ia, ib = idx[a], idx[b]
    G[ia].append(ib)
    G[ib].append(ia)
# print(G)

# bfs開始準備
start = idx[1]
visited = [False] * K
ans = 1

# bfs部分
visited[start] = True
q = deque([start])
while q:
    v = q.popleft()
    ans = max(ans, vals[v])  # 圧縮→元の値に戻して最大更新
    for nv in G[v]:
        if not visited[nv]:
            visited[nv] = True
            q.append(nv)

print(ans)

"""
BFS版
（反復DFSとの違いはスタックとキューの違いのみ）

この問題は、
    数直線上の整数を頂点
    入力のペア (ai,bi) を無向辺
とみなしたグラフの連結成分探索です。
スタートは頂点 1、そこから到達可能な頂点（値）の最大値を答えます。
"""

"""
座標圧縮

座標圧縮は 「大きい・疎な数値を、小さい連続番号に変換する」テクニック です。
この問題では「数直線上の整数」を「グラフの頂点番号」に変換するために必須の処理になっています。

座標圧縮の実装では vals（リスト）と idx（辞書）の2つをセットで用意する のがとても一般的です。
役割の違い
vals（リスト）
    圧縮後の番号から「元の値」に戻すために使います。
    例：vals[2] = 500000000 のように「逆変換」できる。
    BFS/DFSで探索したあと「最大値は？」と答える時に必要。
idx（辞書）
    元の値から「圧縮後の番号」に変換するために使います。
    例：idx[500000000] = 2 のように「順変換」できる。

グラフの辺を作る時や配列アクセスに必要。

まとめると

順変換（元の値 → 連番インデックス） → idx
逆変換（インデックス → 元の値） → vals

両方を用意しておけば、
「探索はインデックスで効率的に」「答え出力は元の値で」
という処理がスムーズにできます。
"""
