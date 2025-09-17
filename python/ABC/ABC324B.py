N = int(input())

while N % 2 == 0:
    N //= 2
#     print(N)
# print()

while N % 3 == 0:
    N //= 3
#     print(N)
# print()

# print(N)
print("Yes" if N == 1 else "No")

"""
何を判定する問題？

正整数 NN が N = 2^x * 3^y （x,y ≥ 0)で表せるかを判定します。

アルゴリズム（本命）
「2 と 3 の素因数だけでできているか」を見るだけです。

まず while で
N を 2 で割れるだけ割る

次に while で
N を 3 で割れるだけ割る

最後に
N==1 なら Yes、そうでなければ No

端数・例外：N=1 は 2^0 * 3^0 なのでYes
"""
