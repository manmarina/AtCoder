import math

N = int(input())

ans = 10**18  # 十分大きく
for d in range(1, math.isqrt(N) + 1):
    if N % d == 0:
        a, b = d, N // d
        cand = max(len(str(a)), len(str(b)))  # a,bの桁数の大きい方
        if cand < ans:
            ans = cand
print(ans)

"""
約数列挙（平方根まで）
チャッピー

1 〜 sqrt(N)を走査し、d が約数なら相方は N/d。
それぞれの桁数を取り、最大値で答え候補を更新。
"""
