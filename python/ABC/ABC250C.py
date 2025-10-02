import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
X = [int(input()) for _ in range(Q)]

# A[i] = 位置iにある値, pos[v] = 値vの位置
A = [0] + [i for i in range(1, N + 1)]  # 通常配列（インデックス→値）
pos = [0] + [i for i in range(1, N + 1)]  # 位置配列（値→インデックス）

for x in X:
    p = pos[x]
    if p == N:
        q = p - 1            # 左隣の位置
    else:
        q = p + 1            # 右隣の位置
    y = A[q]                  # 隣の値

    # A 側を交換
    A[p], A[q] = A[q], A[p]
    # pos 側も交換後の位置に更新
    pos[x], pos[y] = q, p

    # print(A)
    # print(pos)

print(*A[1:])


"""
シミュレーション／位置管理（インデックス↔値の相互参照）
チャッピー
位置配列を使用

各クエリで「要素 x を隣と swap」するだけ。高速にやるために 位置配列 を持つのがポイント。
位置配列を使用しない解ではTLEになる。

https://atcoder.jp/contests/abc250/submissions/me
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68ddc0e7-5140-8322-a9a3-1e689189bbbc
"""
