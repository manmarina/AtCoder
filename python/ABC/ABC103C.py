from math import lcm


N = int(input())
A = list(map(int, input().split()))

hoge = 0
fuga = lcm(*A) - 1  # 最小公倍数-1
for a in A:
    hoge += fuga % a

print(hoge)


"""
法則を見つける系
答えは最小公倍数-1であることに気づく。
実際に適当な数までシミュレーションすると法則が見えてきた。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2018/07/21/224100

https://atcoder.jp/contests/abc103/tasks/abc103_c
"""
