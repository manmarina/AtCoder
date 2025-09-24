import sys
from collections import defaultdict

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

pos = defaultdict(list)
for i, a in enumerate(A, start=1):  # 1-indexed
    pos[a].append(i)

out_lines = []
for _ in range(Q):
    x, k = map(int, input().split())
    L = pos.get(x, [])
    if k <= len(L):
        out_lines.append(str(L[k - 1]))
    else:
        out_lines.append("-1")

print("\n".join(out_lines))

"""
基本実装問題
チャッピー
「データ構造系（連想配列での出現位置管理）」問題

https://atcoder.jp/contests/abc235/tasks/abc235_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68d356c3-2370-832f-ae8c-266469b34f84
"""
