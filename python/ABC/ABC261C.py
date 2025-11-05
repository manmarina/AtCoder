from collections import defaultdict


N = int(input())
S = [input() for _ in range(N)]
# print(S)

dd = defaultdict(int)
for i in range(N):
    cnt = dd[S[i]]
    if cnt == 0:
        print(S[i])
        dd[S[i]] += 1
    else:
        print(f"{S[i]}({dd[S[i]]})")
        dd[S[i]] += 1

"""
文字列処理 x 連想配列（ハッシュマップ）

https://atcoder.jp/contests/abc261/tasks/abc261_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de2fb5-575c-8321-89a9-d45ab3b032c
"""
