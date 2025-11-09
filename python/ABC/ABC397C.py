N = int(input())
A = list(map(int, input().split()))

kind = [0] * (N - 1)  # 数列に含まれる数の種類数を管理する配列
set_L = set()  # 左の部分列に含まれる数の種類数を求めるためのset
for i in range(N - 1):
    set_L.add(A[i])
    kind[i] = len(set_L)  # 種類数を格納
# print(kind)

set_R = set()  # 右の部分列に含まれる数の種類数を求めるためのset
for i in reversed(range(1, N)):  # 逆順に追加してゆく
    set_R.add(A[i])
    kind[i - 1] += len(set_R)  # 種類数を加算
# print(kind)

print(max(kind))  # 最大の種類数が答え

"""
計算量を削減したシミュレーション
setへの追加がO(1)となるように、逆順を利用する。
種類数を管理する配列を用意する。

https://atcoder.jp/contests/abc397/tasks/abc397_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69105978-4f60-8322-8674-ba2afc754aa5
"""
