import sys

input = sys.stdin.readline
N, K, X = map(int, input().split())
A = list(map(int, input().split()))

# 1) まとめて引けるだけ引く
for i in range(N):
    if K == 0:
        break
    t = min(K, A[i] // X)  # tはクーポン使用数
    A[i] -= t * X
    K -= t

# 2) 残りKで大きいものから0にする
A.sort(reverse=True)
ans = sum(A[K:])  # 先頭use個は実質0に
print(ans)

"""
貪欲法（Greedy）+ソート
チャッピー

クーポン1枚で「好きなAiからXを引く（負にならない）」。
合計K枚で配列の総和を最小にしたい。

https://atcoder.jp/contests/abc246/submissions/69770080
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68dd347d-1d94-832d-8fcc-d5303aca53b1
"""
