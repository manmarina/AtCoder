N = int(input())
A = list(map(int, input().split()))
# print(A)

# 最初の乗客が0人としたときの累積和を求める
cs = [0] * (N + 1)
for i in range(1, N + 1):
    cs[i] = cs[i - 1] + A[i - 1]
# print(cs)

# 累積和の最小値のマイナス値が最初の乗客数
print(cs[-1] - min(cs))  # 最後の乗客数 + 最初の乗客数

"""
累積和
累積和の最小値のマイナス値が最初の乗客数。

https://atcoder.jp/contests/abc339/tasks/abc339_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690bf32e-cb3c-8332-8aa4-ee514911ad42
"""
