N, K = map(int, input().split())
A = set(map(int, input().split()))
# print(A)

total = K * (K + 1) // 2  # K以下の数の合計
for a in A:  # Aの中の要素a
    if a <= K:  # aがK以下だった時
        total -= a  # K以下の数の合計からaを引く

print(total)

"""
計算量を削減したシミュレーション
Aの中に現れない数を探索すると最大2x10^9となってしまう。
K以下の数の合計から、Aの中に現れる数を引いてゆけば残りは現れない数の合計となる。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/08/31/024933

https://atcoder.jp/contests/abc346/tasks/abc346_c
"""
