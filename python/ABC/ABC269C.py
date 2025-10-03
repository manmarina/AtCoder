N = int(input())
s = N
ans = []
while True:
    ans.append(s)
    if s == 0:
        break
    s = (s - 1) & N  # 次の submask

print(ans)
print(*sorted(ans), sep="\n")


"""
ビット全探索（bit全探索） サブマスク(submask)
チャッピー

問題文の理解が難しい
この問題文をかみ砕くと問題文ではこう言っています：
「整数 N が与えられる。x & N = x を満たすすべての整数 x を、小さい順に出力せよ。」

入力例3では
[19, 39, 59]
ビットが3つなので、部分集合は 2^3 = 8通り あります。

「mask = 集合」
「submask = 部分集合」

s = (s - 1) & N
を繰り返すと全てのサブマスクパターンを辿れる（仕組みはよくわからない。。）

https://atcoder.jp/contests/abc269/tasks/abc269_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68e03e82-1670-8323-b3b1-1002ba0c47c6
"""
