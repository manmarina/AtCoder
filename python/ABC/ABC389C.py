from collections import defaultdict


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]
# print(Query)

shift = 0  # 抜けたヘビの長さ
bye = 0  # 抜けたヘビの数
head = 0  # ヘビの頭の位置
id = 1  # ヘビのid
dd = defaultdict(list)
for q in Query:
    if q[0] == 1:
        _, l = q
        dd[id] = [head, l]  # (ヘビの頭の位置, ヘビの長さ)
        # print("q:", q[0], "head:", head, "l:", l, "id:", id)

        head += l  # 次の蛇の頭の位置を更新
        id += 1  # 次のヘビのidを更新
    elif q[0] == 2:
        bye += 1  # 抜けたヘビの数を増やす
        shift -= dd[bye][1]  # 抜けたヘビの長さを減らす
        # print("q:", q[0], "bye:", bye, "shift:", shift)
    else:  # q[0] == 3:
        _, k = q
        print(dd[k + bye][0] + shift)  # k番目のヘビの頭の座標を出力
        # print(dd)
        # print("q:", q[0], "bye:", bye, "shift:", shift)

"""
計算量を削減したクエリ処理
連想配列と変数を使用して、ヘビの配列を変更することなくクエリ処理する。

https://atcoder.jp/contests/abc389/tasks/abc389_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690d9b76-d294-8322-95ea-4558c340120a
"""
