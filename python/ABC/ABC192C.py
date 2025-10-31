N, K = map(int, input().split())


def g1(n):
    n = [*str(n)]
    n.sort(reverse=True)
    return int(''.join(n))


def g2(n):
    n = [*str(n)]
    n.sort()
    return int(''.join(n))


def f(n):
    return g1(n) - g2(n)


num = N
for i in range(K):
    num = f(num)

print(num)

"""
基本実装問題
問題文通りの関数を作成して愚直に解く。

桁数 d の上限
例えば N ≤ 10⁹ なら d ≤ 9 なので、
d log d はほぼ定数扱いです。
→ 実質 O(K) とみなせます。

https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690445cb-b668-8323-aae2-7b17af34c905
"""
