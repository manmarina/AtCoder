S = input().strip()
N = len(S)

# 全ペア数 N*(N-1)/2
res = N * (N - 1) // 2

can_S = 0
cnt = [0] * 26

# 文字数カウント
for c in S:
    cnt[ord(c) - ord('a')] += 1

# 同じ文字同士のペアを引く & S自身になれるか判定
for v in range(26):
    if cnt[v] >= 2:
        can_S = 1
    res -= cnt[v] * (cnt[v] - 1) // 2

print(res + can_S)

"""
計算量を削減したシミュレーション
けんちょん
https://drken1215.hatenablog.com/entry/2024/09/04/015546
操作によってできるものの個数を数え上げる系の問題の最も基本的な問題！

https://atcoder.jp/contests/abc345/tasks/abc345_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692e74dd-60c0-8320-857d-a4db22cff847
"""
