MOD = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))

# 右側の合計を最初に作る
right_sum = sum(A) % MOD
ans = 0

for i in range(N - 1):
    right_sum = (right_sum - A[i]) % MOD   # A[i] より右側の合計に更新
    ans = (ans + A[i] * right_sum) % MOD   # A[i] * (右側の和) を加算

print(ans)

"""
計算量を削減したシミュレーション + 数学的な気づき系
数列の式を変形して、計算を高速化する。
変形した式は、チャッピーの解法1の解説を参照して下さい。

けんちょん
https://drken1215.hatenablog.com/entry/2020/10/09/172500

https://atcoder.jp/contests/abc177/tasks/abc177_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/project
"""
