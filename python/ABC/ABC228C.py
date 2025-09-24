import sys

N, K = map(int, sys.stdin.readline().split())
S = []
P = []

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    s = a + b + c
    S.append(s)
    P.append(s)  # 元の順序での出力判定用

T = sorted(S, reverse=True)[K - 1]  # しきい値（K番目）

for s in P:
    print("Yes" if s + 300 >= T else "No")

"""
基本実装問題
チャッピー
ソート＋しきい値で判定するだけ。

https://atcoder.jp/contests/abc228/tasks/abc228_c
https://chatgpt.com/c/68d29c37-36b0-832f-b802-d457a3b56902
"""
