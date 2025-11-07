N = int(input())


def conv(fi):
    # 入力されたカーペットに対して、レベルが1段階上のカーペットを出力する関数
    n = len(fi)  # fiは雛形のカーペット
    res = []  # からの配列に対して積み上げてゆく
    for i in range(n * 3):  # i方向に3倍する
        row = ""
        for j in range(n * 3):  # j方向に3倍する
            # 真ん中はすべて "."
            if n <= i < n * 2 and n <= j < n * 2:
                row += "."
            else:
                # 1つ前のカーペットをコピー
                row += fi[i % n][j % n]  # i,jともnで回転する
        res.append(row)
    return res


# N回レベルアップさせる
res = ["#"]  # 初期値
for _ in range(N):
    res = conv(res)

# 出力
for s in res:
    print(s)

"""
再帰関数
「与えられたカーペットのレベルを 1 段階上げたカーペットを出力する」ような関数を実装しよう！
それが実装できれば、その関数を N回呼び出せばよい。

けんちょん
https://drken1215.hatenablog.com/entry/2024/06/09/233433

https://atcoder.jp/contests/abc357/tasks/abc357_c
"""
