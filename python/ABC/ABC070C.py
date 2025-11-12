from math import lcm


N = int(input())
T = [int(input()) for _ in range(N)]
# print(T)

print(lcm(*T))

"""
数学的な気づき系
最小公倍数を求める。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2025/01/07/000710

https://atcoder.jp/contests/abc070/tasks/abc070_c
"""
