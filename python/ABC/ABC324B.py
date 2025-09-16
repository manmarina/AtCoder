N = int(input())


def prime_factorization_dict(n):  # 素因数分解する関数
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


# 素因数が2と3だけならYes、そうでなければNo
prime = prime_factorization_dict(N)
# print(prime)

if set(prime.keys()) <= {2, 3}:
    print("Yes")
else:
    print("No")

"""
if set(prime.keys()) in ({2}, {3}, {2, 3}):

ここで prime.keys() が 空集合 のケースを考えてみましょう。
例えば N = 1 のとき、素因数分解すると factors = {} になります。

1 は 2**0 * 3**0
 と表せるので答えは Yes ですが、
あなたのコードでは set(prime.keys()) = set() となり、 {2}, {3}, {2,3} のいずれにも一致せず No になってしまいます。

これが WA の原因です。

if set(prime.keys()) <= {2, 3}:

これなら prime.keys() が空集合でも {2,3} の部分集合とみなされるので Yes になります。
"""
