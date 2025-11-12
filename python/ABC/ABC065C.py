N, M = map(int, input().split())


def factorial(n):  # 階乗を計算する関数
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i % 1_000_000_007
    return ans


ans = factorial(N) * factorial(M)  # 犬の順列 x 猿の順列
if abs(N - M) > 1:  # 犬と猿の差が2匹以上
    print(0)
elif abs(N - M) == 1:  # 犬と猿の差が1匹
    print(ans % 1_000_000_007)
else:  # abs(N - M) == 0: 犬と猿の差が0匹
    print(ans * 2 % 1_000_000_007)  # 同じ各順列につき、犬先頭のケースと、猿先頭のケース

"""
数学的な気づき系
n匹の順列はn!

けんちょんの解説
https://drken1215.hatenablog.com/entry/2025/01/01/172204

https://atcoder.jp/contests/abc065/tasks/arc076_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6913dbdf-cda8-8320-a0b1-a5fd625e6c7b
"""
