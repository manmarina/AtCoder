N = int(input())
A = list(map(int, input().split()))

sum_ = sum(A[1:])  # sum_を前計算しておく
ans = []
for i in range(N):
    temp = A[i] * sum_  # A[i]以降の合計とA[i]の積
    ans.append(temp)
    if i == N-1:  # 最後の数字のときはそのまま終了
        break  # インデックスのオーバーフローを避けている
    sum_ -= A[i+1]  # sum_をO(1)で更新
print(sum(ans))

"""
計算量を削減したシミュレーション
二重シグマの計算をO(N)で計算できるように変形する。

https://atcoder.jp/contests/abc405/tasks/abc405_c
"""
