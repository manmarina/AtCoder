q = int(input())
now = 0  # 次のヘビの頭の位置
x = []  # ヘビの頭の位置を格納
id = 0  # 抜けたヘビの数

for _ in range(q):
    t, *rest = map(int, input().split())

    if t == 1:
        l = rest[0]
        x.append(now)  # ヘビの頭の位置を追加
        now += l  # 次のヘビの頭の位置を更新
    elif t == 2:
        id += 1  # 抜けたヘビの数を増やす
    else:  # t == 3
        k = rest[0] - 1  # 0-indexed
        print(x[id + k] - x[id])  # k番目のヘビの頭の座標を出力

print(x)

"""
計算量を削減したクエリ処理
自力解 4変数、1 defaultdict
-> 解説 2変数, 1配列
効率がよくわかりやすい。

https://atcoder.jp/contests/abc389/tasks/abc389_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690d9b76-d294-8322-95ea-4558c340120a
"""
