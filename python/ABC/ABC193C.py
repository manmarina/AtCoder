N = int(input())

ab = set()  # N以下のべき乗数を格納するset
a = 2
while a * a <= N:  # 2から√Nまで（√Nの二乗はNを超えてしまうので）
    val = a * a  # aの二乗からスタート
    while val <= N:  # N以下の間
        ab.add(val)
        val *= a  # 指数を1増やす（^2 -> ^3 -> ^4...）
    a += 1  # aを1増やす

print(N - len(ab))  # NからN以下のべき乗数の数を引いたものが答え

"""
数学的な気づき系
√Nまで探索すれば良いことを見抜く。
なぜなら√Nより大きい整数は二乗するとNより大きくなるからだ。

チャッピーの
例：N=100 の場合
を見るとわかりやすい。

けんちょん
https://drken1215.hatenablog.com/entry/2021/03/02/140000

https://atcoder.jp/contests/abc193/tasks/abc193_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69102bf7-218c-8323-aa18-e9e8dfd7b8ff
"""
