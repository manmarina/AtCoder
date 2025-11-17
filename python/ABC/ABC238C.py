MOD = 998244353

N = int(input())

ans = 0
power10 = 1  # 10^(d-1) を表す（最初は 1 桁 -> 10^0）

while power10 <= N:
    L = power10                 # この桁の最小値
    R = power10 * 10 - 1        # この桁の最大値（例：1桁なら 9, 2桁なら 99）
    if R > N:
        R = N                   # N を超えないように切る

    K = R - L + 1               # このブロックに含まれる個数
    # 1 + 2 + ... + K を足す
    s = K * (K + 1) // 2
    ans = (ans + s) % MOD

    power10 *= 10               # 次は 10, 100, 1000, ... へ

print(ans % MOD)

"""
法則を見つける系
公式解説
d 桁の数の範囲は：
    下端 L = 10^{d-1}
    上端 R = 10^d - 1
でも、N が途中で終わることがあるので、実際に使う上端は
    R’ = min(R, N)
このブロックに含まれる個数 K は
    K=max(0,R’-L+1)
これを全部の桁について足していく。

https://atcoder.jp/contests/abc238/tasks/abc238_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691a7e7e-ad5c-8320-8aef-6f5e7f63ccd0
"""
