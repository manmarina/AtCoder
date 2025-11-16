from itertools import permutations

N, M = map(int, input().split())

# 隣接リスト（集合）で持つ
G1 = [set() for _ in range(N)]
G2 = [set() for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G1[a].add(b)
    G1[b].add(a)

for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    G2[c].add(d)
    G2[d].add(c)

# すべての順列 P を試す
for P in permutations(range(N)):  # P は (0,1,2,...) みたいなタプル
    ok = True
    # グラフ1の全ての辺をチェック（i < j だけ見れば十分）
    for i in range(N):
        for j in G1[i]:
            if i < j:  # 同じ辺を2回見ないように
                if P[j] not in G2[P[i]]:  # 番号を入れ替えたときに、紐のつき方は一致しているか？
                    ok = False
                    break
        if not ok:
            break  # iのループを抜ける
    if ok:
        print("Yes")
        exit()

print("No")

"""
グラフ
公式解説
グラフを同型判定する問題。
(1,2,…,N) を並べ替えて得られる順列 P を全探索することを考えます。
P が条件をみたすことは、次が成り立つことと同値です。

任意の 1≤i≤N,1≤j≤N に対し Xi,j =YPi,Pj

意味を日本語にすると：
「どの 2 頂点 i, j についても、
    高橋側でのひもの有無（X_{i,j}）
    対応先 Pᵢ, Pⱼ で見た青木側のひもの有無（Y_{P_i,P_j}）
がすべて一致している」
= 高橋のグラフを P でラベリングし直したら、青木のグラフと完全に同じ配置になる、ということです。

if i < j:について
隣接配列（隣接行列）では、各ペア (i, j) を 1 回しか見ていない
→ 重複が起こらないので i<j の工夫が不要

隣接リストでは、無向グラフなので必ず辺を 2 回見る
→ (i, j) と (j, i) の両方がリストに入っているため
→ i<j などで 片方だけ 見ないと、同じ辺を 2 回チェックしてしまう

https://atcoder.jp/contests/abc232/tasks/abc232_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691979e5-e8fc-8320-93c5-92090a91d6c9
"""
