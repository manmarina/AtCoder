def reconstruct(n):
    # '123'を’123123'に変換する関数
    val = 1
    nn = n
    while nn:
        val *= 10  # 一番大きい桁を切り上げる ex.'123' -> '1000'
        nn //= 10
    return n * val + n


N = int(input())
res = 0

for n in range(1, 1_000_001):
    if reconstruct(n) <= N:
        res += 1
    else:
        break

print(res)

"""
問題を言い換える系
けんちょん
https://drken1215.hatenablog.com/entry/2021/03/20/225100
たとえば 1234512345 は「良い整数」だが、これは「12345」という整数と同一視できる。
このように圧縮した整数の方を全探索すればよいことに気づく。

https://atcoder.jp/contests/abc196/tasks/abc196_c
"""
