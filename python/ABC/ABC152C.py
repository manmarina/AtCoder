N = int(input())
P = list(map(int, input().split()))
# print(P)

mi = N + 1  # 最小値の初期値を範囲外にする
res = 0
for p in P:  # すべてのPについて
    mi = min(mi, p)  # 前回の最小値と、今回の値ではどちらが小さいか
    if mi == p:  # 今回の値が最小ならば
        res += 1  # カウントを1増やす

print(res)


"""
問題文の理解が難解系
「左から見て、これまでで一番小さい要素の数を数える問題」
任意の整数 j に対して、という表現で、すべてのPjよりも一番小さいと理解する必要がある。

計算量を削減したシミュレーション
最小値の更新がO(1)でできるように工夫する。

けんちょん
https://drken1215.hatenablog.com/entry/2020/01/22/120400

https://atcoder.jp/contests/abc152/tasks/abc152_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6904a9e4-1098-8324-b9f4-c680deb3e4cf
"""
