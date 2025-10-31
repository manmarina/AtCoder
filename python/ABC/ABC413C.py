from collections import deque


Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

A = deque()
for q in query:
    if q[0] == 1:  # クエリ1の時
        _, c, x = q
        A.append([x, c])  # (数値, 個数)を追加
        continue

    # q[0] == 2　クエリ2の時
    _, k = q  # 削除して合計を表示する個数
    x, c = A[0][0], A[0][1]  # 数値, 個数

    temp = 0
    while True:
        if k < c:  # 削除する個数がcよりも小さい時
            print(temp + k * x)  # 削除した数の合計値を出力
            A[0][1] = c - k  # 削除した文の個数を減らす
            break
        else:  # そうでないとき
            temp += x * c  # 削除する数の合計をプール
            k -= c  # 削除した分kを減らす
            A.popleft()  # 　空になったタプルを削除

            # ### 0になったときのチェックをしないとRE ###
            if k == 0:  # ちょうど空になった時
                print(temp)  # 削除した数の合計値を出力して終了
                break

            x, c = A[0][0], A[0][1]  # 数値, 個数を更新

"""
計算量を削減したクエリ処理
整数列Aをそのまま配列で保持しようとすると、 Aの長さは最大 10^14オーダーとなるため現実的ではない。
数値xと個数cを（x,c）というタプルで追加して数量管理する。

Yuulisによる解説
https://yuulis.hatenablog.com/entry/ABC-413-C

https://atcoder.jp/contests/abc413/tasks/abc413_c

チャッピーによるRE対応
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6904608a-117c-8324-98f6-869461231916
"""
