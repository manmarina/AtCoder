N = int(input())

n = 2
ans = 1
while n * n * n <= N:  # N以下の立法数を全探索
    n3 = n * n * n
    if str(n3) == str(n3)[::-1]:
        ans = n3  # 回文ならansを更新
    n += 1
print(ans)

"""
数学的な気づき系 + 全探索
リトライ
N以下の回分立方数の最大値を求める。
N 以下の立方数は O(N^(1/3)) 個しかないことを見抜き、全探索する。

https://atcoder.jp/contests/abc343/tasks/abc343_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68f9b584-a80c-8323-b61f-78541874ccc3
"""
