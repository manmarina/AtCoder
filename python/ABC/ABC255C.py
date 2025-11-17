X, A, D, N = map(int, input().split())

# 数列の最大値、最小値を設定
if D > 0:  # Dが正の時
    mx = A + D * (N - 1)
    mn = A
else:  # Dが負の時
    mx = A
    mn = A + D * (N - 1)
# print(mx)

# 早期終了条件 Xが数列の範囲外の時
if X >= mx:
    print(X - mx)
    exit()
elif X <= mn:
    print(mn - X)
    exit()

# Xが数列の範囲内の時
if D > 0:  # Dが正のとき
    t = (X - A) // D
    L = A + D * t
    R = A + D * (t + 1)
    # print("L:", L, "R:", R)
    print(min(X - L, R - X))
else:  # Dが負のとき
    t = -(A - X) // D
    L = A + D * (t + 1)
    R = A + D * t
    print(min(X - L, R - X))

"""
数学的な気づき系
リトライ
ざっくり言うと「数直線上の等差数列のうち、x に一番近い項との差の最小値」を O(1) で求める問題です。
チャッピーの解のほうが正規化しているのでわかりやすくてスマート。

https://atcoder.jp/contests/abc255/tasks/abc255_c
"""
