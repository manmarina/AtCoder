def is_prime(num):
    lim = int(num ** 0.5)  # 調べる数の平方根が上限
    for i in range(2, lim + 1):
        if num % i == 0:  # 割り切れたら即False
            return False
    return True


X = int(input())

num = X
while True:
    if is_prime(num):
        print(num)
        exit()
    num += 1  # 素数でなければ、一つ大きい数の判定をする

"""
数学的な気づき系
素数判定

https://atcoder.jp/contests/abc149/tasks/abc149_c
"""
