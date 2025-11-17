X, A, D, N = map(int, input().split())

# dを正規化
if D < 0:
    A = A + D * (N - 1)  # Aを数列の最小値にする
    D = -D

# 数列の最大値、最小値を設定
mx = A + D * (N - 1)
mn = A

# 早期終了条件 Xが数列の範囲外の時
if X >= mx:
    print(X - mx)
    exit()
elif X <= mn:
    print(mn - X)
    exit()

# Xが数列の範囲内の時
t = X - mn
r = t % D
print(min(r, D - r))

"""
数学的な気づき系
リトライ
ざっくり言うと「数直線上の等差数列のうち、x に一番近い項との差の最小値」を O(1) で求める問題です。
チャッピーの解のほうが正規化しているのでわかりやすくてスマート。
正規化したバージョンも書いておく。

https://atcoder.jp/contests/abc255/tasks/abc255_c
"""
