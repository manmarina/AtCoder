S = input()
T = input()


def RLE(S):  # ランレングス圧縮
    N = len(S)
    lens = []
    i = 0
    while i < N:
        j = i
        while j < N and S[j] == S[i]:
            j += 1
        lens.append((S[i], j - i))  # (文字,文字長)を記録
        i = j
    return lens


Sc = RLE(S)
Tc = RLE(T)
# print(Sc)
# print(Tc)

if len(Sc) != len(Tc):  # 要素数が異なる時はアウト
    print("No")
    exit()

for s, t in zip(Sc, Tc):
    # 文字が違ったらアウト、tのほうが長かったらアウト、sが1のときにtが1でなければアウト
    if s[0] != t[0] or s[1] > t[1] or (s[1] == 1 and t[1] != 1):
        print("No")
        exit()

print("Yes")

"""
ランレングス圧縮(RLE)
リトライ
ランレングス圧縮テンプレートを使用。
チャッピーと同じロジックで書けた。

操作は「同じ文字が連続2個以上ある箇所だけを、さらに同じ文字で伸ばせる（増やせる）」というもの。
→ つまり 文字の並び順は変えられない、かつ 各連続区間（run）の長さは“そのまま”か“増加”しか起きない。ただし長さ1の区間は増やせない。
これを文字列S, Tの**RLE（文字と長さの列）**に分解して、各区間で判定します。

https://atcoder.jp/contests/abc259/tasks/abc259_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de28fd-d204-8327-85a6-4d40c0bb8216
"""
