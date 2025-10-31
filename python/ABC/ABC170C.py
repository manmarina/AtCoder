X, N = map(int, input().split())
P = set(map(int, input().split()))

i = 0
while True:
    if X + i in P and X - i in P:  # Xの+-1が存在する場合
        i += 1  # iを進める
        continue

    if X - i in P:  # X-1が存在するなら
        print(X + i)  # X+1を表示して終了
        break
    else:  # if X + i in P
        print(X - i)  # X+1が存在するなら
        break  # X-1を表示して終了（X+-1が存在しない時こちらが優先される）

"""
基本実装問題

探している数がsetに存在しないときに表示する。

https://atcoder.jp/contests/abc170/tasks/abc170_c
"""
