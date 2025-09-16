from itertools import combinations
from math import hypot


N = int(input())
XY = [tuple(map(int, input().split()))for _ in range(N)]

# 同じ計算を繰り返さないためにに2次元配列を準備
dists = [[0] * N for _ in range(N)]
# print(dists)

# 2点の組み合わせから距離を計算して、2次元配列に格納する
for xy1, xy2 in combinations(enumerate(XY), 2):
    # print(xy1, xy2)
    idx1, (x1, y1) = xy1
    idx2, (x2, y2) = xy2

    dist = hypot(x1 - x2, y1 - y2)  # 大小比較なら二乗距離でも十分だが今回はhypotで
    dists[idx1][idx2] = dist
    dists[idx2][idx1] = dist
# print(dists)

for row in dists:
    print(row.index(max(row)) + 1)

"""
ユークリッド距離は平方根を取らない
距離の大小比較なら二乗距離で十分。sqrtを使わないので速くて誤差ゼロ。

全探索 (O(N^2)) で十分
各 i について全 j をなめて最大の二乗距離の j を記録。
制約が小さい（N が大きくても 2e3 程度）ので二重ループでOK。

同距離のタイブレーク
もし同距離が複数あるときは、番号が小さい方を選べば安全（典型的なAtCoderの規約）。
実装では「> ではなく >= にしない」ことで自然に小さい方が残ります。
"""
