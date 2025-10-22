A, B, C, D = map(int, input().split())

den = C * D - B  # A + Bx < CDx より
if den <= 0:  # 　不等式を変形 CD-Bが負のときはxが負になり実現不可能
    print(-1)
else:
    # 0 回で既に満たす場合にも対応（A=0なら0が出る）
    # print((A + den - 1) // den)  # A // den の切り上げ除算
    print(-(-A // den))  # A // den の切り上げ除算

"""
不等式の変形 + 切り上げ除算

実現可能性を不等式の変形で判断
最小回数を切り上げ除算で求める

https://atcoder.jp/contests/abc207/tasks/abc207_b
https://chatgpt.com/c/68b00d83-add0-8324-8f51-535b81211407
"""
