x1, y1, x2, y2 = map(int, input().split())

moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),
         (1, -2), (2, -1), (-1, -2), (-2, -1)]

s1 = {(x1 + dx, y1 + dy) for dx, dy in moves}
s2 = {(x2 + dx, y2 + dy) for dx, dy in moves}

print("Yes" if s1 & s2 else "No")

"""
全探索
チャッピー

「半径 5 の円（実際は8点）を両点の周りに置いたとき共通の格子点があるか」を判定するだけ
P1から行ける 8 点と P2から行ける 8 点を作って 集合の積（共通要素）を見れば O(1) で判定できます。

https://atcoder.jp/contests/abc239/tasks/abc239_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68d3b3ee-4170-8331-90c7-c18e15d48142
"""
