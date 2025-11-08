from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
# print(B)

# ランレングス圧縮
lens = []
i = 0
while i < N:
    j = i
    while j < N and B[j] == B[i]:
        j += 1
    lens.append((B[i], j - i))  # (文字,文字長)を記録
    i = j
# print(lens)

# ddの作成
sum_B = sum(B)  # Bの全体のsumを計算しておく
dd = defaultdict(int)  # Ai -> Aiより大きな要素の和
for v, n in lens:  # (文字,文字長)を取り出す
    sum_B -= v * n  # ある文字よりも大きい要素の和を求める
    dd[v] = sum_B
# print(dd)

# 出力
out = []
for a in A:
    out.append(dd[a])
print(*out)

"""
計算量を削減したシミュレーション + ランレングス圧縮
ランレングス圧縮を活用して連想配列の生成を高速化。

https://atcoder.jp/contests/abc331/tasks/abc331_c
"""
