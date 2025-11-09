from collections import Counter


S = list(input())
# print(S)

cnt = Counter(S)
# print(cnt)

if len(cnt) == 1:  # 0か1しかないときは一つも消せない
    print(0)
else:
    print(min(cnt.values()) * 2)  # 少ない文字の数 x 2が消せる数


"""
法則を見つける系
0と1の個数が少ない方はすべて消せることを見抜く。

https://atcoder.jp/contests/abc120/tasks/abc120_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69103b21-457c-8324-99ee-e80f021dcead
"""
