import sys

A, B, P, Q, R, S = map(int, sys.stdin.read().split())

H = Q - P + 1  # 出力する行数
W = S - R + 1  # 出力する列数

# 直線の条件式:
#   (i - j) == (A - B)    … 対角線1（↘↗）
#   (i + j) == (A + B)    … 対角線2（↙↖）
# 行 i ごとに、該当する列 j を式から直接求めて配置する
for i in range(P, Q + 1):
    row = ['.'] * W

    # 対角線1:  i - j = A - B  →  j = i - (A - B)
    j1 = i - (A - B)
    if R <= j1 <= S:
        row[j1 - R] = '#'

    # 対角線2:  i + j = A + B  →  j = (A + B) - i
    j2 = (A + B) - i
    if R <= j2 <= S:
        row[j2 - R] = '#'

    print(''.join(row))

"""
カーソル系（グリッド走査）
チャッピー
条件判定で格子点を出力する系のシミュレーション問題。

問題文の条件から以下を導けるかどうかが鍵になる
    1本目:(A+k,B+k) を黒く塗る から i-j=A-B へ
    2本目:(A+k,B-k) を黒く塗る から i+j=A+B へ

https://atcoder.jp/contests/abc230/tasks/abc230_c
https://chatgpt.com/c/68d2a018-5c40-8320-a18d-7263debfd048
"""
