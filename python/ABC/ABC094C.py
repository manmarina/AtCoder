from collections import defaultdict


N = int(input())
X = list(map(int, input().split()))  # インデックス ->　値

Xs = sorted(X)  # Xをソート
# print("Xs:", Xs)

# Xiの制約が10**9と大きくリストを作成できない
# Xsの逆順列
Xsr = defaultdict(int)  # 値 ->　インデックス
for i in range(N):
    Xsr[Xs[i]] = i
# print("Xsr:", Xsr)

r = Xs[N // 2]  # 中央値の候補 右側
l = Xs[N // 2 - 1]  # 中央値の候補 左側
for i in range(N):
    if Xsr[X[i]] < N // 2:  # 削除する値が左寄りなら、
        print(r)  # 右側が中央値
    else:  # 削除する値が右寄りなら、
        print(l)  # 左側が中央値

"""
計算量を削減したシミュレーション + 逆順列
毎回リストからXiを削除して中央値を求めるとTLE。
削除する値が、ソート後にどこに位置しているかを知るために逆順列を使う。
解となる中央値は2通りしかない。これを左側、右側とする。
削除する値が左寄りなら右側、右寄りなら左側が中央値となる。

hamayanhamayanの解説
https://blog.hamayanhamayan.com/entry/2018/04/15/163238

https://atcoder.jp/contests/abc094/tasks/arc095_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6915561f-3940-8322-9553-1641d4136770
"""
