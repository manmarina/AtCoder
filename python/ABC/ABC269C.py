N = int(input())

pos = [i for i in range(N.bit_length()) if (N >> i) & 1]
k = len(pos)
# print(pos)
# print(k)

ans = []
for mask in range(1 << k):        # 0..2^k-1
    x = 0
    for j in range(k):
        if (mask >> j) & 1:
            x |= 1 << pos[j]      # 選んだ位置のビットを立てる
    ans.append(x)

# print(ans)
ans.sort()
print(*ans, sep="\n")

"""
ビット全探索（bit全探索）
チャッピー

問題文の理解が難しい
この問題文をかみ砕くと問題文ではこう言っています：
「整数 N が与えられる。x & N = x を満たすすべての整数 x を、小さい順に出力せよ。」

入力例3では
[19, 39, 59]
ビットが3つなので、部分集合は 2^3 = 8通り あります。

https://atcoder.jp/contests/abc269/tasks/abc269_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68e03e82-1670-8323-b3b1-1002ba0c47c6
"""
