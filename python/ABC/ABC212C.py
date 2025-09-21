import sys
from bisect import bisect_left

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
INF = 10**18
ans = INF

for a in A:
    j = bisect_left(B, a)
    """
    なぜ if j < M: が必要か
    もし j == M のときに B[j] を参照すると
    B[4] になり IndexError（範囲外アクセス） になるので禁止。
    だから if j < M: で「まだ B[j] が存在するなら見る」としています。
    """
    if j < M:  # aより大きい最小の要素
        ans = min(ans, abs(a - B[j]))
    if j > 0:  # aより小さい最大の要素
        ans = min(ans, abs(a - B[j - 1]))

print(ans)

"""
二分探索（lower_bound）
    ソート済み配列の中から「ある値以上が最初に現れる位置」を探す処理 を指します。
    はじめて学ぶ二分探索の例
チャッピー

問題の要約
2 つの配列 A（長さ N）と B（長さ M）が与えられる。
任意の a∈A と b∈B の差の絶対値 |a-b| の最小値を求めよ。

典型解法
片方（例えば B）を昇順にソート。
各 a∈A について、B の中で a 以上となる最初の要素位置 j = lower_bound(B, a) を探す。
候補は高々 2 つ：
    B[j]（存在すれば）：aより大きい最小の要素
    B[j-1]（j>0 のとき）：より小さい最大の要素
それぞれと a の差を取って最小を更新。

計算量：O(M log M + N log M)（B を一度ソート、A の各要素で二分探索）
"""
