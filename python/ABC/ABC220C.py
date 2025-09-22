N = int(input())
A = list(map(int, input().split()))
X = int(input())

div, mod = divmod(X, sum(A))
cs = 0
cnt = 0
for a in A:
    cs += a
    cnt += 1
    if mod < cs:
        print(div * len(A) + cnt)
        break

"""
累積和
自力解

#1：総和（合計）で“周回”をまとめて処理

#2：残り R は1周内だけ見ればよい
残り R を超える最初の位置を、配列 A を1回だけなめて見つければOK。
具体的には累積和を進め、初めて累積和 >R となる位置（1-indexed）を見つける。

#3：不等号は「>」
問題は「総和が Xを超える 最小の要素数」。よって判定は >= ではなく >。
"""
