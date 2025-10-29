N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))

j = 1
for i in range(1, N + 1):  # i日目
    while A[j] < i:  # 花火の日が今日よりも前だったら
        j += 1  # 次の花火の日に進める
    next = A[j]  # 次回の花火の日
    print(next - i)  # 次の花火までの日数

"""
基本実装問題
同じ解法が見つからなかった
forループの中のwhileループのカウンタjを、forループのカウンタiで上手に制御する。

けんちょんは後ろから見てゆく解法
https://drken1215.hatenablog.com/entry/2023/10/02/140500

https://atcoder.jp/contests/abc322/tasks/abc322_c
"""
