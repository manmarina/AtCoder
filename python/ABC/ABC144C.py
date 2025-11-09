N = int(input())

ans = 10**12  # 最大値は1 x 10^12の場合
i = 1
while i * i <= N:  # √Nまで
    if N % i == 0:  # 約数の場合
        # print(i, N // i)
        ans = min(ans, (i - 1) + (N // i - 1))  # ペアの約数を求め、(1,1)からのマンハッタン距離を計算
    i += 1

print(ans)

"""
数学的な気づき系
約数列挙して約数のペアを求め、(1,1)からマンハッタン距離がもっとも短いペアが答え。

https://atcoder.jp/contests/abc144/tasks/abc144_c
"""
