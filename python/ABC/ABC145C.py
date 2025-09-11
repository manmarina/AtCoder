import math
from itertools import permutations

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

# 距離行列を作成
dist = [[0.0] * N for _ in range(N)]
for i in range(N):
    xi, yi = P[i]
    for j in range(N):
        xj, yj = P[j]
        dist[i][j] = math.hypot(xi - xj, yi - yj)
# print(dist)

# 距離行列から距離を求める
total = 0.0
cnt = 0
for order in permutations(range(N)):
    # print(order) ex.(0,1,2)

    path = 0.0
    for a, b in zip(order, order[1:]):  # ex.(0,1),(1,2)
        path += dist[a][b]
    total += path
    cnt += 1

print(total / cnt)

"""
毎回距離を計算すると重いので、最初に距離行列 dist[i][j] を作ると速く・きれい。
「距離行列」というのは、全ての点のペアごとの距離を前もって計算して表にしておく仕組みです。

これを二次元配列（行列）にするとこうなります：
	P0	P1	P2
P0	0	1	2
P1	1	0	√5
P2	2	√5	0

たとえば巡回順序が (P0 → P1 → P2) なら、
合計距離は
dist[0][1] + dist[1][2] = 1 + √5
もし (P2 → P0 → P1) なら、
dist[2][0] + dist[0][1] = 2 + 1
"""
