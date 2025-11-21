from functools import cmp_to_key

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]


def cmp(i, j):
    Ai, Bi = AB[i]
    Aj, Bj = AB[j]
    lhs = Ai * (Aj + Bj)
    rhs = Aj * (Ai + Bi)

    if lhs > rhs:
        return -1  # i のほうが前（成功率が大）
    if lhs < rhs:
        return 1   # j のほうが前
    # 同率なら番号が小さい順
    return -1 if i < j else 1 if i > j else 0

    # if i < j:
    #     return -1    # i が先
    # elif i > j:
    #     return 1     # j が先
    # else:
    #     return 0     # 同じ


ids = list(range(N))  # インデックスを生成
print(ids)

ids.sort(key=cmp_to_key(cmp))  # sortのキーに比較関数を使用
print(*[i + 1 for i in ids])

"""
数学的な気づき系
普通に計算すると誤差でWAしてしまう -> 整数演算するしかない。
整数演算の結果を比較するために比較関数を利用してソートする。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/10/22/124200

double が表現できる「相対誤差」の目安は約 10^-15くらい。
    今回はAi側で10^-9精度
    Ai+Bi側でも10^-9精度
それを割り算するのでざっくり10^-18くらいの精度が欲しい。
でもdoubleは10^-15くらいまでしかがんばれないので、足りない。
-> 整数演算するしかない。

https://atcoder.jp/contests/abc308/tasks/abc308_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692036f2-dc98-8322-91c6-1b5de8e5e1aa
"""
