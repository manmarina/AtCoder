T = int(input())
tc = [list(map(int, input().split())) for _ in range(T)]
# print(tc)

for na, nb, nc in tc:
    total = na + nb + nc
    print(min(na, nc, total // 3))  # 特にtotal // 3を見抜くのがポイント！！ ex.5,0,7

"""
場合分け系
チャッピー

公式解説がわかりやすい
https://atcoder.jp/contests/abc422/editorial/13811

問題は「各コンテストで必ず A を1つ、C を1つ使い、残り1文字は A/B/C のどれでもよい。
最大で何回開催できるか？」というものです。

考え方（結論から）
1 回の開催につき必ず A と C を 1 つずつ消費し、合計で 3 文字消費します。
したがって開催回数 k は次の3つの上限を同時に満たす必要があります。
    A が足りる:
    C が足りる:
    文字総数が足りる（1回3文字）:
"""
