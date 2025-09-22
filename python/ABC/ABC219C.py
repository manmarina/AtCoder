X = input()
N = int(input())
S = [input() for _ in range(N)]

# 文字を新辞書順のインデックスに変換
S2 = []
for s in S:
    temp = []
    for ch in s:
        temp.append(X.index(ch))
    S2.append(temp)
# print(S2)

# ソートした後にインデックスを新辞書順の文字に変換して表示
S2.sort()
for s in S2:
    temp = []
    for idx in s:
        temp.append(X[idx])
    print(*temp, sep='')

"""
文字列操作
自力解

与えられたアルファベット順（X）に従って、N 個の小文字文字列を辞書順ソートする問題です。
通常の a-z ではなく、X の並びを“あたらしい辞書順”として使います。

文字列をインデックスのリストに変換してソート
ソート済みのインデックスのリストを文字列に逆変換して表示
"""
