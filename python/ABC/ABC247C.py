def build(n):
    if n == 1:
        return [1]
    left = build(n - 1)
    return left + [n] + left


N = int(input())
print(*build(N))

"""
構築系問題(再帰)
チャッピー
配列を使用

ざっくり言うと「再帰で左右対称に積むだけ」の構築問題です。

https://atcoder.jp/contests/abc247/tasks/abc247_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68dd3dd6-9f04-8321-a5e6-7a3f3e7f7b9c
"""
