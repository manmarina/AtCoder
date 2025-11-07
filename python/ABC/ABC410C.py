N, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]

A = list(i for i in range(1, N + 1))
# print(A)

r = 0  # インデックスをオフセットする変数
for q in Query:
    if q[0] == 1:
        _, p, x = q
        p -= 1  # 0-indexed
        A[(p + r) % N] = x  # rでオフセット、%Nで回転に対応する
        # print(A)
    elif q[0] == 2:
        _, p = q
        p -= 1  # 0-indexed
        print(A[(p + r) % N])  # rでオフセット、%Nで回転に対応する
    else:  # q[0] == 3:
        _, k = q
        r += k  # オフセット値を更新する
        r %= N  # オフセット値が巨大になるのを防ぐ

"""
計算量を削減したクエリ処理
配列を変更するとTLEになる。
インデックスをオフセットする変数を使用することでO(1)で変更できるようにする。

https://atcoder.jp/contests/abc410/tasks/abc410_c
"""
