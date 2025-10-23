N = int(input())

cnt = 0
for A in range(1, N):
    B_count = (N - 1) // A
    cnt += B_count
print(cnt)

"""
工夫して探索の通り数を減らす「全探索 + 枝刈り」

三重ループを一重ループに減らす
PAST本 p.232の解説がとてもわかり易い

https://atcoder.jp/contests/abc179/tasks/abc179_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68f9d423-cf6c-8324-9b18-744f11ac3537
"""
