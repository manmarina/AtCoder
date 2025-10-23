def check(n: int) -> bool:
    s = str(n)
    t = s[::-1]
    return s == t  # 回文かどうかブール値を返す


n = int(input())

ans = 0
i = 1
while i * i * i <= n:  # 立方数がnを超えたら終了
    if check(i * i * i):  # 回文なら
        ans = i * i * i  # ansを更新
    i += 1

print(ans)

"""
数学的な気づき系
N以下の回分立方数の最大値を求める。
N 以下の立方数は O(N^(1/3)) 個しかないことを見抜く。

https://atcoder.jp/contests/abc343/tasks/abc343_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68f9b584-a80c-8323-b61f-78541874ccc3
"""
