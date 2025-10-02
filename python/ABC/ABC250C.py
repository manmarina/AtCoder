import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
X = [int(input()) for _ in range(Q)]

# A[i] = 位置iにある値, pos[v] = 値vの位置
A = [0] + [i for i in range(1, N + 1)]

for x in X:
    p = A.index(x)
    if p == N:
        q = p - 1            # 左隣の位置
    else:
        q = p + 1            # 右隣の位置

    # A 側を交換
    A[p], A[q] = A[q], A[p]
    # print(A)

print(*A[1:])
# print(A)

"""
シミュレーション／位置管理（インデックス↔値の相互参照）
自力解 TLE

各クエリで「要素 x を隣と swap」するだけ。高速にやるために 位置配列 を持つのがポイント。
位置配列を使用しない解ではTLEになる。

https://atcoder.jp/contests/abc250/submissions/me
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68ddc0e7-5140-8322-a9a3-1e689189bbbc
"""
