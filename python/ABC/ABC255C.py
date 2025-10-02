import sys

x, a, d, n = map(int, sys.stdin.readline().split())

if d == 0:
    print(abs(x - a))
    exit()

# d を正に正規化
if d < 0:
    a = a + d * (n - 1)
    d = -d

L = a  # 数列の最小値
R = a + d * (n - 1)  # 数列の最大値

if x <= L:  # 数列の最小値よりxが小さいとき
    print(L - x)
elif x >= R:  # 数列の最大値よりxが大きいとき
    print(x - R)
else:
    t = x - L          # 0 <= t < d*(n-1)
    r = t % d          # 最近格子までのずれ
    print(min(r, d - r))

"""
数学的気付き 等差数列・剰余／数直線上の距離計算
チャッピー
ざっくり言うと「数直線上の等差数列のうち、x に一番近い項との差の最小値」を O(1) で求める問題です。
分類：数学（等差数列・剰余）／数直線上の距離計算（二分探索でも解けるが不要）

d を正に正規化しておく(d<0 なら a を a+(N-1)d に置き換え、d=-d にする）。

https://atcoder.jp/contests/abc255/tasks/abc255_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de0fea-ee14-8326-b456-59c906b1882f
"""
