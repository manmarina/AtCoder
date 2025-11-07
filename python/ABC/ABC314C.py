import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = input().strip()
c = list(map(int, input().split()))

# 色ごとにインデックスを集める（1..m）
p = [[] for _ in range(m + 1)]  # 色 -> [インデックスの配列]
for i in range(n):
    p[c[i]].append(i)
print(p)

t = ['?'] * n  # 答えの文字列を格納する配列
print(t)

# 各色クラスで、文字を一つ先の位置に回す
for color in range(1, m + 1):  # 色を1色ずつ操作
    idxs = p[color]  # [インデックスの配列]
    k = len(idxs)
    for j in range(k):
        t[idxs[(j + 1) % k]] = s[idxs[j]]  # 回転を利用して文字の位置を1つずらす
print(t)

print(''.join(t))

"""
文字列操作
回転を利用して色ごとに文字の位置を1つずらす。

https://atcoder.jp/contests/abc314/tasks/abc314_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690d484c-9e64-8323-bb3c-330ae8c2e7c0
"""
