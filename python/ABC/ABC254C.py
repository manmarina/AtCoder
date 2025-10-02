import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 各余りクラスの要素を集める
bins = [[] for _ in range(K)]
for i, a in enumerate(A):
    bins[i % K].append(a)
# print(bins)

# それぞれ昇順に
for r in range(K):
    bins[r].sort()
# print(bins)

# 昇順に取り出して元の位置に再配置
# bins[r] を前から使っていくので、インデックスを進める
idx = [0] * K
recon = [0] * N
for i in range(N):
    r = i % K
    recon[i] = bins[r][idx[r]]
    idx[r] += 1
# print(idx)
# print(recon)

print("Yes" if recon == sorted(A) else "No")

"""
基本実装問題
チャッピー

操作で交換できるのは「距離が K の倍数」のペアだけ＝同じ余りクラス内。
したがって最終的に昇順にしたいなら、各クラス内の要素のマルチセットが、全体昇順配列の対応位置のマルチセットと一致している必要十分です。

https://atcoder.jp/contests/abc254/tasks/abc254_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de0961-baa8-8320-9267-35636c77e30a
"""
