import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
S = input().strip()

groups = defaultdict(list)  # y -> list of (x, dir)
for (x, y), d in zip(XY, S):
    groups[y].append((x, d))
print(groups)

for y, arr in groups.items():
    arr.sort()  # x昇順
    seen_R = False
    for x, d in arr:
        if d == 'R':
            seen_R = True           # 左側にRが出現
        elif d == 'L' and seen_R:   # 左にRがいて右からLが来る → 衝突
            print("Yes")
            exit()
print("No")

"""
基本実装問題
チャッピー
「同じ y 上で、左にいる R と右にいる L が1組でもあれば衝突するか？」を見る問題です。

https://atcoder.jp/contests/abc243/tasks/abc243_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68dd109c-c23c-8326-a5dc-bae462d503cb
"""
