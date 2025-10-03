import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 初期区間 [0..M-1]
S = sum(A[:M])                          # 区間和
T = sum((i + 1) * A[i] for i in range(M))  # 重み付き和（1..M）

ans = T
for l in range(1, N - M + 1):

    out = A[l - 1]  # 左端から出る要素
    inn = A[l + M - 1]  # 右端に入る要素

    # S を更新
    S_prev = S
    S = S - out + inn

    # T を更新
    T = T - S_prev + M * inn

    if T > ans:
        ans = T

print(ans)

"""
累積和、重み付き和
チャッピー

「長さ M の連続区間の 重み付き和 を最大化する」問題です。

更新式の導出
S_prev（更新前の区間和）は S - inn + out で表せる。
「区間を右にずらす」と、すべての係数が1つずつ小さくなる。
→ つまり「古い T から S_prev を引けば」係数を 1 つ下げた形になる。
でもそれだと「新しい要素 inn」が 0 倍になってしまうので、そこに M 倍を足して補正する。

https://atcoder.jp/contests/abc267/tasks/abc267_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df4892-df84-8323-b1db-0d89aaf5d05a
"""
