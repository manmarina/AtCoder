MOD = 10**9 + 7


def sieve(n: int) -> list[int]:
    """エラトステネスの篩で n 未満の素数を列挙"""
    isprime = [True] * n
    isprime[0] = False
    isprime[1] = False
    res = []
    for i in range(2, n):
        if isprime[i]:
            res.append(i)
            for j in range(i * 2, n, i):
                isprime[j] = False
    # print(isprime)
    return res


N = int(input())
res = 1

# N 以下の素数
primes = sieve(N + 1)
# print(primes)

# N!の正の約数の個数を計算　ルジャンドルの定理
for p in primes:  # 全ての素因数の個数を求める
    exp = 0  # 素因数pの指数（=pの個数）
    N2 = N
    while N2:
        exp += N2 // p
        N2 //= p
    # 素因数分解を利用した約数の個数の求め方の公式
    # 素因数pの指数expより 全ての素因数の(exp + 1)の積が正の約数の個数
    res = res * (exp + 1) % MOD  # オーバーフローを避けるため毎回剰余を計算

# # 比較のため
# # Nの正の約数の個数を計算
# n2 = N
# for p in primes:
#     exp = 0  # 素因数pの指数
#     while n2 % p == 0:
#         n2 //= p
#         exp += 1
#     # 素因数分解を利用した約数の個数の求め方の公式
#     # 素因数pの指数expより 全ての素因数の(exp + 1)の積が正の約数の個数
#     res = res * (exp + 1) % MOD　# オーバーフローを避けるため毎回剰余を計算

print(res)

"""
 N! の正の約数の個数の計算
素因数分解はエラトステネスの篩を利用

ルジャンドルの定理
N! = 1x2x…xN の各素因数 p の指数を集計します。
Legendre の公式（最短・数学寄り）
    ある素数 p に対し、N! における p の指数は
    e_p = ⌊N/p⌋ + ⌊N/p²⌋ + ⌊N/p³⌋ + …（0 になったら終了）
    N 以下の素数を列挙（エラトステネスの篩）して、各 p について上式で e_p を求める。
素因数分解を利用した約数の個数の求め方の公式を利用して正の約数の個数の計算して終了

比較のために
N の正の約数の個数の計算
素因数分解を利用した約数の個数の求め方の公式を利用
も試した。
"""
