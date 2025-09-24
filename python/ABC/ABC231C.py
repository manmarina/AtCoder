import sys
from bisect import bisect_left

input = sys.stdin.readline
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()  # 昇順

out = []
for _ in range(Q):
    x = int(input())
    idx = bisect_left(A, x)  # x以上が最初に出る位置
    out.append(str(N - idx))  # 右側の要素数
print("\n".join(out))

"""
二分探索（lower_bound）
チャッピー
「各クエリ x について、配列 A の中で x 以上 の要素がいくつあるか」を高速に数えるだけ。

https://atcoder.jp/contests/abc231/tasks/abc231_c
https://chatgpt.com/c/68d31221-3c30-8331-8010-1aa83814b863
"""
