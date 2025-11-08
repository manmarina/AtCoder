MOD = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))

s1 = 0
s2 = 0
for x in A:
    x %= MOD
    s1 = (s1 + x) % MOD         # sum A_i
    s2 = (s2 + x * x) % MOD     # sum A_i^2 (mod)

ans = (s1 * s1 - s2) % MOD
inv2 = pow(2, MOD - 2, MOD)     # 2 の逆元
ans = ans * inv2 % MOD
print(ans)

"""
計算量を削減したシミュレーション + 数学的な気づき系
別解
数列の式を変形して、計算を高速化する。
変形した式は、チャッピーの解法2の解説を参照して下さい。

けんちょん
https://drken1215.hatenablog.com/entry/2020/10/09/172500

https://atcoder.jp/contests/abc177/tasks/abc177_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/project
"""
