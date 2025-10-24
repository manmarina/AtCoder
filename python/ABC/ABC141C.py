N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

point = [0] + [K] * N
for a in A:
    point[a] += 1

for p in point[1:]:
    print("Yes" if p - Q > 0 else "No")

"""
計算量を削減したシミュレーション

正答者以外のポイントをすべてマイナスすると都度O(N)なので、
正答者のポイントを増やして、判定時に出題数をマイナスすることで計算量を減らす。

https://atcoder.jp/contests/abc141/tasks/abc141_c
"""
