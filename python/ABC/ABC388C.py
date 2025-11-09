N = int(input())
A = list(map(int, input().split()))

ans = 0

# a / 2 より大きい最初の要素（なければ最後の次）を表す値 j
j = 0

for a in A:
    # 越えるまで進める
    while j < N and A[j] * 2 <= a:
        j += 1  # 自分の大きさの半分以下の餅の数
    ans += j

print(ans)

"""
計算量を削減したシミュレーション + しゃくとり法
解説+チャッピー
二分探索では、自分の大きさの倍以上のもちの数を求めたが、
しゃくとり法では、自分の大きさの半分以下の餅の数を求めてゆく。

https://atcoder.jp/contests/abc388/tasks/abc388_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6910c8f2-d858-8323-9214-856f944e1028
"""
