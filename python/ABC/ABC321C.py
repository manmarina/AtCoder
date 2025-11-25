import sys
sys.setrecursionlimit(10**7)


def rec(val, vals):
    # 現在の値を登録
    vals.append(val)

    # 末尾の桁
    last = val % 10

    # 末尾が 0 なら、それ以上小さい数字がない
    if last == 0:
        return

    # 末尾より小さい数字をくっつけて再帰
    for d in range(last):  # d = 0,1,2,...,last-1
        rec(val * 10 + d, vals)


K = int(input())

vals = []

# 1 桁の 1〜9 を根として DFS を開始
for v in range(1, 10):
    rec(v, vals)

vals.sort()
print(vals[K - 1])
# print(vals)

"""
再帰DFSによる全探索
けんちょん
https://drken1215.hatenablog.com/entry/2023/09/30/120900
321-like Number は
    9876543210 から、いくつかの桁を「歯抜け」にして作ったもの。
    最大 1022 個しかない。
        2^10 - 2
        何も選ばないケースと、0だけ選んだケースの2つを除く。

https://atcoder.jp/contests/abc321/tasks/abc321_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69256100-b3f4-832b-b627-e231e0b5865d
"""
