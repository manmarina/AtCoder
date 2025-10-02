import sys

input = sys.stdin.readline
N = int(input())
seen = set()

best_score = 0
best_idx = 0

for i in range(1, N + 1):
    s, t = input().split()
    t = int(t)
    if s in seen:
        continue
    seen.add(s)  # 初出だけ通す

    # 最大値更新。同点はより早い添字を優先（i は 1-index）
    if t > best_score:
        best_score = t
        best_idx = i

print(best_idx)

"""
基本実装問題
チャッピー

ハッシュ（辞書／集合）で重複排除
文字列 S_i が初めて出たときだけその得点 T_i を評価する。
既出の S は無視。
有効な投稿の中で 得点最大、同点なら **最も早い（添字が小さい）**ものの添字を出力。

https://atcoder.jp/contests/abc251/tasks/abc251_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68ddf2fb-a190-8328-9410-e7f94821fac6
"""
