import sys

input = sys.stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))  # 1-indexed

# 「固定点 (fixed point)」の個数を数える変数
# (固定点とは A[i]=i となっている位置 i のこと。)
fixed = 0

# 「相互参照 (mutual reference)」(Ai=jかつAj=i)ペアの個数を数える変数
mutual = 0

for i in range(1, N+1):
    if A[i] == i:
        fixed += 1
    else:
        j = A[i]
        # i < j のときだけ数えると二重カウント防止になる
        if 1 <= j <= N and A[j] == i and i < j:
            mutual += 1

ans = fixed * (fixed - 1) // 2 + mutual  # fixedのペアはnC2の公式で求めている
print(ans)

"""
数え上げ問題
チャッピー

問題文の条件を読み解くのが難しい。
(Ai=i かつ Aj=j)または(Ai=jかつAj=i)
が導けるかが鍵となる。

https://atcoder.jp/contests/abc262/tasks/abc262_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df27aa-e4b0-8321-93be-9d88bd81e47d
"""
