from math import gcd


K = int(input())

ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            ans += gcd(a, b, c)

print(ans)

"""
数学的な気づき系
制約が小さいので数列の数式のとおりに3重ループを実装すれば解ける。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/04/12/225500

https://atcoder.jp/contests/abc162/tasks/abc162_c
"""
