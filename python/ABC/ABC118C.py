def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N = int(input())
A = list(map(int, input().split()))

res = A[0]
for i in range(N):
    res = gcd(res, A[i])  # 最後に残る体力の最小値 = A₁, …, Aₙ の最大公約数（gcd）

print(res)

"""
数学的な気づき系
けんちょん
https://drken1215.hatenablog.com/entry/2019/02/16/224200
どのモンスターの体力も常に g の倍数」が不変量であることに気づく。
最後に残る体力の最小値 = A₁, …, Aₙ の最大公約数（gcd）

a も b も g の倍数だとすると、
a=g⋅x, b=g⋅y
a-b=g(x-y) もやはり g の倍数

つまり 「倍数 - 倍数 = 倍数」 なので、
一生 g の倍数からは逃げられません。

このように、操作をしても変わらない性質を
不変量（invariant） と呼びます。

https://atcoder.jp/contests/abc118/tasks/abc118_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6915de73-05ec-8320-ad9c-70c598d298b2
"""
