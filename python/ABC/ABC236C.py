import sys
from bisect import bisect_left
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]
T = sorted(input().strip() for _ in range(M))

for s in S:
    i = bisect_left(T, s)
    # iには挿入すべき位置が返るので、T[i] == sをあわせて判定する必要がある
    print("Yes" if i < M and T[i] == s else "No")

"""
基本実装問題
チャッピー
データ構造系（集合・辞書）問題
ソート + 二分探索（bisect / lower_bound）による解

与えられた駅名列 S（長さ N）について、
各駅が別の集合 T（長さ M）に含まれるかどうかを判定して「Yes/No」を出力するだけの内容です。

https://atcoder.jp/contests/abc236/tasks/abc236_c
https://chatgpt.com/c/68d35709-dd00-8324-8f70-bf3a65019946
"""
