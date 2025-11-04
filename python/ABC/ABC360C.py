N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

# A[i] を 0-index に変換
A = [a - 1 for a in A]
print(A)

# 各値ごとに重みを格納
tot = [[] for _ in range(N)]
for i in range(N):
    tot[A[i]].append(W[i])

# 各グループを昇順にソート
for v in range(N):
    tot[v].sort()
print(tot)

# 各グループで、最大値以外の合計を加算
res = 0
for v in range(N):
    if len(tot[v]) >= 2:
        res += sum(tot[v][:-1])  # 最後の（最大の）要素を除いて合計
print(res)

"""
問題文の理解が難解系
どの箱に何個荷物が入っているのかわかりにくい。

けんちょん
https://drken1215.hatenablog.com/entry/2024/07/07/211832

https://atcoder.jp/contests/abc360/tasks/abc360_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6909fff4-f16c-8320-93f2-c577a74c9d6b
"""
