N = int(input())
cards = []

for i in range(N):
    A, C = map(int, input().split())
    cards.append((A, C, i))  # (強さA, コストC, 元のID)

# A が大きい順にソート（右から考えるため）
cards.sort(key=lambda x: -x[0])

res = []
prev = 1 << 30   # とても大きい値（C の最小を管理するため）

for A, C, idx in cards:
    if C < prev:
        prev = C
        res.append(idx)

# 元の番号順にソートして出力
res.sort()

print(len(res))
print(*[x + 1 for x in res])

"""
クエリ処理
けんちょん
https://drken1215.hatenablog.com/entry/2024/05/19/021800
座標平面上にプロットしてみよう (A を x 座標、C を y 座標とする)。
このとき、この問題は「自分の右下方向には点がないような点」を抽出せよ、と解釈できる。

https://atcoder.jp/contests/abc354/tasks/abc354_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6931411d-de7c-8322-ad44-8f26415c9a2c
"""
