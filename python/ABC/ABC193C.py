N = int(input())

ok = set()
for i in range(2, int(N**0.5) + 1):
    n = i * i
    while n <= N:
        ok.add(n)
        n *= i

# print(ok)
print(N - len(ok))

"""
数学的な気づき系
リトライ
√Nまで探索すれば良いことを見抜く。
なぜなら√Nより大きい整数は二乗するとNより大きくなるからだ。
けんちょんとほぼ同じ実装ができた！

チャッピーの
例：N=100 の場合
を見るとわかりやすい。

けんちょん
https://drken1215.hatenablog.com/entry/2021/03/02/140000

https://atcoder.jp/contests/abc193/tasks/abc193_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69102bf7-218c-8323-aa18-e9e8dfd7b8ff
"""
