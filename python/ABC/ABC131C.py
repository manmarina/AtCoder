from math import lcm


A, B, C, D = map(int, input().split())

whole = B - A + 1
div_C = B // C - (A - 1) // C
div_D = B // D - (A - 1) // D
div_CD = B // lcm(C, D) - (A - 1) // lcm(C, D)
ans = whole - (div_C + div_D - div_CD)

print(ans)

"""
数学的な気づき系
包除原理（ベン図）を活用する。
全体 - (Cで割り切れる数 + Dで割り切れる数 - CDの最小公倍数で割り切れる数) が答え。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2019/06/22/224100

https://atcoder.jp/contests/abc131/tasks/abc131_c
"""
