from itertools import permutations

N, M = map(int, input().split())

# 隣接行列を 0/1 で作る
X = [[0] * N for _ in range(N)]
Y = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    X[a][b] = X[b][a] = 1

for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    Y[c][d] = Y[d][c] = 1

# すべての順列 P を試す
for P in permutations(range(N)):  # P は (0,1,2,...) みたいなタプル
    ok = True
    for i in range(N):
        for j in range(N):
            if X[i][j] != Y[P[i]][P[j]]:  # 番号を入れ替えたときに、紐のつき方は一致しているか？
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

https://atcoder.jp/contests/abc232/tasks/abc232_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691979e5-e8fc-8320-93c5-92090a91d6c9
"""
