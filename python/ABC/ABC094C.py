from bisect import bisect_left


N = int(input())
X = list(map(int, input().split()))

S = sorted(X)
L = S[N // 2 - 1]
R = S[N // 2]

for x in X:
    j = bisect_left(S, x)  # x の最初の出現位置
    if j < N // 2:
        print(R)  # 左半分から抜ける → 右に寄る
    else:
        print(L)  # 右半分から抜ける → 左に寄る

"""
計算量を削減したシミュレーション + 二分探索
逆順列を使わずに、二分探索で直接削除する値のインデックスを探す。
インデックスを見つけた後の処理は全く逆順列版と同じ。

hamayanhamayanの
https://blog.hamayanhamayan.com/entry/2018/04/15/163238

https://atcoder.jp/contests/abc094/tasks/arc095_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6915561f-3940-8322-9553-1641d4136770
"""
