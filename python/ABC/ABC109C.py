from math import gcd


N, X = map(int, input().split())
x = list(map(int, input().split()))

if N == 1:  # 都市が1つの時
    print(abs(X - x[0]))
    exit()

x.append(X)  # リストにスタート地点の座標を追加してソート
x.sort()
# print(x)

diff = set()  # 座標間の距離を格納するset
for i in range(N):  # スタートを追加しているのでrangeはN
    diff.add(x[i + 1] - x[i])

# print(diff)
print(gcd(*diff))  # すべての座標間の距離の最大公約数が答え。

"""
数学的な気づき系
すべての座標間の距離の最大公約数が答え。

テストケース
3 10
5 15 19
を修正してAC

けんちょんの解説
https://drken1215.hatenablog.com/entry/2018/09/08/230200

https://atcoder.jp/contests/abc109/tasks/abc109_c
"""
