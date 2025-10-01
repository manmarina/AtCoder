import sys
sys.setrecursionlimit(1 << 20)


def emit(n):
    if n == 1:
        print(1, end=' ')
        return
    emit(n - 1)
    print(n, end=' ')
    emit(n - 1)


N = int(input())
emit(N)
print()  # 改行

"""
構築系問題(再帰)
チャッピー
直接print

ざっくり言うと「再帰で左右対称に積むだけ」の構築問題です。

https://atcoder.jp/contests/abc247/tasks/abc247_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68dd3dd6-9f04-8321-a5e6-7a3f3e7f7b9c
"""
